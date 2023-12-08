import os
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QBrush, QPalette, QPainter, QPixmap, QCursor
from components.buttons import Upload_file, Login_Button, Button, Chat_Button
from styles.styles import welcome_user_style, button_style, login_label, login_label_wrong, login_label_ok
from PyQt6.QtCore import QStandardPaths, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudio
from components.global_functions import center_window
import requests
from io import BytesIO


class FrameLogin(QWidget):
    signal_frame_login = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.jwt_token = ''
        # Lounge looped music
        self.media_player = QMediaPlayer(self)
        self.media_player.setAudioOutput(QAudioOutput(self))
        file_url = QUrl.fromLocalFile(os.path.join('Music', 'music2.opus'))
        self.media_player.setSource(file_url)
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)
        self.play_media()
        self.init_gui()

        # Crear un QPalette personalizado con la imagen de fondo
        palette = QPalette()
        background_image = QPixmap(os.path.join('images', '759324.jpg'))

        background_image = background_image.scaled(
            self.size()*2, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
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

    def jws_writter(self, jwt_token: str) -> None:
        self.jwt_token = jwt_token
        print("it's the actual token:", jwt_token)

    def manage_music(self):
        sender = self.sender()
        if sender.name == 'musicButton':
            if sender.music_status == True:
                print('pausada')
                self.media_player.pause()
            elif sender.music_status == False:
                print('reanudada')
                self.media_player.play()

    # def closeEvent(self, event):
    #     # Then, before closing the window, we need to close the sockets and threads
    #     self.signal_frame_login.emit('close')
    #     self.client_thread.join()

    def play_media(self):
        self.media_player.play()

    def handle_media_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.media_player.setPosition(0)  # Restart song when finished
            self.play_media()

    # def open_file(self) -> None:
    #     initial_dir = QStandardPaths.writableLocation(
    #         QStandardPaths.StandardLocation.DocumentsLocation)
    #     self.upload_qfile = QFileDialog.getOpenFileName(
    #         self, 'Upload image', initial_dir, 'All files (*)')
    #     if self.upload_qfile:
    #         print(f'Selected file: {self.upload_qfile}')
    #         dir_image = self.upload_qfile[0]
    #         image_pixmap = QPixmap(dir_image)

    #         self.labels['label_image'].setPixmap(image_pixmap)
    #         self.labels['label_image'].setScaledContents(True)
    #         self.labels['label_image'].setGeometry(200, 200, 300, 300)
    #         self.labels['label_image'].setAlignment(
    #             QtCore.Qt.AlignmentFlag.AlignCenter)
    #         self.labels['label_image'].show()
    #         image = image_pixmap.toImage()
    #         buffer = QtCore.QBuffer()
    #         buffer.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)
    #         image.save(buffer, "PNG")
    #         image_bytes = buffer.data()
    #         url = 'http://localhost:8000/uploadimagen/'
    #         files = {'files': ('blob', BytesIO(image_bytes))}
    #         response = requests.post(url, files=files)
    #         print(f'Response from server: {response.json()}')

    def launch(self):
        sender = self.sender()
        if sender.login_status == True:
            print('Session initiated')
            print('logoutbutton username:', self.logout_button.username)
            self.labels['username_status'].setText('Credentials OK')
            self.labels['username_status'].setStyleSheet(login_label_ok)
            self.labels['username_status'].repaint()  # To avoid bugs
            center_window(self)
            self.show()
            self.setFocus()

    def open_edit_account(self):
        print('logoutbutton username:', self.logout_button.username)
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
            username = sender.username
            self.labels['username'].setText(f'Welcome {username}')
            self.setWindowTitle(f'ConectX Project - {username}')
            self.labels['username'].repaint()  # To avoid bugs

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

        # # Upload profile image
        # self.upload_image = Upload_file(
        #     'uploadButton', (300, 250), 'Upload file', self)
        # self.upload_image.setCursor(
        #     QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        # self.upload_image.setStyleSheet(
        #     button_style)
        # self.upload_image.clicked.connect(self.open_file)

        # Edtir profile
        self.edit_account = Button(
            'editAccount', (300, 250), 'My account', self)
        self.edit_account.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_account.setStyleSheet(
            button_style)
        # self.edit_account.clicked.connect(self.open_edit_account)

        # Logout
        self.logout_button = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button.setStyleSheet(
            button_style)
        self.logout_button.clicked.connect(self.change_username_status)

        # CHAT
        self.chat_button = Chat_Button(
            'chatButton', (300, 250), 'Chat', self)
        self.chat_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.chat_button.setStyleSheet(
            button_style)
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

        # Crear un QPalette personalizado con la imagen de fondo
        palette = QPalette()
        background_image = QPixmap('759324.jpg')
        brush = QBrush(background_image)
        palette.setBrush(QPalette.ColorRole.Window, brush)

        # Aplicar el QPalette al widget
        self.setPalette(palette)

        # Pixmap background
        # background_image = QPixmap(os.path.join('images', '759324.jpg'))
        # self.background_label = QLabel(self)
        # self.background_label.setPixmap(background_image)
        # self.background_label.setGeometry(0, 0, 1280, 720)
        # self.background_label.setStyleSheet(
        #     'background-image: url(images/759324.jpg);')
        # self.background_label.setScaledContents(True)

        vbox.addLayout(hbox1)

        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addStretch(2)
        vbox.addWidget(self.labels['username_status'])
        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addStretch(5)
        self.setLayout(vbox)
