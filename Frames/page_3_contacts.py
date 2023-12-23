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


class PageContactsLayout(QHBoxLayout):
    def __init__(self, parent=None, username=None):
        super().__init__()
        self.username = username
        self.qlabel_to = QLabel("Here's your configuration file:")
        self.qlabel_to.setFixedHeight(30)
        self.qlabel_to.setStyleSheet(
            'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 0px solid rgba(255,255,255,0);\
                border-radius: 4px;')
        self.qlabel_to.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.addWidget(self.qlabel_to)
        self.button_to_change_color = QPushButton('Change Color')
        self.button_to_change_color.setStyleSheet(
            'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 1px solid rgba(255,255,255,1)')

        self.addWidget(self.button_to_change_color)
        self.button_to_change_font = QPushButton('Change Font')
        self.button_to_change_font.setStyleSheet(
            'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 1px solid rgba(255,255,255,1)')

        self.addWidget(self.button_to_change_font)
        self.button_to_change_font_size = QPushButton('Change Font Size')
        self.button_to_change_font_size.setStyleSheet(
            'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 1px solid rgba(255,255,255,1)')
        self.addWidget(self.button_to_change_font_size)

        self.button_to_change_background = QPushButton('Change Background')
        self.button_to_change_background.setStyleSheet(
            'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 1px solid rgba(255,255,255,1)')
        self.addWidget(self.button_to_change_background)
