from time import sleep
import sys
import os
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QFileDialog,
                             QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Register_Button, Login_Button, InputField
from styles.styles import InputFieldStyle, tag, button_style, global_style, login_label, login_label_wrong, login_label_ok
image_florence = 'florence.jpg'
aristotle_1 = 'aristotle_1.jpg'


class Frame1(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()

        # self.setMouseTracking(True)
    # def mouseMoveEvent(self, event):
    #     x = event.pos().x()
    #     y = event.pos().y()
    #     self.y_coord = event.pos().y()
    #     print(x, y)

    def mousePressEvent(self, event):
        x = event.position().x()
        y = event.position().y()
        print(f"Clicked at {x},{y}")

    def mouseReleaseEvent(self, event):
        x = event.position().x()
        y = event.position().y()
        print(f"Click released at {x},{y}")

    def keyPressEvent(self, event):
        print((f'Key: {event.text()} Code: {event.key()}'))
        # if event.text() == 'Q' or event.text() == 'q':
        #     print('A pressed')
        #     sys.exit()

    def change_username_status(self):
        sender = self.sender()
        if sender.login_status == False:
            self.labels['username_status'].setText('Invalid credentials')
            self.labels['username_status'].setStyleSheet(login_label_wrong)
            self.labels['username_status'].repaint()  # To avoid bugs
        elif sender.login_status == True:
            self.labels['username_status'].setText('Credentials OK')
            self.labels['username_status'].setStyleSheet(login_label_ok)
            self.labels['username_status'].repaint()  # To avoid bugs

    def init_gui(self) -> None:
        # Window Geometry
        self.setGeometry(100, 200, 1000, 800)
        self.setWindowTitle('ConectX Project')
        # Grid Layout
        self.grid = QGridLayout()
        # Labels
        self.labels = {}
        self.labels['username'] = QLabel('Your username:', self)
        self.labels['username'].setStyleSheet(tag)
        # self.labels['username'].move(10, 15)
        self.labels['password'] = QLabel('Password', self)
        self.labels['password'].setStyleSheet(tag)
        # self.labels['password'].move(10, 50)
        self.labels['username_status'] = QLabel('', self)
        self.labels['username_status'].setStyleSheet(login_label)

        self.username_field = InputField('username_field', '', self)
        self.username_field.setFixedSize(200, 40)
        self.username_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_field.setStyleSheet(InputFieldStyle)
        self.password_field = InputField('password_field', '', self)
        self.password_field.setFixedSize(200, 40)
        self.password_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_field.setStyleSheet(InputFieldStyle)
        # Register
        self.register_button = Register_Button(
            'registerButton', (300, 250), 'REGISTER', self)
        self.register_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.register_button.setStyleSheet(button_style)
        # Login
        # self.login_button = Login_Button(
        #     'loginButton', (300, 250), 'LOGIN', [1, 2], self)
        self.login_button = Login_Button(
            'loginButton', (300, 250), 'LOGIN', self)
        self.login_button.setStyleSheet(
            button_style)
        self.login_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_button.clicked.connect(self.change_username_status)

        # # Florence mage
        # self.image_florence = QLabel(self)
        # self.image_florence.setGeometry(350, 400, 100, 100)
        # image_florence_path = os.path.join('images', 'florence.jpg')
        # pixels_flocence = QPixmap(image_florence_path)
        # self.image_florence.setPixmap(pixels_flocence)
        # self.image_florence.setScaledContents(True)
        # self.image_florence.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # # Aristotle Image
        # self.image_aristotle1 = QLabel(self)
        # self.image_aristotle1.setGeometry(100, 500, 150, 150)
        # image_aristotle1 = os.path.join('images', 'aristotle_1.jpg')
        # pixels_aristotle1 = QPixmap(image_aristotle1)
        # self.image_aristotle1.setPixmap(pixels_aristotle1)
        # self.image_aristotle1.setScaledContents(True)
        # self.image_aristotle1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.labels['username'])
        hbox1.addWidget(self.username_field)
        hbox1.addWidget(self.labels['password'])
        hbox1.addWidget(self.password_field)
        hbox1.addStretch(1)
        # Second Horizontal Layout
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.login_button)
        hbox2.addStretch(1)
        # Third Horizontal Layout
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.register_button)
        hbox3.addStretch(1)
        # Vertical Layout
        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.labels['username_status'])

        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        vbox.addStretch(5)
        self.setLayout(vbox)
        self.show()
