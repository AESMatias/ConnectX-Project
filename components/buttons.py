# The import below isn't working
from Login.login_module import login
from PyQt6.QtWidgets import (QPushButton, QLineEdit, QLabel)
from PyQt6.QtCore import (QObject, pyqtSignal)
import os
import sys
# print(sys.builtin_module_names)
# print(sys.path)
debugMode: bool = True
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

form_username = ''
form_password = ''


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

    def button_clicked(self, register_label) -> bool:
        sender = self.sender()
        print(sender.text(), "Pressed!") if debugMode else None


class Login_Button(QPushButton):
    login_signal = pyqtSignal()

    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        self.login_status = False  # Has been logged successfully?
        self.clicked.connect(self.button_clicked)
        # global form_username
        self.username = form_username

    # def mousePressEvent(self, event):
    #     self.login_signal.emit()

    def button_clicked(self) -> None:
        sender = self.sender()
        sender.repaint()  # To avoid bugs
        status_login = login(form_username, form_password)
        if status_login:
            self.username = form_username
            print('SELF.USERNAME ', self.username)
            self.login_status = True
            self.login_signal.emit()
            print('Login status:', self.login_status)
        else:
            self.login_status = False
            print(f"No login with username {form_username}")


class InputField(QLineEdit):
    def __init__(self, name: str, text: str, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.name = name
        self.text = ''
        self.textChanged.connect(self.change_text)

    def change_text(self, text_field: str):
        print('text changed to', text_field)
        global form_username
        global form_password
        if self.name == 'username_field':
            form_username = text_field
        elif self.name == 'password_field':
            form_password = text_field
