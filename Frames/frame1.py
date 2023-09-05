from time import sleep
import sys
import os
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtGui import QIcon, QColor, QPalette
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QFileDialog,
                             QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Register_Button, Login_Button, InputField
from styles.styles import new_login_button, InputFieldStyle, tag, button_style, global_style, login_label, login_label_wrong, login_label_ok


class Frame1(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()

    def remove_registered_label(self):
        sender = self.sender()
        print(sender.name)
        print(sender)
        if sender.register_status == False and sender.name == 'logoutnButton':
            self.labels['registered_status'].setText(
                '')
            self.labels['registered_status'].setStyleSheet(login_label)
            self.labels['registered_status'].repaint()  # To avoid bugs

            self.labels['username_status'].setText('')
            self.labels['username_status'].setStyleSheet(login_label)
            self.labels['username_status'].repaint()  # To avoid bugs

        if sender.login_status == False and sender.name == 'loginButton':
            self.labels['username_status'].setText('Invalid credentials')
            self.labels['username_status'].setStyleSheet(login_label_wrong)
            self.labels['username_status'].repaint()  # To avoid bugs
            self.labels['registered_status'].setText('')
            self.labels['registered_status'].setStyleSheet(login_label)

    def change_username_status(self):
        sender = self.sender()
        if sender.login_status == False:
            self.labels['username_status'].setText('Invalid credentials')
            self.labels['username_status'].setStyleSheet(login_label_wrong)
            self.labels['username_status'].repaint()  # To avoid bugs
            self.labels['registered_status'].setText('')
            self.labels['registered_status'].setStyleSheet(login_label)
        elif sender.login_status == True:
            # self.labels['username_status'].setText('')
            # self.labels['username_status'].setStyleSheet(login_label)
            # self.labels['username_status'].repaint()  # To avoid bugs
            self.labels['registered_status'].setText(
                'You have been registered')
            self.labels['registered_status'].setStyleSheet(login_label_ok)
            self.labels['registered_status'].repaint()  # To avoid bugs

    def show_register_status(self):
        sender = self.sender()
        if sender.register_status == False:
            pass
        elif sender.register_status == True:
            # self.labels['username_status'].setText('')
            # self.labels['username_status'].setStyleSheet(login_label)
            # self.labels['username_status'].repaint()  # To avoid bugs
            self.labels['registered_status'].setText(
                'You have been registered')
            self.labels['registered_status'].setStyleSheet(login_label_ok)
            self.labels['registered_status'].repaint()  # To avoid bugs
            sender.register_status = False

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
        # registered status
        self.labels['registered_status'] = QLabel('', self)
        self.labels['registered_status'].setStyleSheet(login_label)
        self.labels['registered_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

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
        self.register_button.clicked.connect(
            self.register_button.button_clicked)
        # Login
        self.login_button = Login_Button(
            'loginButton', (300, 250), 'LOGIN', self)
        self.login_button.setStyleSheet(
            button_style)
        self.login_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_button.clicked.connect(self.change_username_status)

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
        vbox.addWidget(self.labels['registered_status'])

        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        vbox.addStretch(5)
        self.setLayout(vbox)
        self.show()
