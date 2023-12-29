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
from styles.styles import login_label_ok, button_style_contacts
from components.friends_endpoints import get_pendient_friends, get_friend_list
from components.req_friend_label import PendientFriend, MyFriend
from components.scrolled_friends import ScolledFriends
from PyQt6.QtWidgets import QStackedLayout


class StackContacts(QVBoxLayout):
    def __init__(self, parent=None, username=None, token=None):
        super().__init__()
        # Qlabel
        self.qlabel_to = QLabel("My Contacts and Requests")
        self.qlabel_to.setFixedHeight(30)
        self.qlabel_to.setStyleSheet(login_label_ok)
        self.qlabel_to.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.addWidget(self.qlabel_to)
        # buttons
        self.buttons_grouped = QHBoxLayout()
        self.btn_my_friends = QPushButton("My friends")
        self.btn_my_friends.clicked.connect(
            lambda: self.change_page(optional_number=0))
        self.btn_my_friends.setStyleSheet(button_style_contacts)
        self.btn_my_friends.setFixedHeight(50)
        self.btn_my_friends.setFixedWidth(200)
        self.btn_pendient = QPushButton("Pendient requests")
        self.btn_pendient.clicked.connect(
            lambda: self.change_page(optional_number=1))
        self.btn_pendient.setStyleSheet(button_style_contacts)
        self.btn_pendient.setFixedHeight(50)
        self.btn_pendient.setFixedWidth(200)
        self.buttons_grouped.addWidget(self.btn_my_friends)
        self.buttons_grouped.addWidget(self.btn_pendient)
        widget_of_buttons = QWidget()
        widget_of_buttons.setLayout(self.buttons_grouped)
        # Containers
        self.friends_instance = PageFriendsLayout(
            username=username, token=token)
        self.pendient_instance = PagePendientsLayout(
            username=username, token=token)
        container_friends = QWidget()
        container_friends.setLayout(self.friends_instance)
        container_pendient = QWidget()
        container_pendient.setLayout(self.pendient_instance)
        # Stacked Layout and buttons
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_friends)
        self.stacked_layout.addWidget(container_pendient)
        # self.stacked_layout.setCurrentIndex(0)
        main_layout = QVBoxLayout()
        main_layout.addWidget(widget_of_buttons)
        main_layout.addLayout(self.stacked_layout)
        self.addLayout(main_layout)

    def get_token_and_username(self, token: str, username: str):
        '''We start the GUI only when the token is passed by this function'''
        self.jwt = token
        self.username = username
        self.friends_instance.get_token_and_username(token, username)
        self.pendient_instance.get_token_and_username(token, username)
        # self.init_scrolled_area()
        # self.retrieve_data()
        # self.populate_gui()

    def change_page(self, optional_number=None):
        self.stacked_layout.setCurrentIndex(optional_number)
        print(optional_number, 'optional number')
        self.update()


class PagePendientsLayout(QVBoxLayout):
    def __init__(self, parent=None, username=None, token=None):
        super().__init__()
        self.jwt = token
        self.username = username
        self.pendient_friends_list: list = []

    def get_token_and_username(self, token: str, username: str):
        '''We start the GUI only when the token is passed by this function'''
        self.jwt = token
        self.username = username
        self.init_scrolled_area()
        self.retrieve_data()
        self.populate_gui()

    def refresh_page(self):
        # self.scrolled_friends.deleteLater()
        # self.init_scrolled_area()
        # self.retrieve_data()
        # self.populate_gui()
        print('refresh page pendient')
        pass

    def init_scrolled_area(self):
        self.scrolled_pendient: QWidget = ScolledFriends()
        self.addWidget(self.scrolled_pendient)

    def populate_friends(self, friends_list: list[str]):
        print('friends list', friends_list)
        friends_grid_layout = QGridLayout()
        num_columns = 4

        # Add items to the grid layout dynamically
        for index, item in enumerate(friends_list):
            req_username = str(item)
            row = index // num_columns
            col = index % num_columns
            friend_req_label = MyFriend(username=req_username, token=self.jwt)
            friends_grid_layout.addWidget(friend_req_label, row, col)
            self.scrolled_friends.new_label(friend_req_label, row, col)
        # layout.addLayout(friends_grid_layout)
        # self.scrolled_friends.new_label(layout)

    def populate_pendient(self, pendient_list: list[dict]):
        # self.hbox_buttons = QHBoxLayout()
        # layout = QVBoxLayout()
        pendient_grid_layout = QGridLayout()
        num_columns = 4

        # Add items to the grid layout dynamically
        for index, item in enumerate(pendient_list):
            # Cast to string
            req_username = str(item['username'])
            is_pendient = str(item['is_pendient'])
            is_accepted = str(item['is_accepted'])
            is_rejected = str(item['is_rejected'])
            row = index // num_columns
            col = index % num_columns

            pendient_friend_dict = {
                'username': req_username,
                'is_pendient': is_pendient,
                'is_accepted': is_accepted,
                'is_rejected': is_rejected
            }
            friend_req_label = PendientFriend(
                username=req_username, token=self.jwt, is_pendient=is_pendient,
                is_accepted=is_accepted, is_rejected=is_rejected)

            pendient_grid_layout.addWidget(friend_req_label, row, col)
            self.pendient_friends_list.append(pendient_friend_dict)
            self.scrolled_pendient.new_label(friend_req_label, row, col)
        # layout.addLayout(pendient_grid_layout)
        # self.addLayout(layout)

    def populate_gui(self):
        '''We populate the GUI with the data we get from the API only when the token is passed
        by the function get_token and after filtering the data to avoid repeated cases'''
        self.only_friends = [
            friend for friend in self.list_of_friends if friend not in self.list_of_users_pending
            and friend != self.username]
        pendient = [
            pendient for pendient in self.list_of_users_pending if pendient['username'] not in self.only_friends
            and pendient['username'] != self.username]
        print('11only friends', self.only_friends)
        print('11pendientt', pendient)
        self.populate_pendient(pendient)

    def retrieve_data(self) -> None:
        # TODO: Retrieving the friends
        data: list = get_friend_list(self, self.jwt)
        self.list_of_friends: list = []
        # We create a new object just with the info we need
        for user_obj in data:
            self.list_of_friends.append(user_obj)

        # TODO: Retrieving the pendient friends
        data: list = get_pendient_friends(self, self.jwt)
        self.list_of_users_pending: list = []
        # We create a new object just with the info we need
        print(' data', data)
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


class PageFriendsLayout(QVBoxLayout):
    def __init__(self, parent=None, username=None, token=None):
        super().__init__()
        self.jwt = token
        self.username = username

        self.pendient_friends_list: list = []

    def get_token_and_username(self, token: str, username: str):
        '''We start the GUI only when the token is passed by this function'''
        self.jwt = token
        self.username = username
        self.init_scrolled_area()
        self.retrieve_data()
        self.populate_gui()

    def refresh_page(self):
        # self.scrolled_friends.deleteLater()
        # self.init_scrolled_area()
        # self.retrieve_data()
        # self.populate_gui()
        print('refresh page')
        pass

    def init_scrolled_area(self):
        self.scrolled_friends: QWidget = ScolledFriends()
        self.addWidget(self.scrolled_friends)

    def populate_friends(self, friends_list: list[str]):
        print('friends list', friends_list)
        friends_grid_layout = QGridLayout()
        num_columns = 4

        # Add items to the grid layout dynamically
        for index, item in enumerate(friends_list):
            req_username = str(item)
            row = index // num_columns
            col = index % num_columns
            friend_req_label = MyFriend(username=req_username, token=self.jwt)
            friends_grid_layout.addWidget(friend_req_label, row, col)
            print('nuevo qlabel em', row, col)
            self.scrolled_friends.new_label(friend_req_label, row, col)

        # layout.addLayout(friends_grid_layout)
        # self.scrolled_friends.new_label(layout)

    def populate_gui(self):
        '''We populate the GUI with the data we get from the API only when the token is passed
        by the function get_token and after filtering the data to avoid repeated cases'''
        self.only_friends = [
            friend for friend in self.list_of_friends if friend not in self.list_of_users_pending
            and friend != self.username]
        pendient = [
            pendient for pendient in self.list_of_users_pending if pendient['username'] not in self.only_friends
            and pendient['username'] != self.username]
        print('11only friends', self.only_friends)
        print('11pendientt', pendient)
        self.populate_friends(self.only_friends)

    def retrieve_data(self) -> None:
        # TODO: Retrieving the friends
        data: list = get_friend_list(self, self.jwt)
        self.list_of_friends: list = []
        # We create a new object just with the info we need
        for user_obj in data:
            # map_user_obj: map = {}
            # username = user_obj['username']
            # is_accepted = user_obj['accepted']
            # is_pendient = user_obj['pendient']
            # is_rejected = user_obj['rejected']
            # map_user_obj.update({'username': username})
            # map_user_obj.update({'is_accepted': is_accepted})
            # map_user_obj.update({'is_pendient': is_pendient})
            # map_user_obj.update({'is_rejected': is_rejected})
            self.list_of_friends.append(user_obj)

        # TODO: Retrieving the pendient friends
        data: list = get_pendient_friends(self, self.jwt)
        self.list_of_users_pending: list = []
        # We create a new object just with the info we need
        print(' data', data)
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

        # self.hbox_buttons = QHBoxLayout()
        # layout = QVBoxLayout()
        # friends_grid_layout = QGridLayout()
        # num_columns = 5

        # # Add items to the grid layout dynamically
        # for index, item in enumerate(self.list_of_friends):
        #     # Cast to string
        #     # req_username = str(item['username'])
        #     # is_pendient = str(item['is_pendient'])
        #     # is_accepted = str(item['is_accepted'])
        #     # is_rejected = str(item['is_rejected'])
        #     row = index // num_columns
        #     col = index % num_columns
        #     req_username = str(item)

        #     # friend_req_label = MyFriend(username=req_username, token=self.jwt)
        #     # friends_grid_layout.addWidget(friend_req_label, row, col)

        # layout.addLayout(friends_grid_layout)
        # self.addLayout(layout)
