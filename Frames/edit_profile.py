from time import sleep
import sys
import os
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QFileDialog, QStackedLayout, QStackedWidget,
                             QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Upload_file, Register_Button, Login_Button, InputField
from styles.styles import InputFieldStyle, tag, button_style, global_style, login_label, login_label_wrong, login_label_ok
from PyQt6.QtCore import QTimer, QStandardPaths

image_florence = 'images/florence.jpg'
aristotle_1 = 'images/aristotle_1.jpg'


class EditProfile(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.init_gui()

    def init_gui(self) -> None:
        window_size = self.size()
        # Window Geometry
        self.labels = {}
        self.setGeometry(100, 200, 1000, 800)
        self.setWindowTitle(f'ConectX Project - {self.username}')

        # 1 Button
        self.logout_button = Login_Button(
            'logoutnButton', (300, 250), 'Oneee', self)
        self.logout_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button.setStyleSheet(
            button_style)
        # 1 Layout
        # QLabel image assignation
        self.labels['label_image1'] = QLabel(self)
        self.labels['label_image1'].setMaximumSize(window_size)
        self.labels['label_image1'].setGeometry(50, 50, 300, 300)
        self.labels['label_image1'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = image_florence
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image1'].setPixmap(image_pixmap)
        self.labels['label_image1'].setScaledContents(True)
        self.labels['label_image1'].setGeometry(200, 200, 300, 300)
        self.labels['label_image1'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image1'].show()
        # 2 Button
        self.logout_button2 = Login_Button(
            'logoutnButton', (300, 250), 'Twooo', self)
        self.logout_button2.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button2.setStyleSheet(
            button_style)
        # 2 Layout
        # QLabel image assignation
        self.labels['label_image2'] = QLabel(self)
        self.labels['label_image2'].setMaximumSize(window_size)
        self.labels['label_image2'].setGeometry(50, 50, 300, 300)
        self.labels['label_image2'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = aristotle_1
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image2'].setPixmap(image_pixmap)
        self.labels['label_image2'].setScaledContents(True)
        self.labels['label_image2'].setGeometry(200, 200, 300, 300)
        self.labels['label_image2'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image2'].show()
        # 3 Button
        self.logout_button3 = Login_Button(
            'logoutnButton', (300, 250), 'Threee', self)
        self.logout_button3.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button3.setStyleSheet(
            button_style)
        # 3 Layout
        # QLabel image assignation
        self.labels['label_image3'] = QLabel(self)
        self.labels['label_image3'].setMaximumSize(window_size)
        self.labels['label_image3'].setGeometry(50, 50, 300, 300)
        self.labels['label_image3'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = image_florence
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image3'].setPixmap(image_pixmap)
        self.labels['label_image3'].setScaledContents(True)
        self.labels['label_image3'].setGeometry(200, 200, 300, 300)
        self.labels['label_image3'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image3'].show()
        # 4 Button
        self.logout_button4 = Login_Button(
            'logoutnButton', (300, 250), 'Fourrr', self)
        self.logout_button4.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button4.setStyleSheet(
            button_style)
        # 4 Layout
        # QLabel image assignation
        self.labels['label_image4'] = QLabel(self)
        self.labels['label_image4'].setMaximumSize(window_size)
        self.labels['label_image4'].setGeometry(50, 50, 300, 300)
        self.labels['label_image4'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = aristotle_1
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image4'].setPixmap(image_pixmap)
        self.labels['label_image4'].setScaledContents(True)
        self.labels['label_image4'].setGeometry(200, 200, 300, 300)
        self.labels['label_image4'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image4'].show()
        # 5 Button
        self.logout_button5 = Login_Button(
            'logoutnButton', (300, 250), 'Fiveee', self)
        self.logout_button5.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.logout_button5.setStyleSheet(
            button_style)
        # 5 Layout
        # QLabel image assignation
        self.labels['label_image5'] = QLabel(self)
        self.labels['label_image5'].setMaximumSize(window_size)
        self.labels['label_image5'].setGeometry(50, 50, 300, 300)
        self.labels['label_image5'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = image_florence
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image5'].setPixmap(image_pixmap)
        self.labels['label_image5'].setScaledContents(True)
        self.labels['label_image5'].setGeometry(200, 200, 300, 300)
        self.labels['label_image5'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image5'].show()

        # Buttons Grouped
        buttons_grouped = QHBoxLayout()
        buttons_grouped.addWidget(self.logout_button)
        buttons_grouped.addWidget(self.logout_button2)
        buttons_grouped.addWidget(self.logout_button3)
        buttons_grouped.addWidget(self.logout_button4)
        buttons_grouped.addWidget(self.logout_button5)

        page1_layout = QVBoxLayout()
        page1_layout.addWidget(self.labels['label_image1'])
        container1 = QWidget()
        container1.setLayout(page1_layout)

        page2_layout = QVBoxLayout()
        page2_layout.addWidget(self.labels['label_image2'])
        container2 = QWidget()
        container2.setLayout(page2_layout)

        page3_layout = QVBoxLayout()
        page3_layout.addWidget(self.labels['label_image3'])
        container3 = QWidget()
        container3.setLayout(page3_layout)

        page4_layout = QVBoxLayout()
        page4_layout.addWidget(self.labels['label_image4'])
        container4 = QWidget()
        container4.setLayout(page4_layout)

        page5_layout = QVBoxLayout()
        page5_layout.addWidget(self.labels['label_image5'])
        container5 = QWidget()
        container5.setLayout(page5_layout)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container1)
        self.stacked_layout.addWidget(container2)
        self.stacked_layout.addWidget(container3)
        self.stacked_layout.addWidget(container4)
        self.stacked_layout.addWidget(container5)

        main_layout = QVBoxLayout()
        main_layout.addLayout(buttons_grouped)
        main_layout.addLayout(self.stacked_layout)
        self.setLayout(main_layout)
