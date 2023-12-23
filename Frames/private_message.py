from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
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

    def send_message_func(from_username=None, message_text=None, to_username=None):
        "TODO we need to validate the token when we send a message"
        url = "http://localhost:8000/messages/p2p/message"
        username1 = str('nuevoo')
        username2 = str('nuevoo')
        message_text = str('message')
        params = {
            'username': username1,
            'message_text': message_text,
            'username2': username2
        }

        try:
            response = requests.post(url, params=params)
            if response.status_code == 200:
                print("Mensaje enviado con éxito")
            else:
                print(
                    f"Error al enviar el mensaje. Código de estado: {response.status_code}")
                print(response.text)
        except requests.RequestException as e:
            print(f"Error de conexión: {e}")

    def hide_by_button_pressed(self, event):
        # self.hide()
        self.close()

    def show_profile(self):
        print(self.username, self.profile_image)
        self.setGeometry(0, 0, 500, 600)
        self.move(int(self.screen_width)-int(self.width()*2.5),
                  int(self.screen_height*0.2))
        self.show()
        self.raise_()
        self.setFocus()
    # si la ventana pierde el foco, se hace hide

    # def focusOutEvent(self, event):
    #     self.hide()
    #     print('focusOutEvent')
