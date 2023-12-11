import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap
from typing import Tuple
import requests
from Login.login import login


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Upload Image')

        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 380, 200)

        self.load_button = QPushButton('Upload', self)
        self.load_button.setGeometry(10, 220, 120, 30)
        self.load_button.clicked.connect(self.load_image)
        self.retrieve_image_get('admin', 'admin')

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open image', '', 'Images (*.png *.jpg *.jpeg)')

        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
            self.upload_image_post('admin', 'admin', file_path)

    def retrieve_image_get(self, user: str, password: str) -> Tuple[bool, str]:
        status_login = login(user, password)
        jwt_token = status_login[1]
        print('jwt_token: ', jwt_token)
        url = 'http://localhost:8000/user/profilePIC/'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {str(jwt_token)}'
        }
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            with open("images/profile_image.png", "wb") as f:
                f.write(response.content)
                pixmap = QPixmap('images/profile_image.png')
                self.image_label.setPixmap(pixmap)
                self.image_label.setScaledContents(True)

            return True, response.text
        return False, response.text

    def upload_image_post(self, user: str, password: str, image_path) -> Tuple[bool, str]:
        status_login = login(user, password)
        jwt_token = status_login[1]
        print('jwt_token: ', jwt_token)
        print(image_path)
        url = 'http://localhost:8000/user/profilePIC/upload'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {str(jwt_token)}'
        }
        data = {
            'file': open(image_path, 'rb')
        }

        response = requests.post(url, headers=headers, files=data)

        print(response)
