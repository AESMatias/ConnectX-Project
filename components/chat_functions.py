import typing
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout


class ProfileViewBackground(QWidget):
    signal_profile_close = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Background Profile View")
        # Makes the background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setGeometry(-500, -500, 8000, 8000)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # REPLACE THIS WITH ADD BUTTON ETC
        # REPLACE THIS WITH ADD BUTTON ETC
        # REPLACE THIS WITH ADD BUTTON ETC
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(""))
        self.setLayout(layout)

        self.setStyleSheet('background-color: rgba(40, 40, 40, 200);')
        self.setStyleSheet(
            'background-color: red;')

    def show_profile(self):
        self.show()
        self.raise_()
        print(' show profileeeee de elem: ', self)

    def mousePressEvent(self, event) -> None:
        self.signal_profile_close.emit()
        self.hide()


class ChatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Chat Flotante")
        # Makes the background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("PROFILE VIEW QLABEL"))
        self.setLayout(layout)
        self.setGeometry(400, 80, 20, 120)
        self.animation_steps = 100
        self.current_step = 0
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_start)

    def show_profile(self):
        self.show()
        self.setStyleSheet(
            'background-color: rgba(0, 128, 0, 1); border: 1px solid red;')

        # self.background_widget.raise_()
        # self.background_widget.show()
        self.raise_()

        print(' show profileeeee de elem: ', self)
        self.timer_expand_animation.start(2)

    def animate_size_start(self):
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 + self.current_step / self.animation_steps * 0.6
            scaled_width = int(20 * factor*8)
            scaled_height = int(120 * factor*2)
            # self.setFixedSize(scaled_width, scaled_height)
            # Expanding the pixmap as well
            self.resize(scaled_width, scaled_height)
            # self.setGeometry(400, 80, scaled_width, scaled_height)
        else:
            self.current_step = 0
            self.timer_expand_animation.stop()


class QLabelProfilePicture(QLabel):
    signal_profile_picture_clicked = QtCore.pyqtSignal(str)

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

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            print("Clic izquierdo en el QLabel")
            self.signal_profile_picture_clicked.emit('press')

    def mouseReleaseEvent(self, event) -> None:
        # if event.button() == Qt.MouseButton.LeftButton:
        #     self.signal_profile_picture_clicked.emit('release')
        #     print("Soltar clic izquierdo en el QLabel")
        pass

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
