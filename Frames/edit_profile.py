from PyQt6.QtCore import QStandardPaths
import requests
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QKeyEvent, QPixmap
from PyQt6 import QtCore
from PyQt6.QtWidgets import QStackedLayout, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import EditProfileButton
from Frames.change_profile_pic import ChangeAvatar
from styles.styles import edit_profile_button, edit_profile_button_clicked, messages_buttons
from components.input_user import ImageViewer
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QGuiApplication
from components.global_functions import QLabel_Exit
from PyQt6.QtWidgets import QFrame
from components.messages import MessagesWidget
from Frames.private_message import PrivateMessageFrame
from Frames.page_5_layout import PageFiveLayout
from Frames.page_4_security import PageSecurityLayout
from Frames.page_3_contacts import PageFriendsLayout, StackContacts


class ChatWidget(QWidget):
    def __init__(self, parent=None, username=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.username = username
        self.show()
        self.raise_()
        self.setWindowTitle("Chat Flotante")
        self.profile_image = QPixmap(f'profiles/images/{self.username}.png')
        # This is the average color of the image
        image_array = self.load_image(f'profiles/images/{self.username}.png')
        average_color = self.get_average_color(image_array)
        # Makes the background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.username_label = QLabel(self.username)
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_label.setStyleSheet(
            'color: white;text-align: center;font: 75 20pt "MS Shell Dlg 2";')
        self.add_friend = QPushButton("Friend Request")
        self.add_friend.setStyleSheet(f'QPushButton {{ \
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
            stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
            stop:1 rgba({average_color[0]}, {average_color[1]}, {average_color[2]}, 1)); \
            color: white; font: bold 10pt "MS Shell Dlg 2";}} \
            QPushButton:pressed {{color: rgb(0, 0, 128); background-color: white;}}')
        # self.add_friend.setStyleSheet(
        #     'QPushButton {color: white; background-color: rgba(0, 0, 128, 1);\
        #         solid black; font: bold 10pt "MS Shell Dlg 2";} \
        #     QPushButton:pressed {color: rgb(0, 0, 128); background-color: white;}')
        self.add_friend.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_message = QPushButton("Send Message")
        self.send_message.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_message.setStyleSheet(f'QPushButton {{ \
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
            stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
            stop:1 rgba({average_color[0]}, {average_color[1]}, {average_color[2]}, 1)); \
            color: white; font: bold 10pt "MS Shell Dlg 2";}} \
            QPushButton:pressed {{color: rgb(0, 0, 128); background-color: white;}}')

        # Create a container widget for the layout
        container_widget = QWidget(self)
        container_widget.setGeometry(0, 0, 256, 384)

        container_widget.setStyleSheet(
            f'background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
                stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
                    stop:1 rgba({average_color[0]+20}, {average_color[1]+20}, {average_color[2]+20}, 1)); \
    border: 1px solid black; border-radius: 2px;')

        # We make the layout
        layout = QVBoxLayout(container_widget)
        image_profile = QLabel('')
        # Quality: (0 means no compression, 100 is the best quality)
        scaled_image = self.profile_image.scaledToWidth(
            300, QtCore.Qt.TransformationMode.SmoothTransformation)
        image_profile.setPixmap(QtGui.QPixmap(scaled_image))
        image_profile.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_profile)
        layout.addWidget(self.username_label)
        # Horizontal box for add friend and send message buttons
        horizontal_box = QHBoxLayout()
        horizontal_box.addWidget(self.add_friend)
        horizontal_box.addWidget(self.send_message)
        layout.addLayout(horizontal_box)

        self.setLayout(layout)
        self.setGeometry(300, 80, 20, 120)
        self.animation_steps = 100
        self.current_step = 0
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_start)


class ProfileViewBackground(QWidget):
    signal_profile_close = QtCore.pyqtSignal()

    def __init__(self, parent=None, username=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle(f"Background Profile View of {username}")
        self.username = username
        # Makes the background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setGeometry(-500, -500, 8000, 8000)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.hide()

        self.animation_steps = 100
        self.current_step = 0
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_close)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(""))
        self.setLayout(layout)
        self.setStyleSheet('background-color: rgba(0, 0, 0, 0.8);')

    def show_profile(self):
        print('profile showww background')
        self.show()
        self.raise_()

    # def mousePressEvent(self, event) -> None:
    #     self.signal_profile_close.emit()
    #     self.hide()

    def animate_size_close(self):
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 - self.current_step / self.animation_steps * \
                0.4  # Ajuste para partir desde un tamaño más pequeño
            scaled_width = int(self.screen_width * factor * 0.35)
            scaled_height = int(self.screen_height * factor * 0.35)
            self.setGeometry(0, 0, scaled_width, scaled_height)
        else:
            self.current_step = 0
            self.timer_expand_animation_close.stop()
            self.setGeometry(0, 0, int(self.screen_width * 0.7),
                             int(self.screen_height * 0.7))
            self.hide()


class EditProfile(QWidget):

    def __init__(self, parent=None, username=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.parent = parent  # Store the reference to the main window
        self.username = ''
        self.jwt = ''
        self.animation_steps = 50
        self.current_step = 0
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_start)
        self.timer_expand_animation_close = QtCore.QTimer(self)
        self.timer_expand_animation_close.timeout.connect(
            self.animate_size_close)
        self.init_gui()
        self.hide()

        # self.instance_optional = QPushButton('Optional instance')

        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # Monitor dimensions
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
        # The bellowing line isn't necessary, but it is for ensuring the geometry
        self.setGeometry(0, 0, int(self.screen_width * 0.7),
                         int(self.screen_height*0.7))
        self.setStyleSheet('background-color: rgba(30, 30, 30, 1);')

    def close_and_det_first_page(self):
        print(' aaaaaaaaaaaaaaaaaaaa REVISAR ESTO AYUDA')
        self.change_page(optional_number=1)
        self.hide()

    def show_profile(self):
        self.show()
        self.raise_()
        self.timer_expand_animation.start(1)
        self.setFocus()

    # def instance_optional_close(self, cchat_frame):
    #     self.instance_optional = cchat_frame

    # def close_shadow(self, event=None) -> None:
    #     print('instanceee', self.instance_optional)
    #     self.instance_optional.hide()
    #     self.timer_expand_animation_close.start(1)

    def animate_size_start(self):
        if self.current_step < 3:
            print('backkk')
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 + self.current_step / self.animation_steps * \
                0.4  # Ajuste para partir desde un tamaño más pequeño
            scaled_width = int(self.screen_width * factor * 0.5)
            scaled_height = int(self.screen_height * factor * 0.5)
            self.setGeometry(0, 0, scaled_width, scaled_height)
        else:
            self.current_step = 0
            self.timer_expand_animation.stop()
            self.setGeometry(0, 0, int(self.screen_width * 0.7),
                             int(self.screen_height * 0.7))
        self.private_message_frame.username = self.username

    def animate_size_close(self):
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 - self.current_step / self.animation_steps * \
                0.4  # Ajuste para partir desde un tamaño más pequeño
            scaled_width = int(self.screen_width * factor * 0.35)
            scaled_height = int(self.screen_height * factor * 0.35)
            self.setGeometry(0, 0, scaled_width, scaled_height)
        else:
            self.current_step = 0
            self.timer_expand_animation_close.stop()
            self.setGeometry(0, 0, int(self.screen_width * 0.7),
                             int(self.screen_height * 0.7))
            self.hide()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_1:
            self.stack_button1.click()
        elif event.key() == Qt.Key.Key_2:
            self.stack_button2.click()
        elif event.key() == Qt.Key.Key_3:
            self.stack_button3.click()
        elif event.key() == Qt.Key.Key_4:
            self.stack_button4.click()
        elif event.key() == Qt.Key.Key_5:
            self.stack_button5.click()
        elif event.key() == Qt.Key.Key_C:
            self.compose_button.click()
        elif event.key() == Qt.Key.Key_R:
            self.received_button.click()
        elif event.key() == Qt.Key.Key_Escape:
            self.go_back_pixmap.signal_profile_close.emit()

    def get_username(self, username):
        pass
        # self.username = username
        # print('userrrrr', self.username)
        # self.charging_image()
        # print('userrrrr', self.username)

    def change_profile_pic(self) -> None:
        change_avatar_frame = ChangeAvatar(self)
        change_avatar_frame.show()

    def jwt_receiver(self, jwt: str, username: str) -> None:
        self.jwt = jwt
        self.username = username
        # If we have the jwt, we can start the GUI of the StackContacts
        self.stacked_contacts.get_token_and_username(self.jwt, self.username)

        # The following lines are for set the profile image
        # Upload profile image
        # TODO delete the following instance

        self.image_viewer = ImageViewer(username=self.username, jwt=self.jwt)
        self.image_viewer.load_button.clicked.connect(self.load_image)
        self.image_viewer.retrieve_image_get(self.username, self.jwt)

        self.page1_layout.addWidget(self.image_viewer)
        self.page1_layout.update()
        self.messages_widget.jwt = self.jwt
        self.messages_widget.username = self.username
        # TODO: fix the line below
        self.messages_widget.retrieve_messages()

    def load_image(self):
        self.image_viewer.username = self.username
        self.image_viewer.jwt = self.jwt

        file_path, _ = QFileDialog.getOpenFileName(
            self, 'ConnectX - Set your new profile picture!', '', 'Images (*.png *.jpg *.jpeg)')
        if file_path:
            pixmap = QPixmap(file_path).scaled(
                400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.image_viewer.image_label.setPixmap(pixmap)
            self.image_viewer.image_label.setScaledContents(True)

            self.image_viewer.upload_image_post(
                self.username, self.jwt, file_path)
            self.image_viewer.update()

            with open(f"profiles/images/{self.username}.png", "wb") as f:
                f.write(open(file_path, 'rb').read())

        # self.image_viewer.destroy()

    # def charging_image(self):
    #     path_file = f'profiles/images/{self.username}.png'
    #     if os.path.exists(path_file):
    #         print(
    #             f'El archivo {path_file} existe, ergo no la creamos')
    #     else:
    #         print(f'El archivo {path_file} NO existe.')
    #         create_new_os_image = open(path_file, 'wb')
    #         # Ahora creamos la imagen a partir de Anonoymous.png
    #         create_new_os_image.write(
    #             open('profiles/images/Anonymous.png', 'rb').read())
    #         create_new_os_image.close()
    #         self.image_pixmap = QPixmap(path_file)
    # def emit_signal_send_message_offline(self):
    #     message = self.private_message_frame.qlabel_to_write.text()
    #     to_username = self.private_message_frame.username_label.toPlainText()
    #     self.signal_send_message_offline.emit(
    #         self.username, to_username, message)
    #     print('emit_signal_send_message_offline', self.username,
    #           to_username, message)

    def init_gui(self) -> None:
        self.labels = {}

        # QLabel image assignation
        window_size = self.size()
        self.labels['label_image'] = QLabel(self)
        # TODO
        # TODO Empezamos con la imagen de perfil por defecto, luego hay que
        # pedirla cada vez que se inicie la aplicación, pero revisando
        # antes si esta descargada en la ubicacion de self.username TODO
        # self.labels['label_image'].setPixmap(self.image_pixmap)
        self.labels['label_image'].setScaledContents(True)
        self.labels['label_image'].setGeometry(200, 200, 300, 300)
        self.labels['label_image'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        # TODO
        self.labels['label_image'].setMaximumSize(window_size)
        self.labels['label_image'].setGeometry(0, 0, 0, 0)
        self.labels['label_image'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image'].show()

        # 1 Button
        self.stack_button1 = EditProfileButton(
            'logoutnButton', 0, 'Account [1]', self)
        self.stack_button1.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button1.setStyleSheet(
            edit_profile_button)
        self.stack_button1.setStyleSheet(edit_profile_button_clicked)
        # TODO CHnage this variables.
        image_florence = 'images/florence.jpg'
        aristotle_1 = 'images/aristotle_1.jpg'

        # 1 Layout
        # 2 Button
        self.stack_button2 = EditProfileButton(
            'logoutnButton', 1, 'Messages [2]', self)
        self.stack_button2.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button2.setStyleSheet(
            edit_profile_button)

        # 3 Button
        self.stack_button3 = EditProfileButton(
            'logoutnButton', 2, 'Contacts [3]', self)
        self.stack_button3.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button3.setStyleSheet(
            edit_profile_button)
        # 4 Button
        self.stack_button4 = EditProfileButton(
            'logoutnButton', 3, 'Security [4]', self)
        self.stack_button4.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button4.setStyleSheet(
            edit_profile_button)
        # 5 Button
        self.stack_button5 = EditProfileButton(
            'logoutnButton', 4, 'Settings [5]', self)
        self.stack_button5.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button5.setStyleSheet(
            edit_profile_button)
        # 6 Button
        self.go_back_pixmap = QLabel_Exit()
        self.go_back_pixmap.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # 5 Layout
        # QLabel image assignation
        self.labels['label_image5'] = QLabel(self)
        self.labels['label_image5'].setMaximumSize(window_size)
        self.labels['label_image5'].setGeometry(50, 50, 300, 300)
        self.labels['label_image5'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = image_florence
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image5'].setPixmap(image_pixmap)
        self.labels['label_image5'].setScaledContents(True)
        self.labels['label_image5'].setGeometry(200, 200, 300, 300)
        self.labels['label_image5'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image5'].show()

        # Buttons Grouped
        self.buttons_grouped = QHBoxLayout()
        self.buttons_grouped.addStretch(1)
        self.buttons_grouped.addWidget(self.stack_button1)

        self.buttons_grouped.addWidget(self.stack_button2)

        self.buttons_grouped.addWidget(self.stack_button3)

        self.buttons_grouped.addWidget(self.stack_button4)

        self.buttons_grouped.addWidget(self.stack_button5)
        self.buttons_grouped.addStretch(1)
        self.buttons_grouped.addWidget(self.go_back_pixmap)
        # le ponemos stilo al hqboxlayour buttons

        self.page1_layout = QHBoxLayout()
        # self.page1_layout.addWidget(self.labels['label_image1'])

        # page1_layout.addWidget(self.upload_image)
        # self.labels['label_image']
        # self.page1_layout.addWidget(self.labels['label_image'])
        container1 = QWidget()
        container1.setLayout(self.page1_layout)

        # page2_layout.addWidget(self.labels['label_image2'])
        # Compose a new message Button
        page2_layout_buttons = QVBoxLayout()
        self.compose_button = QPushButton('Compose Message [C]')
        self.compose_button.setStyleSheet(messages_buttons)
        self.compose_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        page2_layout_buttons.addWidget(self.compose_button)
        self.private_message_frame = PrivateMessageFrame()
        self.compose_button.clicked.connect(
            self.private_message_frame.emit_signal_send_message_offline)
        # Received messages Button
        self.received_button = QPushButton('Received [R]')
        self.received_button.setStyleSheet(messages_buttons)
        self.received_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        # TODO: TODO: TODO: TODO:
        # self.received_button.clicked.connect(self.retrieve_private_messages)
        page2_layout_buttons.addWidget(self.received_button)
        # Sended messages Button
        sended_button = QPushButton('Sended')
        sended_button.setStyleSheet(messages_buttons)
        sended_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        page2_layout_buttons.addWidget(sended_button)

        #
        page_layout_messages = QVBoxLayout()
        self.messages_widget = MessagesWidget()
        # Connecting the button that retrieves the messages
        self.received_button.clicked.connect(
            self.messages_widget.retrieve_messages)
        page_layout_messages.addWidget(self.messages_widget)
        container2 = QWidget()

        page2_layout_general = QHBoxLayout()
        page2_layout_general.addLayout(page_layout_messages)
        page2_layout_general.addLayout(page2_layout_buttons)
        container2.setLayout(page2_layout_general)

        self.stacked_contacts = StackContacts(
            token=self.jwt)
        container3 = QWidget()
        container3.setLayout(self.stacked_contacts)

        self.page4_layout = PageSecurityLayout()
        container4 = QWidget()
        container4.setLayout(self.page4_layout)

        self.page5_layout = PageFiveLayout()
        container5 = QWidget()
        container5.setLayout(self.page5_layout)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container1)
        self.stacked_layout.addWidget(container2)
        self.stacked_layout.addWidget(container3)
        self.stacked_layout.addWidget(container4)
        self.stacked_layout.addWidget(container5)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.buttons_grouped)
        main_layout.addLayout(self.stacked_layout)
        self.setLayout(main_layout)
        self.setStyleSheet("background-color: rgba(70, 70, 70, 245);")

    def change_page(self, optional_number=None):
        sender = self.sender()
        if optional_number == 1:  # Si salimos del menu, de vuelve al indice 0.
            self.stacked_layout.setCurrentIndex(0)
            self.stack_button1.setStyleSheet(edit_profile_button)
            self.stack_button1.setStyleSheet(edit_profile_button_clicked)
            # eliminamos el efecto de clickeado de todos los botones
            # TODO no eficiente recorrerlos, mejor filtrar por id luego
            self.stack_button2.setStyleSheet(edit_profile_button)
            self.stack_button3.setStyleSheet(edit_profile_button)
            self.stack_button4.setStyleSheet(edit_profile_button)
            self.stack_button5.setStyleSheet(edit_profile_button)
            self.update()
        else:
            self.stacked_layout.setCurrentIndex(sender.index)
            self.stack_button1.setStyleSheet(edit_profile_button)
            self.stack_button2.setStyleSheet(edit_profile_button)
            self.stack_button3.setStyleSheet(edit_profile_button)
            self.stack_button4.setStyleSheet(edit_profile_button)
            self.stack_button5.setStyleSheet(edit_profile_button)
            for i in range(6):
                if i == sender.index:
                    sender.setStyleSheet(edit_profile_button_clicked)
            self.update()
