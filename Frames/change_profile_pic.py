import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import QFileDialog, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QBrush, QPalette, QPainter, QPixmap, QCursor
from components.buttons import Upload_file, Login_Button, Button, Chat_Button
from styles.styles import welcome_user_style, button_style, login_label, login_label_wrong, login_label_ok
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QAudio
from components.global_functions import center_window


class ChangeAvatar(QWidget):
    signal_change_avatar = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.username = ''
        self.setStyleSheet(f"""
            QWidget {{
                background-repeat: no-repeat;
                background-position: center;
                background-color: rgba(0, 0, 0, 128);  /* 128 es el valor de opacidad (0-255) */
            }}
        """)

    def init_gui(self) -> None:
        # Grid Layout
        self.grid = QGridLayout()
        # Labels
        self.labels = {}

        # QLabel image assignation
        window_size = self.size()
        self.labels['label_image'] = QLabel(self)
        self.labels['label_image'].hide()
        self.labels['label_image'].setMaximumSize(window_size)
        self.labels['label_image'].setGeometry(0, 0, 0, 0)
        self.labels['label_image'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addStretch(1)
        # Four
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addStretch(1)
        # Five CHAT
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addStretch(1)
        # Hbox6
        hbox6 = QHBoxLayout()
        hbox6.addStretch(1)
        hbox6.addWidget(self.labels['label_image'])
        hbox6.addStretch(1)
        # Vertical
        vbox = QVBoxLayout()
        vbox.addStretch(2)

        # Crear un QPalette personalizado con la imagen de fondo
        palette = QPalette()
        background_image = QPixmap('759324.jpg')
        brush = QBrush(background_image)
        palette.setBrush(QPalette.ColorRole.Window, brush)
        # Aplicar el QPalette al widget
        self.setPalette(palette)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        self.setLayout(vbox)
        self.show()
