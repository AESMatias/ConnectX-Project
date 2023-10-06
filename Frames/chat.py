from time import sleep
import socket
from threading import Thread
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Upload_file, Register_Button, Login_Button, InputField, Button
from styles.styles import button_style, global_style, login_label, login_label_wrong, login_label_ok

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudio
from Login.client_socket import ClientCommunicator


class ChatFrame(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.init_gui()
        self.host = "127.0.0.1"
        self.port = 12345
        # Create the client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_communicator = ClientCommunicator(
            self.host, self.port, self.username)
        self.client_thread = Thread(target=self.client_communicator.run_client)

    def launch(self):
        sender = self.sender()
        print('sender', sender)
        if sender.login_status == True:
            print('CHAT initiated')
            self.labels['username_status'].setText('Credentials OK')
            self.labels['username_status'].setStyleSheet(login_label_ok)
            self.labels['username_status'].repaint()  # To avoid bugs
            self.show()
            self.client_thread.start()
            self.change_username_status()
            return True

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
            self.client_communicator.username = username

    def new_message(self, message):
        sender = self.sender()
        if message:
            self.labels['msg'].setText(message)
            self.labels['msg'].repaint()  # To avoid bugs

    def init_gui(self) -> None:
        # Window Geometry
        self.setGeometry(100, 200, 1000, 800)
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
        self.labels['label_image'].setMaximumSize(window_size)
        self.labels['label_image'].setGeometry(50, 50, 300, 300)
        self.labels['label_image'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        self.labels['username_status'] = QLabel('', self)
        self.labels['username_status'].setStyleSheet(login_label)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['username_status'].repaint()

        # Message Label
        self.labels['msg'] = QLabel('MESSAGE>', self)
        self.labels['msg'].setStyleSheet(login_label)
        self.labels['msg'].setStyleSheet(login_label_ok)
        self.labels['msg'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['msg'].repaint()

        # Write a message
        self.write_message = QLineEdit(self)
        self.write_message.setStyleSheet(login_label)
        self.write_message.setFixedSize(550, 60)
        self.write_message.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.write_message.repaint()

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.labels['username'])
        self.labels['username'].setScaledContents(True)

        # second
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.write_message)

        # Third Horizontal Layout
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.labels['msg'])
        self.labels['msg'].setScaledContents(True)
        hbox3.addStretch(1)

        # Vertical
        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        # vbox.addLayout(hbox3)

        vbox.addStretch(2)
        vbox.addWidget(self.labels['username_status'])
        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # vbox.addWidget(self.labels['image_input'])
        vbox.addStretch(5)
        self.setLayout(vbox)

        # if self.launch() == True:
        #     print('th4read startttt')
        #     self.client_thread.start()

        # self.login_button.login_signal.connect(client_thread.start)
