from PyQt6.QtCore import QTimer, QCoreApplication, Qt, QObject, pyqtSignal
import sys
import os
import socket
import asyncio
import os
from typing import Optional, List, Dict, Set, Tuple, Union, Any, Literal, Text
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QFileDialog,
                             QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import Register_Button, Login_Button, InputField
from styles.styles import InputFieldStyle, tag, button_style, global_style, global_style_changed, login_label, login_label_wrong, login_label_ok
from Login.client_socket import ClientCommunicator
from Frames.frame1 import Frame1
from Frames.frame_login import FrameLogin
from components.input_user import ImageViewer
from Frames.edit_profile import EditProfile
from Frames.chat import ChatFrame
from threading import Thread

image_florence = 'florence.jpg'
aristotle_1 = 'aristotle_1.jpg'

if __name__ == '__main__':
    try:
        # Debug functionn
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
        window.timer = QTimer()
        window.timer.setInterval(150)
        window.timer.start()

        # RGB components for the gradient of the background
        window.r_first_cycle = True
        window.g_first_cycle = True
        window.r_second_cycle = False
        window.g_second_cycle = False
        window.b_first_cycle = True
        window.b_second_cycle = False
        window.r_colour = 107  # Red component
        window.g_colour = 115  # Green component
        window.b_colour = 255  # Blue component

        def change_style():
            # Red component
            if window.r_colour >= 0 and window.r_first_cycle:
                window.r_colour -= 1  # Red component
                if window.r_colour == 0:
                    window.r_first_cycle = False
                    window.r_second_cycle = True
            if window.r_colour >= 0 and window.r_colour <= 107 and window.r_second_cycle == True:
                window.r_colour += 1  # Red component
                if window.r_colour == 107:
                    window.r_first_cycle = True
                    window.r_second_cycle = False
            # Green component
            if window.g_colour >= 0 and window.g_first_cycle:
                window.g_colour -= 1  # Red component
                if window.g_colour == 0:
                    window.g_first_cycle = False
                    window.g_second_cycle = True
            if window.g_colour >= 0 and window.g_colour <= 180 and window.g_second_cycle == True:
                window.g_colour += 1  # Red component
                if window.g_colour == 180:
                    window.g_first_cycle = True
                    window.g_second_cycle = False
            # Blue component
            if window.b_colour >= 0 and window.b_first_cycle:
                window.b_colour -= 4  # Red component
                if window.b_colour == 0:
                    window.b_first_cycle = False
                    window.b_second_cycle = True
            if window.b_colour >= 0 and window.b_colour <= 255 and window.b_second_cycle == True:
                window.b_colour += 4  # Red component
                if window.b_colour == 255:
                    window.b_first_cycle = True
                    window.b_second_cycle = False

            # Ensure that the values are within the appropriate range (0-255)
            window.r_colour = max(0, min(window.r_colour, 255))
            window.g_colour = max(0, min(window.g_colour, 255))
            window.b_colour = max(0, min(window.b_colour, 255))
            # Turn the RGB values into hexadecimal format
            gradient_colour = "#{:02X}{:02X}{:02X}".format(
                window.r_colour, window.g_colour, window.b_colour)
            window.timer.stop()
            window.setStyleSheet(f"""
    QWidget {{
        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                    stop: 0 {gradient_colour}, stop: 1 #000DFF);
    }}
    """)
            QCoreApplication.processEvents()
            window.timer.start()
        window.timer.timeout.connect(change_style)

        edit_profile_window = EditProfile()
        chat_frame = ChatFrame()

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
        window.login_button.clicked.connect(
            login_window.change_username_status)
        login_window.logout_button.clicked.connect(
            window.remove_registered_label)

        window.register_button.clicked.connect(
            window.show_register_status)
        # open the account configuration
        login_window.edit_account.clicked.connect(edit_profile_window.show)
        #
        input_image = ImageViewer()
        input_image.setStyleSheet(global_style)

        # open the account configuration
        # login_window.chat_button.clicked.connect(chat_frame.show)
        login_window.chat_button.clicked.connect(chat_frame.launch)

        chat_frame.client_communicator.message_received.connect(
            chat_frame.new_message)

        # # Host and port of FastAPI
        # host = "127.0.0.1"
        # port = 12345
        # # Create the client socket
        # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # client_communicator = ClientCommunicator('127.0.0.1', 12345)
        # client_thread = Thread(target=client_communicator.run_client)
        # window.login_button.login_signal.connect(client_thread.start)

        # def print_message(message):
        #     print('print_message>', message)
        # client_communicator.message_received.connect(print_message)

        sys.exit(app.exec())
    except KeyboardInterrupt:
        sys.exit(app.exec())
    finally:
        sys.exit(app.exec())
