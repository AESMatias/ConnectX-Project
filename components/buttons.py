# The import below isn't working
# from Login.login_module import login
from Login.login_module import login
from PyQt6.QtWidgets import (QPushButton)
import os
import sys
# print(sys.builtin_module_names)
# print(sys.path)
debugMode: bool = True
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


class Button(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.counter_clicks = 0
        self.resize(self.sizeHint())
        self.move(*pos)
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.counter_clicks += 1
        print(f'Button {self.name} clicked {self.counter_clicks} times.')


class Register_Button(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.counter_clicks = 0
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        self.clicked.connect(self.button_clicked)
        self.status = False  # Has been clicked?

    def button_clicked(self, register_label) -> bool:
        sender = self.sender()
        print(sender.text(), "Pressed!") if debugMode else None
        return self.status


class Login_Button(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.counter_clicks = 0
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        self.login_status = False  # Has been logged successfully?
        self.clicked.connect(self.button_clicked)
        # self.username = username
        # self.password = password

    def button_clicked(self) -> bool:
        sender = self.sender()
        sender.repaint()  # To avoid bugs
        # print(self.passa, 'passa') if debugMode else None
        login(self.username, self.password)
        print('username', self.username)
        print('pass', self.password)
        if login(self.username, self.password):
            self.login_status = True
        return self.login_status
