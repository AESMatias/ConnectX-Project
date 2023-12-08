from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout


class ChatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Chat Flotante")
        # Hace que el fondo sea transparente
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Contenido del chat"))
        self.setLayout(layout)


class QLabelProfilePicture(QLabel):
    def __init__(self):
        super().__init__()
        # Right Alignment
        self.setFixedSize(50, 50)
        self.original_size = self.sizeHint()
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enterEvent = self.label_enter_event
        self.leaveEvent = self.label_leave_event
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_start)
        self.animation_steps = 100
        self.current_step = 0
        self.original_pixmap = QPixmap('images/cara_blue.jpg')
        self.scaled_pixmap = None

    def label_enter_event(self, event):
        self.timer_expand_animation.start(2)
        event.accept()

    def label_leave_event(self, event):
        self.timer_expand_animation.stop()
        if self.scaled_pixmap is not None:
            self.setPixmap(self.scaled_pixmap)
        else:
            pixmap_scaled = self.original_pixmap.scaled(QtCore.QSize(
                32, 32), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.setPixmap(pixmap_scaled)
            event.accept()

    def animate_size_start(self):
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 + self.current_step / self.animation_steps * 0.3
            scaled_width = int(self.original_size.width() * factor)
            scaled_height = int(self.original_size.height() * factor)
            # self.setFixedSize(scaled_width, scaled_height)
            # Expanding the pixmap as well
            pixmap_scaled = self.original_pixmap.scaled(QtCore.QSize(
                scaled_width, scaled_height), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.setPixmap(pixmap_scaled)
            # print("Current size of the pixmap:", self.pixmap().size())
        else:
            # print("Current size of the pixmap:", self.pixmap().size())
            self.current_step = 0
            self.timer_expand_animation.stop()
