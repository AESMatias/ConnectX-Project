from PyQt6.QtCore import QTimer, QCoreApplication
import sys
import os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from styles.styles import global_style
from Frames.frame1 import Frame1
from Frames.frame_login import FrameLogin
from components.input_user import ImageViewer
from components.global_functions import center_window
from Frames.edit_profile import EditProfile
from Frames.chat import ChatFrame
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
        window.show()
        window.timer = QTimer()
        window.timer.setInterval(150)
        window.timer.start()

        center_window(window)

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

        def change_style() -> None:
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
        # Opening the edit profile window
        login_window.edit_account.clicked.connect(edit_profile_window.show)
        input_image = ImageViewer()
        input_image.setStyleSheet(global_style)

        # Volume label clicked
        window.volume_label.clicked_signal.connect(login_window.manage_music)
        window.volume_label.clicked_signal.connect(
            window.volume_icon_change)
        # Opening the chat
        login_window.chat_button.clicked.connect(chat_frame.launch)

        chat_frame.client_communicator.message_received.connect(
            chat_frame.new_message)
        chat_frame.send_message_signal.connect(
            chat_frame.client_communicator.send_message)
        # window.signal_frame1.connect(chat_frame.close_all)
        # login_window.signal_frame_login.connect(chat_frame.close_all)
        sys.exit(app.exec())
    except KeyboardInterrupt as e:
        window.timer.stop()
        print(e)
    finally:
        window.timer.stop()
