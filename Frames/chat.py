from threading import Thread
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit)
from PyQt6.QtGui import QPixmap, QCursor
from styles.styles import InputFieldStyle, login_label, login_label_wrong, login_label_ok
from components.global_functions import center_window
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudio
from Login.client_socket import ClientCommunicator
from PyQt6.QtGui import QPixmap, QCursor, QCloseEvent


class ChatFrame(QWidget):
    send_message_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.init_gui()
        self.host = "127.0.0.1"
        self.port = 12345
        self.client_communicator = ClientCommunicator(
            self.host, self.port, self.username)
        # self.client_thread = Thread(target=self.client_communicator.run_client)

    def closeEvent(self, event):
        print("Closing the window")
        # Then, before closing the window, we need to close the sockets and threads
        # self.client_communicator.client_socket.close()
        # self.client_communicator.send_message_socket.close()
        self.client_thread.join()

    # def close_all(self):
    #     print(f"Closing the window{self}")
    #     self.client_communicator.client_socket.close()
    #     self.client_communicator.send_message_socket.close()
    #     self.client_thread.join()

    def keyPressEvent(self, event) -> None:
        if event.key() == QtCore.Qt.Key.Key_Return or event.key() == 16777220:
            self.send_message()

    def launch(self) -> None:
        sender = self.sender()
        if sender.login_status == True:
            print('CHAT initiated')
            self.username = sender.username
            self.labels['username'].setText(f'Welcome {self.username}')
            self.setWindowTitle(f'ConectX Project - {self.username}')
            self.client_communicator.username = self.username
            self.labels['username_status'].setText('Credentials OK')
            self.labels['username_status'].setStyleSheet(login_label_ok)
            self.labels['username_status'].repaint()  # To avoid bugs
            center_window(self)
            self.show()
            self.setFocus()
            self.client_thread = Thread(
                target=self.client_communicator.run_client)
            self.client_thread.start()
            self.change_username_status()

    def send_message(self):
        text = self.write_message.text()
        message = f"{text}"
        self.send_message_signal.emit(message)
        self.write_message.setText('')
        if text.endswith('close') or text.endswith('exit'):
            print('closing threads and sockets by send_message func')
            # self.client_communicator.client_socket.close()
            self.client_communicator.send_message_socket.close()
            self.client_thread.join()

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
            if len(self.all_messages) < 6:
                self.all_messages.append(message)
                self.labels['msg'].setText('\n'.join(self.all_messages))
            else:
                self.all_messages.pop(0)
                self.all_messages.append(message)
                self.labels['msg'].setText('\n'.join(self.all_messages))

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
        self.labels['msg'] = QLabel('MESSAGES:', self)
        self.labels['msg'].setStyleSheet(login_label)
        self.labels['msg'].setStyleSheet(login_label_ok)
        self.labels['msg'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['msg'].repaint()

        # Write a message
        # self.write_message = QLineEdit(self)
        # self.write_message.setStyleSheet(login_label)
        self.write_message = QLineEdit(self)
        self.write_message.setStyleSheet(InputFieldStyle)
        self.write_message.setFixedSize(550, 60)
        self.write_message.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.write_message.repaint()
        self.all_messages = []
        for _ in range(5):
            self.all_messages.append('')
        self.labels['msg'].setText('\n'.join(self.all_messages))

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.labels['username'])
        self.labels['username'].setScaledContents(True)

        # second
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.write_message)

        # # Third Horizontal Layout
        # hbox3 = QHBoxLayout()
        # hbox3.addStretch(1)
        # hbox3.addWidget(self.labels['msg'])
        # self.labels['msg'].setScaledContents(True)
        # hbox3.addStretch(1)

        # Third Horizontal Layout
        hbox3 = QVBoxLayout()
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
