# The import below isn't working
# from Login.login_module import login
from PyQt6.QtWidgets import (QPushButton)
import os
import sys
# print(sys.builtin_module_names)
# print(sys.path)
debugMode: bool = True
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from Login.login_module import login


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

    def button_clicked(self):
        print('Register button pressed!') if debugMode else None
        return self.status


class Login_Button(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.counter_clicks = 0
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        self.clicked.connect(self.button_clicked)
        self.status = False  # Has been clicked?

    def button_clicked(self):
        print('Login button pressed!') if debugMode else None
        login('jose', 'pepe')
        return self.status
