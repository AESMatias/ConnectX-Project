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
from PyQt6.QtWidgets import QGridLayout
import requests
from PyQt6.QtWidgets import QLineEdit, QTextEdit
from styles.styles import login_label_ok
from components.friends_endpoints import get_pendient_friends, get_friend_list
from components.req_friend_label import PendientFriend


class PageContactsLayout(QVBoxLayout):
    def __init__(self, parent=None, username=None, token=None):
        super().__init__()
        self.jwt = token
        self.username = username
        self.qlabel_to = QLabel("Friend requests")
        self.qlabel_to.setFixedHeight(30)
        self.qlabel_to.setStyleSheet(login_label_ok)
        self.qlabel_to.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.addWidget(self.qlabel_to)

    def get_token(self, token: str):
        '''We start the GUI only when the token is passed by this function'''
        self.jwt = token
        self.init_gui_request()

    def init_gui_request(self) -> None:
        self.hbox_buttons = QHBoxLayout()
        layout = QVBoxLayout()

        data: list = get_pendient_friends(self, self.jwt)
        self.list_of_users_pending: list = []
        # We create a new object just with the info we need
        for user_obj in data:
            map_user_obj: map = {}
            username = user_obj['username']
            is_accepted = user_obj['accepted']
            is_pendient = user_obj['pendient']
            is_rejected = user_obj['rejected']
            map_user_obj.update({'username': username})
            map_user_obj.update({'is_accepted': is_accepted})
            map_user_obj.update({'is_pendient': is_pendient})
            map_user_obj.update({'is_rejected': is_rejected})
            self.list_of_users_pending.append(map_user_obj)

        friends_grid_layout = QGridLayout()
        num_columns = 5

        # Add items to the grid layout dynamically
        for index, item in enumerate(self.list_of_users_pending):
            # Cast to string
            req_username = str(item['username'])
            is_pendient = str(item['is_pendient'])
            is_accepted = str(item['is_accepted'])
            is_rejected = str(item['is_rejected'])
            row = index // num_columns
            col = index % num_columns

            friend_req_label = PendientFriend(
                username=req_username, is_pendient=is_pendient, token=self.jwt,
                is_accepted=is_accepted, is_rejected=is_rejected)
            # friend_req_label.setStyleSheet(
            #     'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 0px solid rgba(255,255,255,0);\
            #         border-radius: 4px;')

            friends_grid_layout.addWidget(friend_req_label, row, col)

        layout.addLayout(friends_grid_layout)
        self.addLayout(layout)

    def init_gui_friends(self) -> None:
        self.hbox_buttons = QHBoxLayout()
        layout = QVBoxLayout()

        data: list = get_friend_list(self, self.jwt)
        self.list_of_users_pending: list = []
        # We create a new object just with the info we need
        for user_obj in data:
            map_user_obj: map = {}
            username = user_obj['username']
            is_accepted = user_obj['accepted']
            is_pendient = user_obj['pendient']
            is_rejected = user_obj['rejected']
            map_user_obj.update({'username': username})
            map_user_obj.update({'is_accepted': is_accepted})
            map_user_obj.update({'is_pendient': is_pendient})
            map_user_obj.update({'is_rejected': is_rejected})
            self.list_of_users_pending.append(map_user_obj)

        friends_grid_layout = QGridLayout()
        num_columns = 5

        # Add items to the grid layout dynamically
        for index, item in enumerate(self.list_of_users_pending):
            # Cast to string
            req_username = str(item['username'])
            is_pendient = str(item['is_pendient'])
            is_accepted = str(item['is_accepted'])
            is_rejected = str(item['is_rejected'])
            row = index // num_columns
            col = index % num_columns

            friend_req_label = PendientFriend(
                username=req_username, is_pendient=is_pendient, token=self.jwt,
                is_accepted=is_accepted, is_rejected=is_rejected)
            # friend_req_label.setStyleSheet(
            #     'color: white;text-align: center;font: 75 22pt "MS Shell Dlg 2"; border: 0px solid rgba(255,255,255,0);\
            #         border-radius: 4px;')

            friends_grid_layout.addWidget(friend_req_label, row, col)

        layout.addLayout(friends_grid_layout)
        self.addLayout(layout)
