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
from components.chat_functions import QLabelProfilePicture
from PyQt6.QtCore import Qt


class ChatFrame(QWidget):
    send_message_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        qlabelpixamap = QLabel(self)
        qlabelpixamap.setPixmap(QPixmap('images/logo32.png'))
        self.image_pixmap_1 = qlabelpixamap
        self.image_pixmap_1.setVisible(False)
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
            self.labels['username_status'].repaint()  # To avoid bug
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

        qlabelpixamap = QLabelProfilePicture()
        qlabelpixamap.setPixmap(QPixmap(
            'images/cara_blue.jpg').scaled(
            32, 32, Qt.AspectRatioMode.KeepAspectRatio))
        qlabelpixamap.setContentsMargins(100, 100, 100, 100)
        qlabelpixamap.setStyleSheet(
            "QLabel { padding: 50px;}")
        qlabelpixamap.setCursor(Qt.CursorShape.PointingHandCursor)

        if message:

            if len(self.all_messages2) < 6:
                self.all_messages.append([self.image_pixmap_1, message])
                self.all_messages2.append(message)

                qlabel_message = QLabel(message, self)
                horizontal_layout = QHBoxLayout()

                image_pixmap_1 = qlabelpixamap
                qlabel_message.setWordWrap(True)

                horizontal_layout.addWidget(image_pixmap_1)
                horizontal_layout.addWidget(qlabel_message)
                self.messages_images_layout.addLayout(horizontal_layout)

            else:
                self.all_messages.pop(0)
                self.all_messages.append([self.image_pixmap_1, message])
                self.all_messages2.append(message)
                # self.labels['msg'].setText('\n'.join(self.all_messages2))

                # Label para el mensaje
                qlabel_message = QLabel(message, self)
                horizontal_layout = QHBoxLayout()

                image_pixmap_1 = qlabelpixamap
                qlabel_message.setWordWrap(True)

                horizontal_layout.addWidget(image_pixmap_1)
                horizontal_layout.addWidget(qlabel_message)
                self.messages_images_layout.addLayout(horizontal_layout)

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

        # # Message Label
        # self.labels['msg'] = QLabel('MESSAGES:', self)
        # self.labels['msg'].setStyleSheet(login_label)
        # self.labels['msg'].setStyleSheet(login_label_ok)
        # self.labels['msg'].setAlignment(
        #     QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.labels['msg'].repaint()

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

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.labels['username'])
        self.labels['username'].setScaledContents(True)

        # second
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.write_message)

        # Third Horizontal Layout
        hbox3 = QVBoxLayout()
        hbox3.addStretch(1)
        # hbox3.addWidget(self.labels['msg'])
        # self.labels['msg'].setScaledContents(True)
        hbox3.addStretch(1)

        # Vertical
        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(self.messages_images_layout)

        # vbox.addLayout(hbox3)

        vbox.addStretch(2)
        vbox.addWidget(self.labels['username_status'])
        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # vbox.addWidget(self.labels['image_input'])
        vbox.addStretch(5)
        self.setLayout(vbox)
