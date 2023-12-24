import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QBrush, QPalette, QPixmap, QCursor
from components.buttons import Login_Button, Button, Chat_Button
from styles.styles import welcome_user_style, button_style_logged, login_label, login_label_wrong, login_label_ok
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

from threading import Thread
from Login.client_socket import ClientCommunicator
from PyQt6.QtCore import pyqtSignal
from time import sleep
from Frames.edit_profile import EditProfile, ProfileViewBackground
from Frames.chat import ChatFrame
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtCore import Qt


class FrameLogin(QWidget):
    signal_frame_login = pyqtSignal(str)
    send_message_login = pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.jwt = ''
        self.host = "127.0.0.1"
        self.port = 12345

        self.client_communicator = ClientCommunicator(
            self.host, self.port, self.username)
        self.client_thread = Thread(
            target=self.client_communicator.run_client)

        self.chat_frame = ChatFrame(self)

        # Lounge looped music
        self.media_player = QMediaPlayer(self)
        self.media_player.setAudioOutput(QAudioOutput(self))
        file_url = QUrl.fromLocalFile(os.path.join('Music', 'music2.opus'))
        self.media_player.setSource(file_url)
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)
        self.screen = QGuiApplication.primaryScreen()
        self.screen_geometry = self.screen.geometry()
        # Monitor dimensions
        self.screen_width = self.screen_geometry.width()
        self.screen_height = self.screen_geometry.height()
        self.play_media()
        self.edit_account_frame = EditProfile(self)
        self.init_gui()

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Return or event.key() == 16777220:
            self.login_button.click()
        if event.key() == Qt.Key.Key_1:
            self.chat_button.click()
        elif event.key() == Qt.Key.Key_2:
            self.edit_account.click()
        elif event.key() == Qt.Key.Key_Escape:
            # TODO: set a counter with QTimer to avoid closing the app by mistake
            pass

    def send_first_message(self):
        # Método para enviar el primer mensaje después de que el cliente esté listo
        # self.first_message = f"general|{self.jwt}|general|MESSAGE_LOGIN"
        # print(' SENDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        # self.send_message_login.emit(self.first_message)
        sleep(0)  # Without this sleep, the first message is not sent
        self.client_communicator.username = self.username
        # self.client_thread = Thread(
        #     target=self.client_communicator.run_client)
        # self.client_thread.start()
        message = f"general|{self.jwt}|general|MESSAGE_LOGIN"
        self.send_message_login.emit(message)

    def jws_writter(self, jwt: str, username=None) -> None:
        self.jwt = jwt

    def manage_music(self):
        sender = self.sender()
        if sender.name == 'musicButton':
            if sender.music_status == True:
                print('pausada')
                self.media_player.pause()
            elif sender.music_status == False:
                print('reanudada')
                self.media_player.play()

    def play_media(self):
        self.media_player.play()

    def handle_media_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.media_player.setPosition(0)  # Restart song when finished
            self.play_media()

    def center_window(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # Monitor dimensions
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # # Stablish the frame position in the center of the screen
        # frame_to_center.setGeometry(x_position, y_position, 1280, 720)
        self.setFixedSize(int(screen_width * 0.7),
                          int(screen_height*0.7))
        # self.setGeometry(0, 0, int(screen_width * 0.6),
        #                  int(screen_height*0.6))
        self.move(int(screen_width)-int(self.width()*1.2),
                  int(screen_height)-int(self.height()*1.3))

        # Crear un QPalette personalizado con la imagen de fondo
        palette = QPalette()
        background_image = QPixmap(os.path.join(
            'images', 'wallpaper_profile.jpg'))

        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)
        background_image = background_image.scaled(
            window_width, window_height, QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)

        self.setAutoFillBackground(True)
        brush = QBrush(background_image)
        palette.setBrush(QPalette.ColorRole.Window, brush)
        self.setPalette(palette)
        self.setStyleSheet(f"""
            QWidget {{
                background-image: url({background_image});
                background-repeat: no-repeat;
                background-position: center;
                background-color: rgba(0, 0, 0, 128);  /* 128 es el valor de opacidad (0-255) */
            }}
        """)

    def launch(self):
        sender = self.sender()
        if sender.login_status == True:
            print('Session initiated')
            self.change_username_status()
            self.labels['username_status'].setText('Credentials OK')
            self.labels['username_status'].setStyleSheet(login_label_ok)
            self.labels['username_status'].repaint()  # To avoid bugs
            self.center_window()
            # self.setGeometry(0, 0, int(self.screen_width * 0.5),
            #                  int(self.screen_height*0.5))
            # self.move(int(self.screen_width)-int(self.width()*1.5),
            #           int(self.screen_height)-int(self.height()*1.5))
            self.show()
            self.setFocus()
            self.client_communicator.username = self.username

            # self.client_communicator.username = self.username
            # self.client_thread = Thread(
            #     target=self.client_communicator.run_client)
            # self.client_thread.start()
            # message = f"general|{self.jwt}|general|MESSAGE_LOGIN"
            # self.send_message_login.emit(message)

            # Asigna el nombre de usuario antes de iniciar el hilo del cliente
            self.client_communicator.username = self.username
            self.client_thread.start()
            self.send_first_message()
            # # Verifica si el hilo del cliente ya se está ejecutando
            # if not self.client_communicator.is_running():
            #     self.client_thread = Thread(
            #         target=self.client_communicator.run_client)
            #     self.client_thread.start()
            #     self.send_first_message()
            #     print(" no esta running asi que STARTED AAAAAAAAAAAAAA")
            # else:
            #     self.send_first_message()
            #     print("Client thread is already running.")

            # # Envía el mensaje de inicio de sesión solo si el hilo del cliente está en ejecución
            # if self.client_communicator.is_running():
            #     message = f"general|{self.jwt}|general|MESSAGE_LOGIN"
            #     self.client_thread = Thread(
            #         target=self.client_communicator.run_client)
            #     self.client_thread.start()
            #     self.send_first_message()

            #     print('THREAD STARTED WITH self.username = ', self.username)
            # else:
            #     print("Unable to send login message. Client thread is not running.")

    def open_edit_account(self):
        self.labels['username_status'].setText('Credentials OK')
        self.labels['username_status'].setStyleSheet(login_label_ok)
        self.labels['username_status'].repaint()  # To avoid bugs
        self.show()

    def change_username_status(self):
        sender = self.sender()
        if sender.login_status == False:
            self.labels['username_status'].setText('Invalid credentials')
            self.labels['username_status'].setStyleSheet(login_label_wrong)
            self.labels['username_status'].repaint()  # To avoid bugs
        elif sender.login_status == True:
            self.username = sender.username
            self.labels['username'].setText(f'Welcome {self.username}')
            self.setWindowTitle(f'ConectX Project - {self.username}')
            self.labels['username'].repaint()  # To avoid bugs
            # self.send_first_message()
            # TODO

    def init_gui(self) -> None:
        # Grid Layout
        self.grid = QGridLayout()
        # Labels
        self.labels = {}
        self.labels['username'] = QLabel(f'Welcome, {self.username}', self)
        self.labels['username'].setStyleSheet(welcome_user_style)
        self.labels['username'].setFixedSize(550, 60)
        self.labels['username'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['username'].repaint()

        # QLabel image assignation
        window_size = self.size()
        self.labels['label_image'] = QLabel(self)
        self.labels['label_image'].hide()
        self.labels['label_image'].setMaximumSize(window_size)
        self.labels['label_image'].setGeometry(0, 0, 0, 0)
        self.labels['label_image'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # Edtir profile
        self.edit_account = Button(
            'editAccount', (300, 250), ' Menu [2] ', self)
        self.edit_account_shadow = ProfileViewBackground(self)
        # self.edit_account_frame.instance_optional_close(
        #     self.edit_account_shadow)

        self.edit_account.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_account.setStyleSheet(
            button_style_logged)
        # self.edit_account.clicked.connect(self.open_edit_account)

        # Logout
        self.logout_button = Login_Button(
            'logoutnButton', (300, 250), ' Close session', self)
        self.logout_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button.setStyleSheet(
            button_style_logged)
        self.logout_button.clicked.connect(self.change_username_status)

        # CHAT
        self.chat_button = Chat_Button(
            'chatButton', (300, 250), ' Chat [1] ', self)
        self.chat_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.chat_button.setStyleSheet(
            button_style_logged)
        self.chat_button.clicked.connect(self.change_username_status)

        # UsernameStatus
        self.labels['username_status'] = QLabel('', self)
        self.labels['username_status'].setStyleSheet(login_label)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['username_status'].repaint()

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.labels['username'])
        self.labels['username'].setScaledContents(True)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.chat_button)
        hbox3.addStretch(1)
        # Four
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(self.edit_account)
        hbox4.addStretch(1)
        # Five CHAT
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addWidget(self.logout_button)
        hbox5.addStretch(1)
        # Hbox6
        hbox6 = QHBoxLayout()
        hbox6.addStretch(1)
        hbox6.addWidget(self.labels['label_image'])
        hbox6.addStretch(1)
        # Vertical
        vbox = QVBoxLayout()
        vbox.addStretch(2)

        # # Crear un QPalette personalizado con la imagen de fondo
        # palette = QPalette()
        # background_image = QPixmap('759324.jpg')
        # brush = QBrush(background_image)
        # palette.setBrush(QPalette.ColorRole.Window, brush)

        # # Aplicar el QPalette al widget
        # self.setPalette(palette)

        # Pixmap background
        # background_image = QPixmap(os.path.join('images', '759324.jpg'))
        # self.background_label = QLabel(self)
        # self.background_label.setPixmap(background_image)
        # self.background_label.setGeometry(0, 0, 1280, 720)
        # self.background_label.setStyleSheet(
        #     'background-image: url(images/759324.jpg);')
        # self.background_label.setScaledContents(True)

        vbox.addLayout(hbox1)

        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(2)

        vbox.addLayout(hbox6)
        vbox.addStretch(1)
        vbox.addWidget(self.labels['username_status'])
        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addStretch(3)
        self.setLayout(vbox)
