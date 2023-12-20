
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap
from typing import Tuple
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
import requests

from styles.styles import button_style_upload


class ImageViewer(QMainWindow):
    def __init__(self, username: str, jwt: str):
        super().__init__()
        self.username = username
        self.jwt = jwt
        self.initUI()

    def initUI(self):
        # self.setGeometry(0, 0, 0, 0)
        # self.setFixedWidth(400)
        # self.setFixedHeight(400)
        self.setWindowTitle('Change your profile picture')

        self.image_label = QLabel(self)
        self.image_label.setGeometry(400, 0, 400, 400)
        self.setStyleSheet(
            'background-color: rgba(0,0,0,0); border: 1px solid rgba(190,190,255,0.6)')
        self.image_label.setStyleSheet(
            'background-color: rgba(0,0,0,0); border: 20px solid rgba(255,255,255,0)')
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.load_button = QPushButton('Upload New Avatar', self)
        self.load_button.setGeometry(500, 450, 200, 60)
        self.load_button.setStyleSheet(button_style_upload)
        # hacemos efecto pointer cursosr
        self.load_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
    #     self.load_button.clicked.connect(self.load_image)

    # def load_image(self):
    #     file_path, _ = QFileDialog.getOpenFileName(
    #         self, 'Set your new profile picture!', '', 'Images (*.png *.jpg *.jpeg)')

    #     if file_path:
    #         pixmap = QPixmap(file_path)
    #         self.image_label.setPixmap(pixmap)
    #         self.image_label.setScaledContents(True)
    #         print('ID of the EditProfile instance:', id(self))
    #         self.upload_image_post(self.username, self.jwt, file_path)
    #         print('post con username: ', self.username, ' y jwt: ', self.jwt)
    #         with open(f"profiles/images/{self.username}.png", "wb") as f:
    #             f.write(open(file_path, 'rb').read())

    def retrieve_image_get(self, user: str, jwt: str) -> Tuple[bool, str]:
        # status_login = login(user, password)
        # jwt_token = status_login[1]
        # print('jwt_token: ', jwt_token)

        url = 'http://localhost:8000/user/profilePIC/'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {str(self.jwt)}'
        }
        response = requests.get(url, headers=headers)

        # TODO> If the image exists, then we don't need to download it
        if response.status_code == 200:
            with open("images/profile_image.png", "wb") as f:
                f.write(response.content)
                pixmap = QPixmap(f'profiles/images/{user}.png').scaled(
                    400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.image_label.setPixmap(pixmap)
                self.image_label.repaint()
                self.image_label.show()

            return True, response.text
        elif response.status_code == 404:  # Which means, not found
            # If the user doesn't have a profile picture, then we set the default one
            with open("images/profile_image.png", "wb") as f:
                f.write(open('profiles/images/Anonymous.png', 'rb').read())
                pixmap = QPixmap('profiles/images/Anonymous.png').scaled(
                    350, 350, Qt.AspectRatioMode.KeepAspectRatio)
                self.image_label.setPixmap(pixmap)
                self.image_label.repaint()
                self.image_label.show()
# Then, we write the image inside the profiles/images folder so we can retrieve it in the chat
            with open(f"profiles/images/{self.username}.png", "wb") as f:
                f.write(open('profiles/images/Anonymous.png', 'rb').read())
                # return False, response.text

    def upload_image_post(self, username: str, jwt: str, image_path) -> Tuple[bool, str]:
        url = f'http://localhost:8000/user/profilePIC/upload'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {str(jwt)}'
        }
        data = {
            'file': open(image_path, 'rb')
        }

        response = requests.post(url, headers=headers, files=data)
        if response.status_code == 200:
            pixmap = QPixmap(image_path).scaled(
                350, 350, Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
            # recargamos para que se vea
            self.image_label.repaint()
            self.image_label.show()

        else:
            print('Error uploading the image')
            self.hide()
