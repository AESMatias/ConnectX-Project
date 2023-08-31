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


class FrameLogin(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.init_gui()

    def launch(self):
        sender = self.sender()
        if sender.login_status == True:
            print('Session initiated')
            print('logoutbutton username:', self.logout_button.username)
            self.show()

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
        self.labels['username'] = QLabel(f'Welcome {self.username}', self)
        self.labels['username'].setStyleSheet(tag)
        self.labels['username'].setFixedSize(200, 40)
        self.labels['username'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # Logout
        self.logout_button = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button.setStyleSheet(
            button_style)
        self.logout_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button.clicked.connect(self.change_username_status)

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
        hbox1.addStretch(1)
        # Second Horizontal Layout
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        # hbox2.addWidget(self.login_button)
        hbox2.addStretch(1)
        # Third Horizontal Layout
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        # hbox3.addWidget(self.register_button)
        hbox3.addStretch(1)
        # Vertical Layout
        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(5)
        self.setLayout(vbox)
        # self.show()
