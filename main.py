import sys
import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QFileDialog,
                             QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Button, Register_Button
from components.form_field import Form
from styles.styles import button_style, global_style
image_florence = 'florence.jpg'
aristotle_1 = 'aristotle_1.jpg'


class Frame(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        # Window Geometry
        self.setGeometry(200, 100, 800, 800)
        self.setWindowTitle('ConectX Project')
        # Grid Layout
        self.grid = QGridLayout()
        # Labels
        self.labels = {}
        self.labels['label1'] = QLabel('Your username:', self)
        self.labels['label1'].move(10, 15)
        self.labels['label2'] = QLabel('Answer:', self)
        self.labels['label2'].move(10, 50)

        self.edit1 = QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        # Buttons
        self.button1 = QPushButton('&Send', self)
        self.button1.resize(self.button1.sizeHint())
        self.button1.move(5, 70)
        # 1
        self.button2 = Button('nameButton', (50, 40), '&Enter', self)
        self.register_button = Register_Button(
            'registerButton', (300, 250), 'REGISTER', self)
        self.register_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.register_button.setStyleSheet(button_style)
        # register_clicked = self.register_button.button_clicked()
        # Text
        self.text_to_edit = QLineEdit('Edit this!', self)
        self.text_to_edit.setGeometry(50, 50, 100, 40)
        # Florence mage
        # self.image_florence = QLabel(self)
        # self.image_florence.setGeometry(350, 400, 400, 400)
        # image_florence_path = os.path.join('images', 'florence.jpg')
        # pixels_flocence = QPixmap(image_florence_path)
        # self.image_florence.setPixmap(pixels_flocence)
        # self.image_florence.setScaledContents(True)
        # Aristotle Image
        # self.image_aristotle1 = QLabel(self)
        # self.image_aristotle1.setGeometry(100, 500, 150, 150)
        # image_aristotle1 = os.path.join('images', 'aristotle_1.jpg')
        # pixels_aristotle1 = QPixmap(image_aristotle1)
        # self.image_aristotle1.setPixmap(pixels_aristotle1)
        # self.image_aristotle1.setScaledContents(True)
        # self.image_aristotle1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Horizontal Layout
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.labels['label1'])
        hbox.addWidget(self.edit1)
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.labels['label2'])
        hbox.addStretch(1)

        # Vertical Layout
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(8)
        self.setLayout(vbox)

        self.show()
#


if __name__ == '__main__':

    # Debug function
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication(sys.argv)

    window = Frame()
    window.setStyleSheet(global_style)
    window.show()

    # window2 = Frame()
    # window2.setStyleSheet(global_style)
    # window2.show()

    sys.exit(app.exec())
