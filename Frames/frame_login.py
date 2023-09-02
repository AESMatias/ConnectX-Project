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
from PyQt6.QtCore import QTimer
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
        self.labels['username'].repaint()

        # Logout
        self.logout_button = Login_Button(
            'logoutnButton', (300, 250), 'Close session', self)
        self.logout_button.setStyleSheet(
            button_style)
        self.logout_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        # self.logout_button.clicked.connect(self.change_username_status)

        self.labels['username_status'] = QLabel('', self)
        self.labels['username_status'].setStyleSheet(login_label)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['username_status'].repaint()
        # Image Input
        # self.labels['image_input'] = QPushButton('Upload image', self)
        # self.labels['image_input'].setStyleSheet(login_label)
        # self.labels['image_input'].setText('IMAGE INPUT')
        # self.labels['image_input'].setStyleSheet(login_label_ok)
        # self.labels['image_input'].repaint()  # To avoid bugs
        # self.labels['image_input'].clicked.connect(self.load_image)

    def load_image(self):
        print('UPLOADING IMAGEEE')

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
        vbox.addStretch(3)
        vbox.addWidget(self.labels['username_status'])
        # vbox.addWidget(self.labels['image_input'])
        vbox.addStretch(5)
        self.setLayout(vbox)
        # self.show()

    # def load_image(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.ReadOnly
    #     file_name, _ = QFileDialog.getOpenFileName(
    #         'Abrir Imagen', '', 'Imágenes (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)', options=options)

    #     if file_name:
    #         pixmap = QPixmap(file_name)
    #         image_label.setPixmap(pixmap)
    #         image_label.setScaledContents(True)
