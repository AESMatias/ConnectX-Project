from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QScrollArea, QSizePolicy)
from PyQt6.QtGui import QPixmap
from styles.styles import InputFieldStyle, login_label_ok
from components.chat_functions import QLabelProfilePicture, ChatWidget, ProfileViewBackground, QLabelMessageMail
from components.messages_functions import MessagesBoxWidget
from typing import Tuple, List
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton
import numpy as np
from PIL import Image
from PyQt6 import QtGui
import os
from components.global_functions import QLabel_Exit
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPalette, QBrush, QGuiApplication
import requests
import json


class ScolledFriends(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.pixmaps_profiles_array = []
        self.pixmaps_profiles_array = []
        self.background_widgets_list = []
        self.chat_widgets_list = []
        self.hor_layouts_to_delete = []
        self.init_gui()
        self.show()
        self.raise_()
        self.animation_steps = 50
        self.current_step = 0
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # Monitor dimensions
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
        # The bellowing line isn't necessary, but it is for ensuring the geometry
        self.setGeometry(0, 0, int(self.screen_width * 0.7),
                         int(self.screen_height*0.7))

        # Create a custom QPalette with the background image
        palette = QPalette()
        background_image = QPixmap(
            os.path.join('images', 'wallpaper_chat.jpg'))
        self.setAutoFillBackground(True)
        self.brush = QBrush(background_image)
        palette.setBrush(QPalette.ColorRole.Window, self.brush)
        self.setPalette(palette)
        self.setStyleSheet(f"""
            QWidget {{
                background-image: url({background_image});
                background-repeat: no-repeat;
                background-position: center;
                background-color: rgba(0, 0, 0, 128);
            }}
        """)

    def launch(self) -> None:
        sender = self.sender()
        if sender.login_status == True:
            self.active_users_chat = self.active_users()
            self.username = sender.username
            self.move(0, 0)
            self.show()
            self.raise_()
            self.setFocus()
            self.timer_animate_start.start(1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.retrieve_messages()

    def new_label(self, label, row, col):
        pixmap_delete64 = QPixmap('images/delete64.png').scaled(
            40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # if label:
        #     self.counter_messages += 1
        #     horizontal_layout = QHBoxLayout()
        #     horizontal_layout.addWidget(label)
        #     self.hor_layouts_to_delete.append(horizontal_layout)
        #     self.container_layout.addLayout(horizontal_layout)

        # Add items to the grid layout dynamically
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(label)
        # self.grid.addLayout(horizontal_layout, row, col)
        self.gridLayout_2.addWidget(label, row, col)
        # friends_grid_layout.addWidget(friend_req_label, row, col)
        # self.scrolled_friends.new_label(friend_req_label, row, col)

    def init_gui(self) -> None:

        # self.grid = QGridLayout()
        # # widget_temporal = QWidget()
        # # widget_temporal.setLayout(self.grid)

        # # Create a scroll area and the container
        # self.scroll_area = QScrollArea(self)
        # self.scroll_area.setHorizontalScrollBarPolicy(
        #     Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # # Create a widget to contain the layout
        # self.container_widget = QWidget(self.scroll_area)
        # self.scroll_area.setStyleSheet(
        #     "background-color: rgba(30, 70, 180, 0.1); color: white;")
        # self.container_layout = QVBoxLayout(self.container_widget)

        # # Set the container widget as the scroll area's widget
        # self.scroll_area.setWidget(self.container_widget)
        # self.scroll_area.setWidgetResizable(True)
        # self.container_widget.setMinimumHeight(600)
        # self.container_widget.setMinimumWidth(1300)
        # self.scroll_area.setFixedHeight(600)
        # self.scroll_area.setFixedWidth(1300)

        # self.scroll_area.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # self.container_widget.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # self.container_layout.addLayout(self.grid)
        # self.setLayout(self.container_layout)

        self.setObjectName("Form")
        self.resize(387, 324)
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 365, 302))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)
        # # Vertical
        # vbox = QVBoxLayout()
        # vbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # hbox_final = QHBoxLayout()
        # hbox_final.addLayout(vbox)
        # self.setLayout(hbox_final)
        # GRID
        # grid = QGridLayout()
        # grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.setLayout(grid)

    # def clean_the_messages(self):
    #     for elem in self.container_widget.children():
    #         if type(elem) == QLabelMessageMail or type(elem) == QLabelProfilePicture or type(elem) == QLabel:
    #             print('borrando elem', elem)
    #             elem.deleteLater()

    #     for elem in self.pixmaps_profiles_array:
    #         elem.deleteLater()
    #     for elem in self.background_widgets_list:
    #         elem.deleteLater()
    #     # for elem in self.chat_widgets_list:
    #     #     elem.deleteLater()
    #     self.pixmaps_profiles_array.clear()
    #     self.background_widgets_list.clear()
    #     # self.chat_widgets_list.clear()
    #     self.hor_layouts_to_delete.clear()
    #     self.all_messages2.clear()
    #     self.all_messages2 = []
    #     # for _ in range(5):
    #     #     self.all_messages2.append('')
    #     self.counter_messages = 0
    #     self.counter_chat_enter = 0
