import os
from utils.AristotleQuotes_ES import generate_quote
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QPalette, QBrush, QIcon, QGuiApplication, QPixmap, QCursor, QFont
from components.buttons import Register_Button, Login_Button, InputField
from styles.styles import quote_style, InputFieldStyle, tag, button_style, login_label, login_label_wrong, login_label_ok
from components.global_functions import center_window
from components.qlabels import MusicButton, ConnectXLogo


class Frame1(QWidget):
    signal_frame1 = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # Monitor dimensions
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
    # def closeEvent(self, event):
    #     print("Closing the main window")
    #     # Then, before closing the window, we need to close the sockets and threads
    #     self.signal_frame1.emit('close')
    #     self.client_thread.join()
        # Crear un QPalette personalizado con la imagen de fondo

    def volume_icon_change(self):
        sender = self.sender()
        if sender.music_status == True:
            print(sender.music_status, 'music status')
            self.volume_label.setPixmap(self.volume_label.pixmap_muted)
            self.repaint()
        elif sender.music_status == False:
            print(sender.music_status, 'music status')
            self.volume_label.setPixmap(self.volume_label.pixmap)
            self.repaint()

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Return or event.key() == 16777220:
            self.login_button.click()

    def remove_registered_label(self):
        sender = self.sender()
        if sender.register_status == False and sender.name == 'logoutnButton':
            self.labels['registered_status'].setText(
                '')
            self.labels['registered_status'].setStyleSheet(login_label)
            self.labels['registered_status'].repaint()  # To avoid bugs

            self.labels['username_status'].setText('')
            self.labels['username_status'].setStyleSheet(login_label)
            self.labels['username_status'].repaint()  # To avoid bugs

        if sender.login_status == False and sender.name == 'loginButton':
            self.labels['username_status'].setText('Invalid credentials')
            self.labels['username_status'].setStyleSheet(login_label_wrong)
            self.labels['username_status'].repaint()  # To avoid bugs
            self.labels['registered_status'].setText('')
            self.labels['registered_status'].setStyleSheet(login_label)

    def change_username_status(self):
        sender = self.sender()
        if sender.login_status == False:
            self.labels['username_status'].setText('Invalid credentials')
            self.labels['username_status'].setStyleSheet(login_label_wrong)
            self.labels['username_status'].repaint()  # To avoid bugs
            self.labels['registered_status'].setText('')
            self.labels['registered_status'].setStyleSheet(login_label)
        elif sender.login_status == True:
            self.labels['registered_status'].setText(
                'You have been registered')
            self.labels['registered_status'].setStyleSheet(login_label_ok)
            self.labels['registered_status'].repaint()  # To avoid bugs

    def show_register_status(self):
        sender = self.sender()
        if sender.register_status == False:
            self.labels['registered_status'].setText(
                'The user already exists')
            self.labels['registered_status'].setStyleSheet(login_label_wrong)
            self.labels['registered_status'].repaint()  # To avoid bugs
            sender.register_status = False
        elif sender.register_status == True:
            self.labels['registered_status'].setText(
                'You have been registered')
            self.labels['registered_status'].setStyleSheet(login_label_ok)
            self.labels['registered_status'].repaint()  # To avoid bugs
            sender.register_status = False

    def init_gui(self) -> None:
        # Window Geometry
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('ConectX Project')
        # Grid Layout
        self.grid = QGridLayout()
        # Labels
        self.labels = {}
        self.labels['username'] = QLabel('Username', self)
        self.labels['username'].setStyleSheet(tag)
        self.labels['password'] = QLabel('Password ', self)
        self.labels['password'].setStyleSheet(tag)
        self.labels['username_status'] = QLabel('', self)
        self.labels['username_status'].setStyleSheet(login_label)
        # registered status
        self.labels['registered_status'] = QLabel('', self)
        self.labels['registered_status'].setStyleSheet(login_label)
        self.labels['registered_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        self.username_field = InputField('username_field', '', self)
        self.username_field.setFixedSize(200, 40)
        self.username_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_field.setStyleSheet(InputFieldStyle)
        self.password_field = InputField('password_field', '', self)
        self.password_field.setFixedSize(200, 40)
        self.password_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password_field.setStyleSheet(InputFieldStyle)

        # Pixmap background
        background_image = QPixmap(os.path.join('images', '759324.png'))
        self.background_label = QLabel()
        self.background_label.setPixmap(background_image)
        self.background_label.setGeometry(
            0, 0, 800, 600)

        # Register
        self.register_button = Register_Button(
            'registerButton', (300, 250), 'REGISTER', self)
        self.register_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.register_button.setStyleSheet(button_style)
        # Login
        self.login_button = Login_Button(
            'loginButton', (300, 250), 'LOGIN', self)
        self.login_button.setStyleSheet(
            button_style)
        self.login_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_button.clicked.connect(self.change_username_status)

        # QLabel image assignation
        dir_image = os.path.join('images', 'logo512.png')
        image_pixmap = QPixmap(dir_image)
        image_pixmap = image_pixmap.scaled(
            200, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.labels['logo_welcome'] = ConnectXLogo(self)
        self.labels['logo_welcome'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['logo_welcome'].setPixmap(image_pixmap)
        self.labels['logo_welcome'].show()
        self.opacity_decimal = 9
        self.labels['logo_welcome'].setStyleSheet(
            'background:none;opacity:0.9')
        self.labels['logo_welcome'].setCursor(
            Qt.CursorShape.PointingHandCursor)
        # Volume label
        self.volume_label = MusicButton(self)
        self.volume_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.volume_label.setGeometry(1260-64, 780-64, 64, 64)
        self.volume_label.setStyleSheet(
            'background:none')
        self.volume_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        volume_pixmap = self.volume_label.pixmap
        self.volume_label.pixmap = volume_pixmap.scaled(
            64, 64, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.volume_label.setPixmap(volume_pixmap)
        self.volume_label.show()

        # Quote Label
        self.labels['quote_label'] = QLabel(self)
        self.labels['quote_label'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['quote_label'].setStyleSheet(quote_style)
        self.labels['quote_label'].setText(
            generate_quote()
            + '\n - Aristotle'
        )
        self.labels['quote_label'].setFont(QFont('Times', 20))
        self.labels['quote_label'].setWordWrap(True)

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.labels['username'])
        hbox1.addWidget(self.username_field)
        hbox1.addStretch(1)
       # Horizontal Layout 2
        hbox_pass = QHBoxLayout()
        hbox_pass.addStretch(1)
        hbox_pass.addWidget(self.labels['password'])
        hbox_pass.addWidget(self.password_field)
        hbox_pass.addStretch(1)
        # Second Horizontal Layout
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.login_button)
        hbox2.addStretch(1)
        # Third Horizontal Layout
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.register_button)
        hbox3.addStretch(1)
        # Third Horizontal Layout
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(self.labels['quote_label'])
        hbox4.addStretch(1)
        # Horizontal Layout logo+volume
        hbox5 = QHBoxLayout()
        hbox5.addStretch(13)
        hbox5.addWidget(self.labels['logo_welcome'])
        hbox5.addStretch(10)
        hbox5.addWidget(self.volume_label)
        hbox5.addStretch(1)

        # Vertical Layout
        vbox = QVBoxLayout()
        vbox.addSpacing(20)
        vbox.addLayout(hbox4)
        vbox.addSpacing(20)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox_pass)
        vbox.addSpacing(20)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addSpacing(20)
        vbox.addWidget(self.labels['username_status'])
        vbox.addSpacing(1)
        vbox.addWidget(self.labels['registered_status'])
        vbox.addSpacing(1)
        vbox.addSpacing(10)
        vbox.addLayout(hbox5)
        self.labels['username_status'].setScaledContents(True)
        self.labels['username_status'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addStretch(5)
        self.setLayout(vbox)
        center_window(self)
        self.show()
