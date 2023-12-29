from PyQt6.QtCore import QTimer, QCoreApplication
import sys
import os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from styles.styles import global_style
from Frames.frame1 import Frame1
from Frames.frame_login import FrameLogin

image_florence = 'florence.jpg'
aristotle_1 = 'aristotle_1.jpg'

if __name__ == '__main__':
    try:
        # Debug functionn
        def hook(type, value, traceback) -> None:
            print('hook - type:', type)
            print('hook - traceback:', traceback)
        sys.__excepthook__ = hook
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(os.path.join('images', 'logo32.png')))
        window = Frame1()
        login_window = FrameLogin()
        window.setStyleSheet(global_style)

        # login_window.setStyleSheet(global_style)
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

    #     def change_style() -> None:
    #         # Red component
    #         if window.r_colour >= 0 and window.r_first_cycle:
    #             window.r_colour -= 1  # Red component
    #             if window.r_colour == 0:
    #                 window.r_first_cycle = False
    #                 window.r_second_cycle = True
    #         if window.r_colour >= 0 and window.r_colour <= 107 and window.r_second_cycle == True:
    #             window.r_colour += 1  # Red component
    #             if window.r_colour == 107:
    #                 window.r_first_cycle = True
    #                 window.r_second_cycle = False
    #         # Green component
    #         if window.g_colour >= 0 and window.g_first_cycle:
    #             window.g_colour -= 1  # Red component
    #             if window.g_colour == 0:
    #                 window.g_first_cycle = False
    #                 window.g_second_cycle = True
    #         if window.g_colour >= 0 and window.g_colour <= 180 and window.g_second_cycle == True:
    #             window.g_colour += 1  # Red component
    #             if window.g_colour == 180:
    #                 window.g_first_cycle = True
    #                 window.g_second_cycle = False
    #         # Blue component
    #         if window.b_colour >= 0 and window.b_first_cycle:
    #             window.b_colour -= 4  # Red component
    #             if window.b_colour == 0:
    #                 window.b_first_cycle = False
    #                 window.b_second_cycle = True
    #         if window.b_colour >= 0 and window.b_colour <= 255 and window.b_second_cycle == True:
    #             window.b_colour += 4  # Red component
    #             if window.b_colour == 255:
    #                 window.b_first_cycle = True
    #                 window.b_second_cycle = False

    #         # Ensure that the values are within the appropriate range (0-255)
    #         window.r_colour = max(0, min(window.r_colour, 255))
    #         window.g_colour = max(0, min(window.g_colour, 255))
    #         window.b_colour = max(0, min(window.b_colour, 255))
    #         # Turn the RGB values into hexadecimal format
    #         gradient_colour = "#{:02X}{:02X}{:02X}".format(
    #             window.r_colour, window.g_colour, window.b_colour)
    #         window.timer.stop()
    #         window.setStyleSheet(f"""
    # QWidget {{
    #     background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
    #                                 #000DFF);
    #                                 stop: 0 {gradient_colour}, stop: 1
    # }}
    # """)
        # QCoreApplication.processEvents()
        # window.timer.start()

        # window.timer.timeout.connect(change_style)

        # edit_profile_window = EditProfile()
        # chat_frame = ChatFrame()

        # This two code lines below, trigger to open a login window and close the main
        window.login_button.login_signal.connect(login_window.launch)

        window.login_button.login_signal.connect(window.close)
        window.login_button.signal_jwt_login.connect(login_window.jws_writter)
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
        # login_window.edit_account.clicked.connect(edit_profile_window.show_profile)
        # TODO TODO TODO
        # login_window.chat_button.signal_pressed.connect(
        #     edit_profile_window.get_username)
        # TODO TODO TODO
        # When the chat opens, we need to charging the .png image or set the default one
        # TODO TODO TODO
        # login_window.chat_button.clicked.connect(
        #     edit_profile_window.get_username)
        # TODO TODO TODO
        # input_image = ImageViewer()
        # input_image.setStyleSheet(global_style)

        # TODO: Add a new friend
        login_window.chat_frame.signal_send_request_friend.connect(
            login_window.add_friend_func)
        window.volume_label.clicked_signal.connect(login_window.manage_music)
        window.volume_label.clicked_signal.connect(
            window.volume_icon_change)
        login_window.volume_label.clicked_signal.connect(
            login_window.manage_music)
        # login_window.volume_label.clicked_signal.connect(
        #     login_window.volume_icon_change)

        # TODO AAAA TODO
        # new message
        login_window.client_communicator.message_received.connect(
            login_window.chat_frame.new_message)
        # Opening the chat
        login_window.chat_button.clicked.connect(
            login_window.chat_frame.launch)
        window.login_button.signal_jwt_login.connect(
            login_window.chat_frame.jwt_receiver)

        # TODO if the user close the session, then terminate the whole application,
        # but we need to fix this and just close the sockets, not the whole application,
        # this imply that we need to change the way we are closing the sockets and maybe more.
        login_window.logout_button.clicked.connect(window.close)

        login_window.chat_frame.send_message_signal.connect(
            login_window.client_communicator.send_message)
        # TODO AAA TODO
        # # Opening the chat
        # login_window.chat_button.clicked.connect(chat_frame.launch)
        # login_window.chat_button.jwt_emit.connect(chat_frame.jwt_receiver)
        # todo this TODO arreglar esto JWT UNO SOLOOO
        # window.login_button.signal_jwt_login.connect(chat_frame.jwt_receiver)
        # TODO TODO TODO
        window.login_button.signal_jwt_login.connect(
            login_window.edit_account_frame.jwt_receiver)
        # TODO TODO TODO

        # # new message
        # login_window.client_communicator.message_received.connect(
        #     chat_frame.new_message)
        # chat_frame.client_communicator.message_received.connect(
        #     chat_frame.new_message)
        # Here, we send the first message through the socket to the server with the token:
        # TODO
        login_window.send_message_login.connect(
            login_window.client_communicator.send_message)
        # chat_frame.send_message_signal.connect(
        #     login_window.client_communicator.send_message)
        # When the client is ready, send the first message
        # login_window.client_communicator.client_ready.connect(
        #     login_window.send_first_message)
        # TODO TODO TODO
        # Changing the layout of the edit profile window

        login_window.edit_account_frame.go_back_pixmap.signal_profile_close.connect(
            login_window.edit_account_frame.close_and_det_first_page)

        login_window.edit_account_frame.stack_button1.clicked.connect(
            login_window.edit_account_frame.change_page)
        login_window.edit_account_frame.stack_button2.clicked.connect(
            login_window.edit_account_frame.change_page)
        login_window.edit_account_frame.stack_button2.clicked.connect(
            login_window.edit_account_frame.messages_widget.set_first_messages)

        login_window.edit_account_frame.stack_button3.clicked.connect(
            login_window.edit_account_frame.change_page)
        login_window.edit_account_frame.stack_button4.clicked.connect(
            login_window.edit_account_frame.change_page)
        login_window.edit_account_frame.stack_button5.clicked.connect(
            login_window.edit_account_frame.change_page)
        # Conec
        login_window.edit_account.clicked.connect(
            login_window.edit_account_frame.show_profile)
        # Conectamos la de;al de presional el QLabel con cerrar el chat
        login_window.chat_frame.go_back_pixmap.signal_profile_close.connect(
            login_window.chat_frame.timer_animate_close.start)
        # Conectamos la de;al de presionar el Qlabel con cerrar el menu
        login_window.edit_account_frame.go_back_pixmap.signal_profile_close.connect(
            login_window.edit_account_frame.timer_expand_animation_close.start)
        # TODO lo mismo de arriba, pero ahora si el usuario aprieta escape
        # login_window.edit_account_frame.signal_escape.connect(
        #     login_window.chat_frame.timer_animate_close.start)
        # Conectamos la de;al de presional el Qlabel con la shadow que aparece
        # login_window.edit_account_frame.go_back_pixmap.signal_profile_close.connect(
        #     login_window.edit_account_frame.close_menu_shadow)

        # Conectamos la senal de presionar enviar mensaje privado offline con la ventana que lo abre
        login_window.edit_account_frame.private_message_frame.signal_send_message_offline.connect(
            login_window.edit_account_frame.private_message_frame.show_function)

        # TODO TODO TODO
        # login_window.edit_account.clicked.connect(
        #     edit_profile_window.show_profile)
        # Profile picture chat clicked
        # timer = QTimer()
        # timer.timeout.connect(enviar_senal)
        # timer.start(1000)  # Cada 1000 milisegundos (1 segundo)
        # def enviar_senal():
        #     for element in chat_frame.pixmaps_profiles_array:
        #         element.signal_profile_picture_clicked.emit('press')
        # def printear():
        #     print("Clic en la imagen del chat")
        # chat_frame.pixmaps_profiles_array[0].signal_profile_picture_clicked.connect(printear)

        # window.signal_frame1.connect(chat_frame.close_all)
        # login_window.signal_frame_login.connect(chat_frame.close_all)
        sys.exit(app.exec())
    except KeyboardInterrupt as e:
        window.timer.stop()
        print(e)
    finally:
        window.timer.stop()
