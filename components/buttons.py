# The import below isn't working
# from Login.login_module import login
from Server.login import login
from Login.register import register
from PyQt6.QtWidgets import (QPushButton, QLineEdit, QLabel)
from PyQt6.QtCore import (QObject, pyqtSignal)
import os
import sys
import requests
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
        self.resize(self.sizeHint())
        self.move(*pos)
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        sender = self.sender
        pass


class Upload_file(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        # self.clicked.connect(self.button_clicked)

    # def button_clicked(self) -> None:
    #     sender = self.sender()
    #     self.username = form_username
    #     self.login_status = True
    #     print('FILE OPEN')


class Register_Button(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.register_status = False
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        self.clicked.connect(self.button_clicked)

    def button_clicked(self) -> None:
        sender = self.sender()
        sender.repaint()  # To avoid bugs
        status_register = register(form_username, form_password)
        if status_register:
            self.register_status = True
            self.username = form_username
            print('SELF.USERNAME ', self.username, 'has been registered')
            self.login_status = True
            # self.login_signal.emit()
            print('Login status:', self.login_status)
        else:
            self.login_status = False
            print(f"No login with username {form_username}")


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
        self.register_status = False

    def button_clicked(self) -> None:
        sender = self.sender()
        sender.repaint()  # To avoid bugs
        status_login, text_response = login(form_username, form_password)
        print('RETORNAAA', status_login)
        # Username and password from the form
        username = form_username
        password = form_password
        # URL of the endpoint of the API for login
        # Reemplaza con la URL real de tu servidor
        url_login = "http://127.0.0.1:8000/login"

        # Datos para enviar en el cuerpo de la solicitud POST
        data = {
            "username": username,
            "password": password
        }

        # Realizar la solicitud POST
        response = requests.post(url_login, json=data)

        # Comprobar la respuesta del servidor
        if response.status_code == 200:
            # El servidor respondió con un código 200 (OK), lo que generalmente significa que el inicio de sesión fue exitoso
            # Esto depende de cómo se estructura la respuesta en el servidor
            is_valid = response.json()
            print("Inicio de sesión válido:", is_valid)
        else:
            # El servidor respondió con un código de error (por ejemplo, 401 Unauthorized)
            print("Error en el inicio de sesión. Código de estado:",
                  response.status_code)

        if status_login and self.name == 'logoutnButton':
            self.username = form_username
            print('SELF.USERNAME ', self.username)
            self.login_status = False
            self.login_signal.emit()
            print('Login status:', self.login_status)
        elif status_login and self.name == 'loginButton':
            self.username = form_username
            self.login_status = True
            print('SELF.USERNAME ', self.username)
            self.login_signal.emit()
            print('Login status:', self.login_status)
        elif status_login:
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
