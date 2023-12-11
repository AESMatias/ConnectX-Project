# The import below isn't working
from Login.login import login
from Login.register import register
from PyQt6.QtWidgets import (QPushButton, QLineEdit)
from PyQt6.QtCore import (pyqtSignal, QUrl)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QGuiApplication
import os
import sys
from typing import Tuple
import requests
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

form_username = ''
form_password = ''
password_not_visible = ''
jwt_token = ''


class EditProfileButton(QPushButton):
    edit_stack_layout = pyqtSignal(int)

    def __init__(self, name: str, index: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.resize(self.sizeHint())
        self.index = index
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.edit_stack_layout.emit(self.index)


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

        # Obtaining the screen dimensions
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # Obtaining the screen dimensions
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Central position of the button
        button_width = self.sizeHint().width()
        button_height = self.sizeHint().height()
        x_position = (screen_width - button_width) // 2
        y_position = (screen_height - button_height) // 2

        # Stablish the button position in the center of the screen
        self.setGeometry(x_position, y_position, button_width, button_height)

    def button_clicked(self) -> None:
        sender = self.sender()
        status_register = register(form_username, password_not_visible)
        if status_register == True:
            self.register_status = True
            self.username = form_username
            print('SELF.USERNAME ', self.username, 'has been registered')
            self.login_status = True
            # self.login_signal.emit()
            print('Login status:', self.login_status)
            # Successfull sound
            self.media_player = QMediaPlayer(self)
            self.media_player.setAudioOutput(QAudioOutput(self))
            file_url = QUrl.fromLocalFile(os.path.join(
                'Music', 'mixkit-fantasy-game-sweep-notification-255.wav'))
            self.media_player.setSource(file_url)
            # self.media_player.mediaStatusChanged.connect(self.handle_media_status)
            self.media_player.play()

        elif status_register == False:
            self.login_status = False
            print(f"No login with username {form_username}")
            # Unsuccessfull sound
            self.media_player = QMediaPlayer(self)
            self.media_player.setAudioOutput(QAudioOutput(self))
            file_url = QUrl.fromLocalFile(os.path.join(
                'Music', 'mixkit-alert-bells-echo-765.wav'))
            self.media_player.setSource(file_url)
            # self.media_player.mediaStatusChanged.connect(self.handle_media_status)
            self.media_player.play()


class Login_Button(QPushButton):
    login_signal = pyqtSignal()
    signal_jwt_login = pyqtSignal(str)

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
        status_login = login(form_username, password_not_visible)
        print('RETORNAAA', status_login)
        # if status_login[0] == False:
        #     self.username = form_username
        #     print('SELF.USERNAME ', self.username)
        #     self.login_status = False
        #     self.login_signal.emit()
        #     print('Login status:', self.login_status)
        if status_login[0] == True:
            print(f"soy un jwt {status_login[1]}")
            self.signal_jwt_login.emit(status_login[1])
            self.username = form_username
            self.login_status = True
            print('SELF.USERNAME ', self.username)
            self.login_signal.emit()
            print('Login status:', self.login_status)\

        # Login successfull sound
            self.media_player = QMediaPlayer(self)
            self.media_player.setAudioOutput(QAudioOutput(self))
            file_url = QUrl.fromLocalFile(os.path.join(
                'Music', 'mixkit-fantasy-game-sweep-notification-255.wav'))
            self.media_player.setSource(file_url)
            # self.media_player.mediaStatusChanged.connect(self.handle_media_status)
            self.media_player.play()
        # elif status_login:
        #     self.username = form_username
        #     print('SELF.USERNAME ', self.username)
        #     self.login_status = True
        #     self.login_signal.emit()
        #     print('Login status:', self.login_status)
        elif status_login[0] == False:
            # Login unsuccessfull sound
            self.media_player = QMediaPlayer(self)
            self.media_player.setAudioOutput(QAudioOutput(self))
            file_url = QUrl.fromLocalFile(os.path.join(
                'Music', 'mixkit-alert-bells-echo-765.wav'))
            self.media_player.setSource(file_url)
            # self.media_player.mediaStatusChanged.connect(self.handle_media_status)
            self.media_player.play()
            self.login_status = False
            print(f"No login with username {form_username}")


class InputField(QLineEdit):
    def __init__(self, name: str, text: str, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.name = name
        self.text = ''
        self.textChanged.connect(self.change_text)
        self.password_has_been_changed = False

    def change_text(self, text_field: str):
        global form_username
        global form_password
        global password_not_visible
        if self.name == 'username_field':
            form_username = text_field
            print('username', form_username)
        elif self.name == 'password_field':
            # Later, change the entire password field to * at [index] with a temporary variable
            # with a library.
            form_password = text_field
            # Then the hole password has been deleted
            if len(text_field) == 0 and self.password_has_been_changed:
                password_not_visible = ''
                self.password_has_been_changed = False
            # Then the hole password has been changed to a character
            elif abs(len(password_not_visible)-len(text_field)) > 1 and self.password_has_been_changed:
                if len(text_field) != 0:
                    password_not_visible = text_field[-1]
                else:
                    password_not_visible = ''
                self.password_has_been_changed = False
            # Then a character has been added
            elif len(password_not_visible)-len(text_field) < 0 and self.password_has_been_changed:
                password_not_visible += text_field[-1]
                self.password_has_been_changed = True
            # Then a character has been deleted
            elif len(password_not_visible)-len(text_field) > 0 and self.password_has_been_changed:
                password_not_visible = password_not_visible[:-1]
                self.password_has_been_changed = True
            else:
                password_not_visible += text_field[-1]
                self.password_has_been_changed = True
            print('password_not_visible', password_not_visible)
            # Disconnect the signal textChanged so it doesn't infinite loop
            self.textChanged.disconnect(self.change_text)
            # Set the password text to asterisks
            self.setText('*' * len(text_field))
            password_has_been_changed = True
            # Connect the signal again
            self.textChanged.connect(self.change_text)


class Chat_Button(QPushButton):
    login_signal = pyqtSignal(str)
    jwt_emit = pyqtSignal(str)

    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        self.login_status = True  # FIX THIS, NEEDS TO CHANGE
        self.clicked.connect(self.button_clicked)
        self.username = form_username
        self.register_status = False

    def retrieve_image_get(self, jwt_token: str) -> Tuple[bool, str]:
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

    def button_clicked(self) -> None:
        status_login = login(form_username, password_not_visible)
        jwt_token = status_login[1]
        print('chatRETORNAAA', status_login)
        if status_login and self.name == 'chatButton':
            self.username = form_username
            print('SELF.USERNAME ', self.username)
            self.login_status = True
            self.jwt_emit.emit(jwt_token)
            print('Login status:', self.login_status)
            self.retrieve_image_get(jwt_token)

        # elif status_login and self.name == 'chatButton':
        #     self.username = form_username
        #     self.login_status = True
        #     print('SELF.USERNAME ', self.username)
        #     self.login_signal.emit()
        #     print('Login status:', self.login_status)
        # # Login successfull sound
        #     self.media_player = QMediaPlayer(self)
        #     self.media_player.setAudioOutput(QAudioOutput(self))
        #     file_url = QUrl.fromLocalFile(os.path.join(
        #         'Music', 'mixkit-fantasy-game-sweep-notification-255.wav'))
        #     self.media_player.setSource(file_url)
        #     # self.media_player.mediaStatusChanged.connect(self.handle_media_status)
        #     self.media_player.play()
        elif status_login:
            self.username = form_username
            print('SELF.USERNAME ', self.username)
            self.login_status = True
            self.login_signal.emit()
            print('Login status:', self.login_status)
        else:
            # Login unsuccessfull sound
            self.media_player = QMediaPlayer(self)
            self.media_player.setAudioOutput(QAudioOutput(self))
            file_url = QUrl.fromLocalFile(os.path.join(
                'Music', 'mixkit-alert-bells-echo-765.wav'))
            self.media_player.setSource(file_url)
            # self.media_player.mediaStatusChanged.connect(self.handle_media_status)
            self.media_player.play()
            self.login_status = False
            print(f"No login with username {form_username}")
