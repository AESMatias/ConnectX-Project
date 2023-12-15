from threading import Thread
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QScrollArea, QSizePolicy)
from PyQt6.QtGui import QPixmap
from styles.styles import InputFieldStyle, login_label_ok
from components.global_functions import center_window
from Login.client_socket import ClientCommunicator
from components.chat_functions import QLabelProfilePicture, ChatWidget, ProfileViewBackground, QLabelMessage
from Login.login import login
from typing import Tuple
import requests
import os
from PyQt6.QtGui import QPalette, QBrush
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtCore import Qt


class ChatFrame(QWidget):
    send_message_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setFixedSize(1000, 750)
        self.counter_messages = 0
        self.username = ''
        self.username_tuple = ()
        qlabelpixamap = QLabel(self)
        qlabelpixamap.setPixmap(QPixmap('images/logo32.png'))
        self.image_pixmap_1 = qlabelpixamap
        self.image_pixmap_1.setVisible(False)
        self.profile_pixmap = QPixmap('images/profile_image.png')
        self.init_gui()
        self.host = "127.0.0.1"
        self.port = 12345
        # self.client_communicator = ClientCommunicator(
        #     self.host, self.port, self.username)
        self.intentos_restantes_jwt = 1
        # self.client_thread = Thread(target=self.client_communicator.run_client)
        # Profile View
        self.chat_widget = ChatWidget()
        self.chat_widget.hide()
        # Profile View Background
        self.background_widget = ProfileViewBackground(self)
        self.background_widget.hide()

        self.pixmaps_profiles_array = []
        self.scroll_area = QScrollArea()
        # aplicamos transparencia al scroll area
        self.scroll_area.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # Crear un QPalette personalizado con la imagen de fondo
        palette = QPalette()
        background_image = QPixmap(
            os.path.join('images', 'chat_wallpaper.jpg'))

        # background_image = background_image.scaled(
        #     self.size()*2, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
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

    def retrieve_image_get(jwt_token: str) -> Tuple[bool, str]:
        status_login = login("admin", "admin")
        jwt_token = status_login[1]
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

    def closeEvent(self, event):
        print("Closing the window")
        # Then, before closing the window, we need to close the sockets and threads
        # self.client_communicator.client_socket.close()
        # self.client_communicator.send_message_socket.close()

        # We need to close the thread too, fix this!!!!!!!!! TO-DO:
        # self.client_thread.join()
        # self.client_communicator._stop_threads = True
        # cerramos los hilos todos y los sockets abiedrtos tambien
        # self.client_communicator.client_socket.close()
        # self.client_communicator.send_message_socket.close()
    # def close_all(self):
    #     print(f"Closing the window{self}")
    #     self.client_communicator.client_socket.close()
    #     self.client_communicator.send_message_socket.close()
    #     self.client_thread.join()

    def keyPressEvent(self, event) -> None:
        if event.key() == QtCore.Qt.Key.Key_Return or event.key() == 16777220:
            self.send_message()

    def jwt_receiver(self, jwt: str) -> None:
        self.jwt = jwt
        print('JWT:', self.jwt)

    def launch(self) -> None:
        sender = self.sender()
        if sender.login_status == True:
            print('CHAT initiated')
            self.username = sender.username
            self.labels['username'].setText(f'Welcome {self.username}')
            self.setWindowTitle(f'ConectX Project - {self.username}')
            # self.client_communicator.username = self.username
            # self.labels['username_status'].setText('Credentials OK')
            # self.labels['username_status'].setStyleSheet(login_label_ok)
            # self.labels['username_status'].repaint()  # To avoid bug
            center_window(self)
            self.show()
            self.setFocus()
            # self.client_thread = Thread(
            #     target=self.client_communicator.run_client)
            # self.client_thread.start()
            self.change_username_status()

    def send_message(self):
        text = self.write_message.text()
        # message = f"{text}"
        message = f"general|{self.jwt}|general|{text}"
        # if self.intentos_restantes_jwt == 1:

        #     self.intentos_restantes_jwt -= 1
        #     # self.send_message_signal.emit(self.jwt)
        #     # self.send_message_signal.emit(message)
        #     self.write_message.setText('')
        #     # no lee las siguientes lineas del codigo, asi que salimos de la func
        #     return

        self.send_message_signal.emit(message)
        self.write_message.setText('')
        if text.endswith('/close') or text.endswith('/exit'):
            pass
            # print('closing threads and sockets by send_message func')
            # # self.client_communicator.client_socket.close()
            # self.client_communicator.send_message_socket.close()
            # self.client_thread.join()

    def change_username_status(self):
        sender = self.sender()
        if sender.login_status == False:
            # self.labels['username_status'].setText('Invalid credentials')
            # self.labels['username_status'].setStyleSheet(login_label_wrong)
            # self.labels['username_status'].repaint()  # To avoid bugs
            pass
        elif sender.login_status == True:
            username = sender.username
            # self.labels['username'].setText(f'Welcome {username}')
            # self.setWindowTitle(f'ConectX Project - {username}')
            # self.labels['username'].repaint()  # To avoid bugs
            # self.client_communicator.username = username
            pass

    def get_pic_by_name(self, name: str) -> QPixmap:
        import requests

        url = "http://localhost:8000/user/picture/"

        querystring = {"user_name": f"{name}"}

        headers = {
            "Accept": "image/png"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        with open(f"profiles/images/{name}.png", "wb") as f:
            f.write(response.content)
        return QPixmap(f"profiles/images/{name}.png")

    def new_message(self, message):
        # TODO Change the username tuple
        # username, message = message.split(':')
        username = 'USERNAME_TEST'
        print('the message is ', message, 'and the username is ', username)
        if username not in self.username_tuple:
            self.username_tuple += (username,)

            # abrimos /profiles/images/username.png y miramos si existe tal archivo
            # si existe, lo cargamos, si no, lo descargamos
            ruta_archivo = f'profiles/images/{username}.png'

            # Verificar si el archivo existe
            if os.path.exists(ruta_archivo):
                print(
                    f'El archivo {ruta_archivo} existe, ergo no lo descargamos')
            else:
                print(f'El archivo {ruta_archivo} NO existe.')
                self.pixmap_username = self.get_pic_by_name(username)
                print('Obteniendo pixmap del usuario ', username)

        # message = username + ':' + message\

        # message = f"general|{self.jwt}|general|{message}"
        # general | token | general |Holaa
        # p2p | token | juanito | adios
        self.retrieve_image_get()
        # NO SE USA ESTO TODO
        qlabelpixamap = QLabelProfilePicture(username)
        # qlabelpixamap.setPixmap(self.pixmap_username.scaledToWidth(
        #     32, QtCore.Qt.TransformationMode.SmoothTransformation))
        qlabelpixamap.setContentsMargins(100, 100, 100, 100)
        qlabelpixamap.setStyleSheet(
            "QLabel { padding: 50px; background-color: rgba(0,0,0,0); border-radius:10px;}")
        qlabelpixamap.setCursor(Qt.CursorShape.PointingHandCursor)
        # abajo enviamos un evento al qlabelpixamap
        qlabelpixamap.label_enter_event_first()
        # This is the last message
        self.qlabelpixamap = qlabelpixamap
        self.pixmaps_profiles_array.append(qlabelpixamap)
        # repintamos la imagen
        self.qlabelpixamap.repaint()
        # self.chat_widget.profile_image = self.pixmap_username #does not exist  pixmapusername before
        self.chat_widget.__init__(self)
        if message:
            self.counter_messages += 1

            if len(self.all_messages) < 1:
                # self.all_messages.append([self.image_pixmap_1, message])
                # self.all_messages2.append(message)
                qlabel_message = QLabelMessage()
                qlabel_message.setWordWrap(True)
                qlabel_message.setText(message)
                qlabel_message.setTextInteractionFlags(
                    Qt.TextInteractionFlag.TextSelectableByMouse)
                # qlabel_message.setStyleSheet(
                #     "QLabel { background-color: rgba(0,0,0,0); border-radius:0px;padding:\
                #     0px; margin: 0px; font: bold 10pt 'MS Shell Dlg 2';color: white;}")
                # Allow vertical expansion
                size_policy = QSizePolicy(
                    QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                qlabel_message.setSizePolicy(size_policy)

                horizontal_layout = QHBoxLayout()

                image_pixmap_1 = self.qlabelpixamap

                horizontal_layout.addWidget(image_pixmap_1)
                horizontal_layout.addWidget(qlabel_message)
                horizontal_layout.setGeometry(QtCore.QRect(10, 10, 550, 60))

                self.container_layout.addLayout(horizontal_layout)

            else:
                print('ELSEEEEEEEEEEEEEE')
                # self.all_messages.pop(0)
                # self.all_messages.append([self.image_pixmap_1, message])
                self.all_messages2.append(message)
                # self.labels['msg'].setText('\n'.join(self.all_messages2))

                qlabel_message = QLabel(self)
                qlabel_message.setWordWrap(True)
                qlabel_message.setText(message)
                qlabel_message.setTextInteractionFlags(
                    Qt.TextInteractionFlag.TextSelectableByMouse)

                # qlabel_message.setStyleSheet(
                #     "QLabel {;padding:\
                #     0px; margin: 0px; font: bold 10pt 'MS Shell Dlg 2';color: black;}")

                horizontal_layout = QHBoxLayout()
                image_pixmap_1 = self.qlabelpixamap

                # horizontal_layout.addWidget(pixmap_username)
                horizontal_layout.addWidget(qlabel_message)
                horizontal_layout.setGeometry(QtCore.QRect(10, 10, 550, 60))
                # horizontal_layout.setContentsMargins(0, 0, 0, 10)
                self.container_layout.addLayout(horizontal_layout)
                # self.messages_images_layout.setAlignment(
                #     Qt.AlignmentFlag.AlignCenter)
            # Agregar al contenedor principal

            # for elem in self.pixmaps_profiles_array:
            #     elem.signal_profile_picture_clicked.connect(
            #         self.chat_widget.show_profile)
            self.pixmaps_profiles_array[-1].signal_profile_picture_clicked.connect(
                self.background_widget.show_profile)
            self.pixmaps_profiles_array[-1].signal_profile_picture_clicked.connect(
                self.chat_widget.show_profile)
            self.background_widget.signal_profile_close.connect(
                self.chat_widget.hide)
            # self.container_widget.setFixedSize(
            #     256, 500+132*self.counter_messages*0)
            # self.scroll_area.setFixedSize(
            #     600, 500+132*self.counter_messages)

            # Permitir que la interfaz gráfica de usuario (GUI) se actualice
            QCoreApplication.processEvents()

            # Después de inicializar el QScrollArea
            scroll_bar = self.scroll_area.verticalScrollBar()

            # Set the scrollbar value directly to the maximum
            scroll_bar.setValue(scroll_bar.maximum())
            # ASEGURAMOS QUE ESTE EN UN VALOR
            scroll_bar.setValue(800)

            # Print some information for debugging
            print('Scroll Bar Value After:', scroll_bar.value())

            # Permitir que la interfaz gráfica de usuario (GUI) se actualice nuevamente
            QCoreApplication.processEvents()

    def init_gui(self) -> None:
        # Window Geometry
        self.setGeometry(100, 200, 1200, 900)
        # Grid Layout
        self.grid = QGridLayout()
        # Labels
        self.labels = {}
        self.labels['username'] = QLabel(f'Welcome {self.username}', self)
        self.labels['username'].setStyleSheet(login_label_ok)
        self.labels['username'].setFixedSize(550, 60)
        self.labels['username'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['username'].repaint()

        # # QLabel image assignation
        # window_size = self.size()
        # self.labels['label_image'] = QLabel(self)
        # self.labels['label_image'].setMaximumSize(window_size)
        # self.labels['label_image'].setGeometry(0, 0, 300, 300)
        # self.labels['label_image'].setAlignment(
        #     QtCore.Qt.AlignmentFlag.AlignCenter)

        # self.labels['username_status'] = QLabel('', self)
        # self.labels['username_status'].setStyleSheet(login_label)
        # self.labels['username_status'].setAlignment(
        #     QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.labels['username_status'].repaint()

        # # Message Label
        # self.labels['msg'] = QLabel('MESSAGES:', self)
        # self.labels['msg'].setStyleSheet(login_label)
        # self.labels['msg'].setStyleSheet(login_label_ok)
        # self.labels['msg'].setAlignment(
        #     QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.labels['msg'].repaint()

        # Write a message
        # self.write_message = QLineEdit(self)
        # self.write_message.setStyleSheet(login_label)
        self.write_message = QLineEdit(self)
        self.write_message.setStyleSheet(InputFieldStyle)
        self.write_message.setFixedSize(550, 60)
        self.write_message.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.write_message.setPlaceholderText('Write a message...')
        self.write_message.setStyleSheet(
            "QLineEdit { background-color: rgba(255,255,255,0.25); border-radius:0px;padding:\
            0px; margin: 0px; font: bold 15pt 'MS Shell Dlg 2';color: white;}")
        self.write_message.repaint()
        self.all_messages = []
        self.all_messages2 = []

        for _ in range(5):
            self.all_messages2.append('')
        # self.labels['msg'].setText('\n'.join(self.all_messages))

        # All the messages will be stored in a list of tuples (image,username,message)

        # for _ in range(5):
        #     self.all_messages.append([self.image_pixmap_1, ''])
        # self.labels['msg'].setText('\n'.join(self.all_messages2))

        # Crear un layout horizontal
        self.messages_images_layout = QVBoxLayout()
        self.messages_images_layout.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.labels['username'])
        self.labels['username'].setScaledContents(True)

        # second
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.write_message)

        # Create a scroll area and the container
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Create a widget to contain the layout
        self.container_widget = QWidget(self.scroll_area)
        self.scroll_area.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0.2); color: white;")
        self.container_layout = QVBoxLayout(self.container_widget)
        # Set the container widget as the scroll area's widget
        self.scroll_area.setWidget(self.container_widget)
        self.scroll_area.setWidgetResizable(True)

        self.container_widget.setMinimumHeight(500)
        self.scroll_area.setMinimumHeight(500)
        self.scroll_area.setMaximumHeight(500)
        self.scroll_area.setMaximumHeight(500)

        self.scroll_area.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.container_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # self.container_widget.setLayout(self.container_layout)
        # self.container_layout.addLayout(messages_layout)
        # messages_layout = QVBoxLayout()
        # # Add your existing self.messages_images_layout to the messages_layout
        # messages_layout.addLayout(self.messages_images_layout)

        # Vertical
        vbox = QVBoxLayout()
        vbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.scroll_area)
        vbox.addLayout(hbox2)
        # vbox.addWidget(self.container_widget)
        vbox.addStretch(2)
        # vbox.addWidget(self.labels['username_status'])
        # self.labels['username_status'].setScaledContents(True)
        # self.labels['username_status'].setAlignment(
        #     QtCore.Qt.AlignmentFlag.AlignCenter)

        # vbox.addWidget(self.labels['image_input'])
        vbox.addStretch(5)
        self.setLayout(vbox)
