from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QScrollArea, QSizePolicy)
from PyQt6.QtGui import QPixmap
from styles.styles import InputFieldStyle, login_label_ok
from components.chat_functions import QLabelProfilePicture, ChatWidget, ProfileViewBackground, QLabelMessage
from typing import Tuple, List
import requests
import os
import json
from PyQt6.QtGui import QPalette, QBrush
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QScrollBar


class ChatFrame(QWidget):
    send_message_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.counter_chat_enter = 0
        self.counter_messages = 0
        self.username = ''
        self.username_tuple = ()
        self.active_users_chat = (0, '')
        qlabelpixamap = QLabel(self)
        qlabelpixamap.setPixmap(QPixmap('images/logo32.png'))
        self.image_pixmap_1 = qlabelpixamap
        self.image_pixmap_1.setVisible(False)
        self.profile_pixmap = QPixmap('images/profile_image.png')
        self.init_gui()
        self.host = "127.0.0.1"
        self.port = 12345
        self.hide()
        self.raise_()
        self.timer_active_users = QtCore.QTimer()
        self.timer_active_users.timeout.connect(self.active_users)
        self.timer_active_users.start(15000)
        self.timer_scroll_to_bottom = QtCore.QTimer()
        self.timer_scroll_to_bottom.timeout.connect(self.scroll_to_bottom)
        self.timer_scroll_to_bottom.start(250)
        self.intentos_restantes_jwt = 1
        # Profile View
        self.chat_widget = ChatWidget()
        self.chat_widget.hide()
        # Profile View Background
        self.background_widget = ProfileViewBackground(self, self.username)
        self.background_widget.hide()
        self.pixmaps_profiles_array = []
        self.background_widgets_list = []
        self.chat_widgets_list = []
        self.hor_layouts_to_delete = []
        self.animation_steps = 50
        self.current_step = 0
        self.timer_animate_start = QtCore.QTimer()
        self.timer_animate_start.timeout.connect(self.animate_size_start)
        self.timer_animate_close = QtCore.QTimer()
        self.timer_animate_close.timeout.connect(self.animate_size_close)
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # Monitor dimensions
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
        # The bellowing line isn't necessary, but it is for ensuring the geometry
        self.setGeometry(0, 0, int(self.screen_width * 0.7),
                         int(self.screen_height*0.7))

        # Create a custom QPalette with the background image
        palette = QPalette()
        background_image = QPixmap(
            os.path.join('images', 'wallpaper_chat.jpg'))
        self.setAutoFillBackground(True)
        self.brush = QBrush(background_image)
        palette.setBrush(QPalette.ColorRole.Window, self.brush)
        self.setPalette(palette)
        self.setStyleSheet(f"""
            QWidget {{
                background-image: url({background_image});
                background-repeat: no-repeat;
                background-position: center;
                background-color: rgba(0, 0, 0, 128);
            }}
        """)

    def animate_size_start(self):
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 + self.current_step / self.animation_steps * \
                0.4  # Ajuste para partir desde un tamaño más pequeño
            scaled_width = int(self.screen_width * factor * 0.5)
            scaled_height = int(self.screen_height * factor * 0.5)
            self.setGeometry(0, 0, scaled_width, scaled_height)
        else:
            self.current_step = 0
            self.timer_animate_start.stop()
            self.setGeometry(0, 0, int(self.screen_width * 0.7),
                             int(self.screen_height * 0.7))

    def animate_size_close(self):
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 - self.current_step / self.animation_steps * \
                0.4  # Ajuste para partir desde un tamaño más pequeño
            scaled_width = int(self.screen_width * factor * 0.4)
            scaled_height = int(self.screen_height * factor * 0.4)
            self.setGeometry(0+self.current_step*12, 0 +
                             self.current_step*6, scaled_width, scaled_height)
            print('self.current_step: ', self.current_step)
        else:
            self.current_step = 0
            self.timer_animate_close.stop()
            self.setGeometry(0, 0, int(self.screen_width * 0.7),
                             int(self.screen_height * 0.7))
            self.hide()

    def retrieve_image_get(self, username: str) -> Tuple[bool, str]:
        url = 'http://localhost:8000/user/profilePIC/'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {str(self.jwt)}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(f"profiles/images/{username}.png", "wb") as f:
                f.write(response.content)
        elif response.status_code == 404:
            print('status_code 404: No existe la imagen de perfil')
            return QPixmap('profiles/images/Anonymous.png')

    def closeEvent(self, event):
        print("Closing the window")
        # Then, before closing the window, we need to close the sockets and threads
        # self.client_communicator.client_socket.close()
        # self.client_communicator.send_message_socket.close()

        # We need to close the thread too, fix this!!!!!!!!! TO-DO:
        # self.client_thread.join()
        # self.client_communicator._stop_threads = True
        # cerramos los hilos todos y los sockets abiedrtos tambien
        # self.client_communicator.client_socket.close()
        # self.client_communicator.send_message_socket.close()
    # def close_all(self):
    #     print(f"Closing the window{self}")
    #     self.client_communicator.client_socket.close()
    #     self.client_communicator.send_message_socket.close()
    #     self.client_thread.join()

    def scroll_to_bottom(self):
        # Después de inicializar el QScrollArea
        scroll_bar = self.scroll_area.verticalScrollBar()
        # Set the scrollbar value directly to the maximum
        scroll_bar.setValue(scroll_bar.maximum()+56)
        QCoreApplication.processEvents()

    def keyPressEvent(self, event) -> None:
        if event.key() == QtCore.Qt.Key.Key_Return or event.key() == 16777220:
            self.send_message()

    def jwt_receiver(self, jwt: str) -> List[str]:
        self.jwt = jwt

    def active_users(self) -> Tuple[bool, str]:
        print('active_users function in chat.py every 15 seconds')
        url = 'http://localhost:8000/active/'
        headers = {'accept': 'application/json'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            active_users_decoded = response.content.decode('utf-8')
            list_of_active_users = json.loads(active_users_decoded)
            self.active_users_chat = len(
                list_of_active_users), list_of_active_users
            self.labels['username'].setText(
                f'{self.active_users_chat[0]} Users online')
            self.labels['users_active'].setText('Active users: \n \n{}'.format(
                '\n'.join(self.active_users_chat[1])))
            return len(list_of_active_users), list_of_active_users

        elif response.status_code == 404:
            print('status_code 404 active users')

    def launch(self) -> None:
        sender = self.sender()
        if sender.login_status == True:
            self.active_users_chat = self.active_users()
            self.counter_chat_enter += 1
            self.username = sender.username
            self.labels['username'].setText(
                f'{self.active_users_chat[0]} Users online')
            self.labels['users_active'].setText('Active users: \n\n{}'.format(
                '\n'.join(self.active_users_chat[1])))

            self.move(0, 0)
            self.show()
            self.raise_()
            self.setFocus()
            # self.client_thread = Thread(
            #     target=self.client_communicator.run_client)
            # self.client_thread.start()
            self.change_username_status()  # TODO VER ESTO, NO SE USA

            self.timer_animate_start.start(1)

    def send_message(self, event=None):
        text = self.write_message.text()
        message = f"general|{self.jwt}|{self.username}|{text}"
        self.send_message_signal.emit(message)
        self.write_message.setText('')
        if text.endswith('/close') or text.endswith('/exit'):
            pass
            # print('closing threads and sockets by send_message func')
            # # self.client_communicator.client_socket.close()
            # self.client_communicator.send_message_socket.close()
            # self.client_thread.join()
        # Después de inicializar el QScrollArea

    def change_username_status(self):
        sender = self.sender()
        if sender.login_status == False:
            # self.labels['username_status'].setText('Invalid credentials')
            # self.labels['username_status'].setStyleSheet(login_label_wrong)
            # self.labels['username_status'].repaint()  # To avoid bugs
            pass
        elif sender.login_status == True:
            username = sender.username
            # self.labels['username'].setText(f'Welcome {username}')
            # self.setWindowTitle(f'ConectX Project - {username}')
            # self.labels['username'].repaint()  # To avoid bugs
            # self.client_communicator.username = username
            pass

    def get_pic_by_name(self, username: str, optional_object=None) -> QPixmap:
        if username == 'Anonymous':
            # If the username does not have a profile picture, we return the default one
            return QPixmap('profiles/images/Anonymous.png')
        else:
            with open(f"profiles/images/{username}.png", "rb") as f:
                # f.write(response.content)
                if optional_object and username:
                    print('OPTIONAL OBJECT WIDGETTT AT GETPICNBYNAME CHAT.PY')
                    optional_object.change_pixmap(username)
                else:
                    print('ELSEEEEEEE AT GETPICBYNAME IN CHAT DOT PY')
                    return QPixmap(f"profiles/images/{username}.png")

    def new_message(self, message):
        # TODO Change the username tuple
        # username, message = message.split(':')
        username, message_text = message.split(':')

        if username not in self.username_tuple:
            # self.username_tuple += (username,)

            # abrimos /profiles/images/username.png y miramos si existe tal archivo
            # si existe, lo cargamos, si no, lo descargamos
            path_file = f'profiles/images/{username}.png'

            # Verificar si el archivo existe
            if os.path.exists(path_file):
                print(
                    f'The file {path_file} exists, ergo we do not download it again.')
            else:
                pass  # mientras
                # print(f'El archivo {ruta_archivo} NO existe.')
                # image_retrieved = self.retrieve_image_get(username)
                # if image_retrieved is not None:
                #     print(' not NONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE A A A A A')
                #     self.pixmap_username = image_retrieved
                # else:
                #     self.pixmap_username = self.get_pic_by_name(username)
                #     print('Obteniendo pixmap del usuario ', username)

        # NO SE USA ESTO TODO
        self.qlabelpixamap = QLabelProfilePicture(username)
        # qlabelpixamap.setPixmap(self.pixmap_username.scaledToWidth(
        #     32, QtCore.Qt.TransformationMode.SmoothTransformation))
        self.qlabelpixamap.setContentsMargins(100, 100, 100, 100)
        self.qlabelpixamap.setStyleSheet(
            "QLabel { padding: 50px; background-color: rgba(0,0,0,0); border-radius:10px;}")
        self.qlabelpixamap.setCursor(Qt.CursorShape.PointingHandCursor)
        # abajo enviamos un evento al qlabelpixamap
        self.qlabelpixamap.label_enter_event_first()
        # This is the last message
        self.pixmaps_profiles_array.append(self.qlabelpixamap)
        # repintamos la imagen
        self.qlabelpixamap.repaint()
        # self.chat_widget.profile_image = self.pixmap_username #does not exist  pixmapusername before
        self.chat_widget.__init__(self)
        if message:
            self.counter_messages += 1

            if len(self.all_messages2) < 25:
                # self.all_messages.append([self.image_pixmap_1, message])
                # self.all_messages2.append(message)
                self.qlabel_message = QLabelMessage()
                self.qlabel_message.setWordWrap(True)
                self.qlabel_message.setText(message)
                self.qlabel_message.setTextInteractionFlags(
                    Qt.TextInteractionFlag.TextSelectableByMouse)
                # Allow vertical expansion
                size_policy = QSizePolicy(
                    QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                self.qlabel_message.setSizePolicy(size_policy)

                horizontal_layout = QHBoxLayout()

                horizontal_layout.addWidget(self.qlabelpixamap)
                horizontal_layout.addWidget(self.qlabel_message)
                horizontal_layout.setGeometry(QtCore.QRect(10, 10, 550, 60))

                self.hor_layouts_to_delete.append(horizontal_layout)
                self.container_layout.addLayout(horizontal_layout)
                self.all_messages2.append(message_text)
            elif len(self.all_messages2) >= 25:
                print('HAN LLEGADO 150 MENSAJES POR LO QUE SE BORRAN TODOS MUAJAJAJA')
                # self.all_messages.pop(0)
                # self.all_messages.append([self.image_pixmap_1, message])
                self.all_messages2.clear()
                for _ in range(10):
                    for elem in self.container_widget.children():
                        if type(elem) == QLabelMessage or type(elem) == QLabelProfilePicture or type(elem) == QLabel:
                            print('borrando elem', elem)
                            elem.deleteLater()

                for elem in self.pixmaps_profiles_array:
                    elem.deleteLater()
                for elem in self.background_widgets_list:
                    elem.deleteLater()
                for elem in self.chat_widgets_list:
                    elem.deleteLater()
                self.pixmaps_profiles_array.clear()
                self.background_widgets_list.clear()
                self.chat_widgets_list.clear()
                self.hor_layouts_to_delete.clear()
                # Then, we add the new message

                # NO SE USA ESTO TODO
                self.qlabelpixamap = QLabelProfilePicture(username)
                # qlabelpixamap.setPixmap(self.pixmap_username.scaledToWidth(
                #     32, QtCore.Qt.TransformationMode.SmoothTransformation))
                self.qlabelpixamap.setContentsMargins(100, 100, 100, 100)
                self.qlabelpixamap.setStyleSheet(
                    "QLabel { padding: 50px; background-color: rgba(0,0,0,0); border-radius:10px;}")
                self.qlabelpixamap.setCursor(Qt.CursorShape.PointingHandCursor)
                # abajo enviamos un evento al qlabelpixamap
                self.qlabelpixamap.label_enter_event_first()
                # This is the last message
                self.pixmaps_profiles_array.append(self.qlabelpixamap)
                # repintamos la imagen
                self.qlabelpixamap.repaint()
                # self.chat_widget.profile_image = self.pixmap_username #does not exist  pixmapusername before
                self.chat_widget.__init__(self)

                self.qlabel_message = QLabelMessage()
                self.qlabel_message.setWordWrap(True)
                self.qlabel_message.setText(message)
                self.qlabel_message.setTextInteractionFlags(
                    Qt.TextInteractionFlag.TextSelectableByMouse)
                # Allow vertical expansion
                size_policy = QSizePolicy(
                    QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                self.qlabel_message.setSizePolicy(size_policy)

                horizontal_layout = QHBoxLayout()

                horizontal_layout.addWidget(self.qlabelpixamap)
                horizontal_layout.addWidget(self.qlabel_message)
                horizontal_layout.setGeometry(QtCore.QRect(10, 10, 550, 60))

                self.hor_layouts_to_delete.append(horizontal_layout)
                self.container_layout.addLayout(horizontal_layout)
                self.all_messages2.append(message_text)
            # Profile View Background
            background_widget = ProfileViewBackground(self, username)
            background_widget.hide()
            # Profile View
            chat_widget = ChatWidget(self, username)
            chat_widget.hide()

            self.get_pic_by_name(
                username, chat_widget)
            try:
                self.pixmaps_profiles_array[-1].signal_profile_picture_clicked.connect(
                    background_widget.show_profile)
            except IndexError:
                print('IndexError at chat.py 1')
            try:
                self.pixmaps_profiles_array[-1].signal_profile_picture_clicked.connect(
                    chat_widget.show_profile)
            except IndexError:
                print('IndexError at chat.py 2')
            try:
                background_widget.signal_profile_close.connect(
                    chat_widget.hide_profile)
            except IndexError:
                print('IndexError at chat.py 3')
            self.background_widgets_list.append(background_widget)
            self.chat_widgets_list.append(chat_widget)

            print('----------LENNNNNNNNN aprox of the messages:',
                  len(self.pixmaps_profiles_array), len(
                      self.background_widgets_list), len(self.chat_widgets_list))

    def init_gui(self) -> None:

        # Grid Layout
        self.grid = QGridLayout()
        # Labels
        self.labels = {}
        self.labels['username'] = QLabel(f'Welcome {self.username}', self)
        self.labels['username'].setStyleSheet(login_label_ok)
        self.labels['username'].setFixedSize(300, 50)
        self.labels['username'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['username'].repaint()

        # QLabel users active
        self.labels['users_active'] = QLabel(self)
        self.labels['users_active'].setFixedHeight(700)
        self.labels['users_active'].setFixedWidth(270)
        self.labels['users_active'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['users_active'].setText('')
        self.labels['users_active'].setStyleSheet(
            "QLabel { background-color: rgba(80,80,80,0.5); border-radius:10px;\
                text-align: center; font: bold 12pt 'MS Shell Dlg 2';color: white;}")

        self.write_message = QLineEdit(self)
        self.write_message.setStyleSheet(InputFieldStyle)
        self.write_message.setFixedSize(550, 60)
        self.write_message.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.write_message.setPlaceholderText('Write a message...')
        self.write_message.setStyleSheet(
            "QLineEdit { background-color: rgba(255,255,255,0.25); border-radius:1px;padding:\
            0px; margin: 0px; font: bold 15pt 'MS Shell Dlg 2';color: white;}")
        self.write_message.repaint()
        self.all_messages = []
        self.all_messages2 = []

        for _ in range(5):
            self.all_messages2.append('')
        # self.labels['msg'].setText('\n'.join(self.all_messages))

        # All the messages will be stored in a list of tuples (image,username,message)

        # for _ in range(5):
        #     self.all_messages.append([self.image_pixmap_1, ''])
        # self.labels['msg'].setText('\n'.join(self.all_messages2))

        # Crear un layout horizontal
        self.messages_images_layout = QVBoxLayout()
        self.messages_images_layout.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.labels['username'])
        self.labels['username'].setScaledContents(True)

        # second
        hbox2 = QHBoxLayout()
        # qlabel to back
        go_back_pixmap = QLabel(self)
        go_back_pixmap.setPixmap(QPixmap('images/undo64.png'))
        # hacemos que cuando hagamos click en qlabelpixamap, se envie un evento
        go_back_pixmap.setCursor(Qt.CursorShape.PointingHandCursor)
        go_back_pixmap.setFixedHeight(64)
        go_back_pixmap.setFixedWidth(64)
        go_back_pixmap.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        # Definimos una función para manejar el evento de clic del mouse

        def handle_mouse_click(event):
            if event.button() == Qt.MouseButton.LeftButton:
                # Acciones a realizar cuando se hace clic izquierdo
                self.timer_animate_close.start(1)

        # Conectamos la función al evento de clic del mouse
        go_back_pixmap.mousePressEvent = handle_mouse_click

        send_pixmap = QLabel(self)
        send_pixmap.setPixmap(QPixmap('images/send64.png'))
        send_pixmap.setCursor(Qt.CursorShape.PointingHandCursor)
        send_pixmap.setFixedHeight(64)
        send_pixmap.setFixedWidth(64)
        send_pixmap.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        send_pixmap.mousePressEvent = self.send_message

        hbox2.addWidget(self.write_message)
        hbox2.addWidget(send_pixmap)
        hbox2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        hbox_2_and_3 = QHBoxLayout()
        hbox_2_and_3.addLayout(hbox2)
        hbox_2_and_3.addWidget(go_back_pixmap)
        # hbox3 = QHBoxLayout()
        # hbox3.addWidget(qlabelpixamap)
        # hbox3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        # Create a scroll area and the container
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Create a widget to contain the layout
        self.container_widget = QWidget(self.scroll_area)
        self.scroll_area.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0.2); color: white;")
        self.container_layout = QVBoxLayout(self.container_widget)
        # Set the container widget as the scroll area's widget
        self.scroll_area.setWidget(self.container_widget)
        self.scroll_area.setWidgetResizable(True)
        self.container_widget.setMinimumHeight(500)
        self.scroll_area.setMinimumHeight(500)
        self.scroll_area.setMaximumHeight(500)
        self.scroll_area.setMaximumHeight(500)
        self.scroll_area.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.container_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # self.container_widget.setLayout(self.container_layout)
        # self.container_layout.addLayout(messages_layout)
        # messages_layout = QVBoxLayout()
        # # Add your existing self.messages_images_layout to the messages_layout
        # messages_layout.addLayout(self.messages_images_layout)

        # Vertical
        vbox = QVBoxLayout()
        vbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.scroll_area)
        vbox.addStretch(1)
        vbox.addLayout(hbox_2_and_3)
        # vbox.addWidget(self.container_widget)
        vbox.addStretch(2)
        # vbox.addWidget(self.labels['username_status'])
        # self.labels['username_status'].setScaledContents(True)
        # self.labels['username_status'].setAlignment(
        #     QtCore.Qt.AlignmentFlag.AlignCenter)

        # vbox.addWidget(self.labels['image_input'])
        vbox.addStretch(5)
        hbox_final = QHBoxLayout()
        hbox_final.addLayout(vbox)
        hbox_final.addWidget(self.labels['users_active'])
        self.setLayout(hbox_final)
