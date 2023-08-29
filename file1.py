import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap
image_florence = 'florence.jpg'
aristotle_1 = 'aristotle_1.jpg'


class Window(QWidget):
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

        self.boton1 = QPushButton('&Send', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(5, 70)
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
        self.image_aristotle1 = QLabel(self)
        self.image_aristotle1.setGeometry(100, 500, 150, 150)
        image_aristotle1 = os.path.join('images', 'aristotle_1.jpg')
        pixels_aristotle1 = QPixmap(image_aristotle1)
        self.image_aristotle1.setPixmap(pixels_aristotle1)
        self.image_aristotle1.setScaledContents(True)

        # Horizontal Layout
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.labels['label1'])
        hbox.addWidget(self.edit1)
        hbox.addWidget(self.boton1)
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
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
