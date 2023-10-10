import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QFileDialog, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Upload_file, Login_Button, Button, Chat_Button
from styles.styles import button_style, login_label, login_label_wrong, login_label_ok
from PyQt6.QtCore import QStandardPaths, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudio
<<<<<<< Updated upstream
from components.global_functions import center_window
=======
import requests
from io import BytesIO
>>>>>>> Stashed changes


class FrameLogin(QWidget):
    signal_frame_login = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.init_gui()
        # Lounge looped music
        self.media_player = QMediaPlayer(self)
        self.media_player.setAudioOutput(QAudioOutput(self))
        file_url = QUrl.fromLocalFile(os.path.join('Music', 'music2.opus'))
        self.media_player.setSource(file_url)
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)
        self.play_media()

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

    def open_file(self) -> None:
        initial_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DocumentsLocation)
        self.upload_qfile = QFileDialog.getOpenFileName(
            self, 'Upload image', initial_dir, 'All files (*)')
        if self.upload_qfile:
            print(f'Selected file: {self.upload_qfile}')
            dir_image = self.upload_qfile[0]
            image_pixmap = QPixmap(dir_image)
            
            self.labels['label_image'].setPixmap(image_pixmap)
            self.labels['label_image'].setScaledContents(True)
            self.labels['label_image'].setGeometry(200, 200, 300, 300)
            self.labels['label_image'].setAlignment(
                QtCore.Qt.AlignmentFlag.AlignCenter)
            self.labels['label_image'].show()
            image = image_pixmap.toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)
            image.save(buffer, "PNG") 
            image_bytes = buffer.data() 
            url = 'http://localhost:8000/uploadimagen/'  
            files = {'files': ('blob', BytesIO(image_bytes))}
            response = requests.post(url, files=files)
            print(f'Response from server: {response.json()}')

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
        sender = self.sender()
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
        self.labels['username'] = QLabel(f'Welcome {self.username}', self)
        self.labels['username'].setStyleSheet(login_label_ok)
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

        # Upload profile image
        self.upload_image = Upload_file(
            'uploadButton', (300, 250), 'Upload file', self)
        self.upload_image.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.upload_image.setStyleSheet(
            button_style)
        self.upload_image.clicked.connect(self.open_file)

        # Edtir profile
        self.edit_account = Button(
            'editAccount', (300, 250), 'Edit your account', self)
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
            'chatButton', (300, 250), 'CHAT', self)
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
        # Second Horizontal Layout
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.upload_image)
        hbox2.addStretch(1)
        # Third Horizontal Layout
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
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addStretch(2)
        vbox.addWidget(self.labels['username_status'])
        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # vbox.addWidget(self.labels['image_input'])
        vbox.addStretch(5)
        self.setLayout(vbox)
