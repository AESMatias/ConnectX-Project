from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QHBoxLayout
from PIL import Image
import numpy as np
from PyQt6.QtGui import QPainter, QColor
from components.friends_endpoints import accept_friend_request, reject_friend_request


class PendientFriend(QWidget):
    signal_add_friend = QtCore.pyqtSignal(str)
    signal_send_message = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, username=None, app_username=None, is_pendient=None,
                 is_accepted=None, is_rejected=None, token=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.username = username
        self.token = token
        self.app_username = app_username
        self.is_rejected = is_rejected
        self.is_accepted = is_accepted
        self.is_pendient = is_pendient
        self.setWindowTitle("Pending Friend QWidget")
        self.profile_image = QPixmap(f'profiles/images/{self.username}.png')
        # This is the average color of the image
        image_array = self.load_image(f'profiles/images/{self.username}.png')
        average_color = self.get_average_color(image_array)
        # Makes the background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.username_label = QLabel(self.username)
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_label.setStyleSheet(
            'color: white;text-align: center;font: 75 20pt "MS Shell Dlg 2";')
        self.accept_friend = QPushButton("Accept")
        # self.accept_friend.setStyleSheet(f'QPushButton {{ \
        #     background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
        #     stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
        #     stop:1 rgba({average_color[0]}, {average_color[1]}, {average_color[2]}, 1)); \
        #     color: white; font: bold 10pt "MS Shell Dlg 2";border:1px solid black;border-radius:2px;}} \
        #     QPushButton:pressed {{color: rgb(0, 0, 0); background-color: white;}}')
        self.accept_friend.setStyleSheet(f'QPushButton {{background: green; \
            color: white; font: bold 10pt "MS Shell Dlg 2";border:1px solid black;border-radius:2px;}} \
            QPushButton:pressed {{color: rgb(0, 0, 0); background-color: white;}}')
        # self.accept_friend.setStyleSheet(
        #     'QPushButton {color: white; background-color: rgba(0, 0, 128, 1);\
        #         solid black; font: bold 10pt "MS Shell Dlg 2";} \
        #     QPushButton:pressed {color: rgb(0, 0, 128); background-color: white;}')
        self.accept_friend.setCursor(Qt.CursorShape.PointingHandCursor)
        self.reject_friend = QPushButton("Reject")
        self.reject_friend.clicked.connect(self.send_message_to)
        self.reject_friend.setCursor(Qt.CursorShape.PointingHandCursor)
        self.reject_friend.setStyleSheet(f'QPushButton {{background: rgba(200,10,10,1); \
            color: white; font: bold 10pt "MS Shell Dlg 2";border:1px solid black;border-radius:2px;}} \
            QPushButton:pressed {{color: rgb(0, 0, 0); background-color: white;}}')
        # self.reject.setStyleSheet(f'QPushButton {{ \
        #     background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
        #     stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
        #     stop:1 rgba({average_color[0]}, {average_color[1]}, {average_color[2]}, 1)); \
        #     color: white; font: bold 10pt "MS Shell Dlg 2"; border:1px solid black;border-radius:2px;}} \
        #     QPushButton:pressed {{color: rgb(0, 0, 128); background-color: white;}}')
        self.reject_friend.setFixedHeight(25)
        self.accept_friend.setFixedHeight(25)
        # Create a container widget for the layout
        container_widget = QWidget(self)
        container_widget.setGeometry(0, 0, 250, 280)

        container_widget.setStyleSheet(
            f'background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
                stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
                    stop:1 rgba({average_color[0]+20}, {average_color[1]+20}, {average_color[2]+20}, 1)); \
    border: 1px solid white; border-radius: 2px;')

        # We make the layout
        layout = QVBoxLayout(container_widget)
        image_profile = QLabel('')
        # Quality: (0 means no compression, 100 is the best quality)
        scaled_image = self.profile_image.scaledToHeight(
            250, QtCore.Qt.TransformationMode.SmoothTransformation)

        image_profile.setPixmap(scaled_image)
        image_profile.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_profile)
        layout.addWidget(self.username_label)
        # Horizontal box for add friend and send message buttons
        horizontal_box = QHBoxLayout()
        horizontal_box.addWidget(self.accept_friend)
        horizontal_box.addWidget(self.reject_friend)
        layout.addLayout(horizontal_box)
        self.setLayout(layout)
        self.setFixedWidth(250)
        self.setFixedHeight(280)
        self.accept_friend.clicked.connect(self.accept_friend_function)
        self.reject_friend.clicked.connect(self.reject_friend_function)
        self.change_status()

    # def send_post_request(self, request: str):
    #     '''This method is called when the user clicks on the accept or reject button'''
    #     if is_accepted == True:
    #         self.accept_friend_function()
    #     elif is_rejected == True:
    #         self.reject_friend_function()
    #     elif is_pendient == True:
    #         pass

    def change_status(self):
        '''When the instance is created, we check the status of the friend request.
        If it is accepted, rejected o pendient, we change the buttons accordingly'''
        if self.is_accepted == True:
            self.accept_friend_function(self.token, self.username)
        elif self.is_rejected == True:
            self.reject_friend_function(self.token, self.username)
        elif self.is_pendient == True:
            pass

    def accept_friend_function(self):
        self.reject_friend.hide()
        self.accept_friend.setFixedWidth(230)
        self.accept_friend.setText('Accepted')
        self.accept_friend.setStyleSheet(f'QPushButton {{background: rgba(10,200,10,1); \
            color: white; font: bold 10pt "MS Shell Dlg 2";border:1px solid black;border-radius:2px;}} \
            QPushButton:pressed {{color: rgb(0, 0, 0); background-color: white;}}')
        # If the user accepts the friend request, we send a post request to the server
        if self.is_accepted == 'False':
            accept_friend_request(token=self.token, to_username=self.username)
            self.is_accepted = 'True'

    def reject_friend_function(self):
        self.accept_friend.hide()
        self.reject_friend.setFixedWidth(230)
        self.reject_friend.setText('Rejected')
        self.reject_friend.setStyleSheet(f'QPushButton {{background: rgba(250,10,10,1); \
            color: white; font: bold 10pt "MS Shell Dlg 2";border:1px solid black;border-radius:2px;}} \
            QPushButton:pressed {{color: rgb(0, 0, 0); background-color: white;}}')
        # If the user rejects the friend request, we send a post request to the server
        if self.is_rejected == 'False':
            reject_friend_request(token=self.token, to_username=self.username)
            self.is_rejected = 'True'

    def change_pixmap(self, username: str):
        path_username = f'profiles/images/{username}.png'
        self.profile_image = QPixmap(path_username)
        self.update()
        print('CHANGING PIXMAP AT ChatWidget.change_pixmap method!')

    def send_signal_add_friend(self):
        self.signal_add_friend.emit(self.username)

    def send_message_to(self):
        self.signal_send_message.emit(self.username)

    def load_image(self, image_path):
        # TODO We need to check if the image exists and retrieve it from the cache
        # if the image does not exist, we return a default image
        try:
            image = Image.open(image_path)
            return np.array(image)
        except:
            return np.array(Image.open('images/profile_image.png'))

    def get_average_color(self, image_array):
        average_color = np.mean(image_array, axis=(0, 1)).astype(int)
        return average_color
