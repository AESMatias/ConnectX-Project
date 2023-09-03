from PyQt6.QtCore import QTimer
import sys
import os
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QFileDialog,
                             QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Register_Button, Login_Button, InputField
from styles.styles import InputFieldStyle, tag, button_style, global_style, login_label, login_label_wrong, login_label_ok
from Frames.frame1 import Frame1
from Frames.frame_login import FrameLogin
from components.input_user import ImageViewer
from Frames.edit_profile import EditProfile

image_florence = 'florence.jpg'
aristotle_1 = 'aristotle_1.jpg'

if __name__ == '__main__':

    # Debug function
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join('images', 'logo32.png')))
    window = Frame1()
    login_window = FrameLogin()
    window.setStyleSheet(global_style)
    login_window.setStyleSheet(global_style)
    # window.setFixedWidth(1280)
    window.show()
    edit_profile_window = EditProfile()

    # window2 = Frame()
    # window2.setStyleSheet(global_style)
    # window2.show()
    # This two code lines below, trigger to open a login window and close the main
    window.login_button.login_signal.connect(login_window.launch)
    window.login_button.login_signal.connect(window.close)

    # Once the login was successful, we adding the close session option
    login_window.logout_button.login_signal.connect(window.show)
    login_window.logout_button.login_signal.connect(login_window.close)
    #
    window.login_button.clicked.connect(login_window.change_username_status)
    login_window.logout_button.clicked.connect(window.remove_registered_label)

    window.register_button.clicked.connect(
        window.show_register_status)
    # open the account configuration
    login_window.edit_account.clicked.connect(edit_profile_window.show)
    #
    input_image = ImageViewer()
    input_image.setStyleSheet(global_style)
    sys.exit(app.exec())
