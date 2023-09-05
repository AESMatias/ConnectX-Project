from time import sleep
import sys
import os
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QFileDialog,
                             QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Upload_file, Register_Button, Login_Button, InputField
from styles.styles import InputFieldStyle, tag, button_style, global_style, login_label, login_label_wrong, login_label_ok
from PyQt6.QtCore import QTimer, QStandardPaths
image_florence = 'florence.jpg'
aristotle_1 = 'aristotle_1.jpg'


class EditProfile(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.init_gui()

    def init_gui(self) -> None:
        # Window Geometry
        self.setGeometry(100, 200, 1000, 800)
        self.setWindowTitle(f'ConectX Project - {self.username}')
        # 1
        self.logout_button = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button.setStyleSheet(
            button_style)
        # 2
        self.logout_button2 = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button2.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button2.setStyleSheet(
            button_style)
        # 3
        self.logout_button3 = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button3.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button3.setStyleSheet(
            button_style)
        # 4
        self.logout_button4 = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button4.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button4.setStyleSheet(
            button_style)
        # 5
        self.logout_button5 = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button5.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button5.setStyleSheet(
            button_style)
        # self.logout_button.clicked.connect(self.change_username_status)

        # hbox4.addStretch(1)

        # Horizonatal Layout
        hbox_left1 = QHBoxLayout()
        hbox_left1.addWidget(self.logout_button)
        hbox_left1.addStretch(1)
        hbox_left2 = QHBoxLayout()
        hbox_left2.addWidget(self.logout_button2)
        hbox_left2.addStretch(1)
        hbox_left3 = QHBoxLayout()
        hbox_left3.addWidget(self.logout_button3)
        hbox_left3.addStretch(1)
        hbox_left4 = QHBoxLayout()
        hbox_left4.addWidget(self.logout_button4)
        hbox_left4.addStretch(1)
        hbox_left5 = QHBoxLayout()
        hbox_left5.addWidget(self.logout_button5)
        hbox_left4.addStretch(1)
        # Left menu
        vbox_left = QVBoxLayout()
        vbox_left.addLayout(hbox_left1)
        vbox_left.addLayout(hbox_left2)
        vbox_left.addLayout(hbox_left3)
        vbox_left.addLayout(hbox_left4)
        vbox_left.addLayout(hbox_left5)
        vbox_left.addStretch(20)
        # RIGHT
        vbox_right = QVBoxLayout()
        vbox_right.addStretch(20)
        hbox_principal = QHBoxLayout()
        hbox_principal.addStretch(20)
        hbox_principal.addLayout(vbox_right)
        hbox_principal.addLayout(vbox_left)
        self.setLayout(hbox_principal)
        # self.show()
