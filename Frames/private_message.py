from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QHBoxLayout
from PIL import Image
import numpy as np
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QFrame
# QGuiApplication
from PyQt6.QtGui import QGuiApplication
import requests
from PyQt6.QtWidgets import QLineEdit, QTextEdit


class PrivateMessageFrame(QWidget):
    signal_send_message_offline = QtCore.pyqtSignal()
    signal_message_content = QtCore.pyqtSignal(str, str, str)

    def __init__(self, parent=None, username=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.username = username
        self.setWindowTitle("Private Message")
        self.profile_image = QPixmap(f'profiles/images/{self.username}.png')
        self.setGeometry(0, 0, 400, 600)
        self.button_close = QLabel(self)
        self.button_close.setFixedHeight(64)
        self.button_close.setFixedWidth(64)
        self.button_close.setPixmap(QPixmap('images/cancel64.png'))
        self.button_close.setCursor(Qt.CursorShape.PointingHandCursor)
        # button_close hbox
        self.button_close_hbox = QHBoxLayout()
        self.button_close_hbox.addWidget(self.button_close)
        self.button_close_hbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        # button qlabel clicked, netonceshacemos .hide
        self.button_close.mousePressEvent = self.hide_by_button_pressed
        self.setStyleSheet('background-color: rgba(39, 54, 82, 1);')
        self.hide()
        # tomamos las dimensiones ancho y largo del monitor
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        # Monitor dimensions
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()

        # Un lugar para poder escribir el destinatario, y otro mas grande para el mensaje:
        self.qlabel_to = QLabel('To:', self)
        self.qlabel_to.setFixedHeight(30)
        self.qlabel_to.setStyleSheet(
            'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 0px solid rgba(255,255,255,0);\
                border-radius: 4px;')
        self.qlabel_to.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qlabel_to_write = QLineEdit(self)
        self.qlabel_to_write.setFixedHeight(30)
        self.qlabel_to_write.setStyleSheet(
            'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 1px solid rgba(255,255,255,1)')
        self.qlabel_to_write.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.to_hbox = QHBoxLayout()
        self.to_hbox.addWidget(self.qlabel_to)
        self.to_hbox.addWidget(self.qlabel_to_write)
        #
        self.username_label = QTextEdit(self.username)
        self.username_label.setFixedHeight(300)
        self.username_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.username_label.setFixedHeight(350)
        self.username_label.setFixedWidth(500)

        self.username_label.setStyleSheet(
            'color: white;text-align: center;font: 75 12pt "MS Shell Dlg 2"; border: 2px solid rgba(255,255,255,1);\
                border-radius: 8px;')
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # Button to send the message
        self.send_message = QPushButton("Send Message", self)
        self.send_message.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_message.setStyleSheet(
            'QPushButton {color: white; background-color: rgba(0, 0, 128, 1);\
                solid black; font: bold 28pt "MS Shell Dlg 2";} \
            QPushButton:pressed {color: rgb(0, 0, 128); background-color: white;}')
        self.send_message.clicked.connect(self.send_message_func)

        self.vertical_container = QVBoxLayout(self)
        self.vertical_container.addLayout(self.button_close_hbox)
        self.vertical_container.addLayout(self.to_hbox)
        self.vertical_container.addWidget(self.username_label)
        self.vertical_container.addWidget(self.send_message)
        # Stablish the tabulation order
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.setTabOrder(self.qlabel_to_write, self.username_label)
        self.setTabOrder(self.username_label, self.send_message)

    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        if event.key() == Qt.Key.Key_Escape:
            # TODO: Make an animation to hide and open the window
            self.hide()

    def emit_signal_send_message_offline(self):
        self.signal_send_message_offline.emit()

    def send_message_func(self, from_username=None, message_text=None, to_username=None):
        to_username = self.qlabel_to_write.text().strip()
        message_text = self.username_label.toPlainText().strip()
        # if the username contains a space, we take only the first word
        if to_username.__contains__(' '):
            to_username = to_username.split(' ')
            to_username = to_username[0]

        from_username = str(self.username)
        "TODO: we need to validate the token when we send a message"
        url = "http://localhost:8000/messages/p2p/message"
        params = {
            'username': from_username,
            'message_text': message_text,
            'username2': to_username
        }
        try:
            response = requests.post(url, params=params)
            if response.status_code == 200:
                print("Mensaje enviado con éxito")
                print('Mensaje del usuario', from_username)
                print('Mensaje para el usuario', to_username)
                print('Mensaje:', message_text)
                self.qlabel_to_write.setText('')
                self.username_label.setText('')
                self.hide()
                # TODO put a qlabel message that indicates that the message was sent or not
            else:
                print(
                    f"Error al enviar el mensaje. Código de estado: {response.status_code}")
                print(response.text)
        except requests.RequestException as e:
            print(f"Error de conexión: {e}")

    def hide_by_button_pressed(self, event):
        self.close()

    def show_function(self):
        print(self.username, self.profile_image)
        self.setGeometry(0, 0, 500, 600)
        self.move(int(self.screen_width)-int(self.width()*2.5),
                  int(self.screen_height*0.2))
        self.show()
        self.raise_()
        self.setFocus()
