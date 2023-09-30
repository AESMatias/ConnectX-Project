import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Visor de Imágenes')

        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 380, 200)

        self.load_button = QPushButton('Cargar Imagen', self)
        self.load_button.setGeometry(10, 220, 120, 30)
        self.load_button.clicked.connect(self.load_image)

    def load_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Open image', '', 'Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)', options=options)

        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
