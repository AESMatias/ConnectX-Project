import typing
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QHBoxLayout, QGridLayout, QSizePolicy, QSpacerItem, QFrame, QScrollArea
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


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

        self.setStyleSheet('background-color: rgba(0, 0, 0, 0.8);')

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
        self.profile_image = QPixmap('images/profile_image.png')
        # This is the average color of the image
        image_array = self.load_image('images/profile_image.png')
        average_color = self.get_average_color(image_array)
        # Makes the background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.username_label = QLabel('Username')
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_label.setStyleSheet(
            'color: white;text-align: center;text-decoration: \
                underline;text-decoration-color: rgb(0, 0, 128)\
                ;font: 75 20pt "MS Shell Dlg 2";')
        self.add_friend = QPushButton("Friend Request")
        self.add_friend.setStyleSheet(f'QPushButton {{ \
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
            stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
            stop:1 rgba({average_color[0]}, {average_color[1]}, {average_color[2]}, 1)); \
            color: white; font: bold 10pt "MS Shell Dlg 2";}} \
            QPushButton:pressed {{color: rgb(0, 0, 128); background-color: white;}}')
        # self.add_friend.setStyleSheet(
        #     'QPushButton {color: white; background-color: rgba(0, 0, 128, 1);\
        #         solid black; font: bold 10pt "MS Shell Dlg 2";} \
        #     QPushButton:pressed {color: rgb(0, 0, 128); background-color: white;}')
        self.add_friend.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_message = QPushButton("Send Message")
        self.send_message.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_message.setStyleSheet(f'QPushButton {{ \
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
            stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
            stop:1 rgba({average_color[0]}, {average_color[1]}, {average_color[2]}, 1)); \
            color: white; font: bold 10pt "MS Shell Dlg 2";}} \
            QPushButton:pressed {{color: rgb(0, 0, 128); background-color: white;}}')

        # Create a container widget for the layout
        container_widget = QWidget(self)
        container_widget.setGeometry(0, 0, 256, 384)

        container_widget.setStyleSheet(
            f'background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
                stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
                    stop:1 rgba({average_color[0]+20}, {average_color[1]+20}, {average_color[2]+20}, 1)); \
    border: 1px solid black; border-radius: 2px;')

        # We make the layout
        layout = QVBoxLayout(container_widget)
        image_profile = QLabel('')
        # Quality: (0 means no compression, 100 is the best quality)
        scaled_image = self.profile_image.scaledToWidth(
            300, QtCore.Qt.TransformationMode.SmoothTransformation)
        image_profile.setPixmap(QtGui.QPixmap(scaled_image))
        image_profile.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_profile)
        layout.addWidget(self.username_label)
        # Horizontal box for add friend and send message buttons
        horizontal_box = QHBoxLayout()
        horizontal_box.addWidget(self.add_friend)
        horizontal_box.addWidget(self.send_message)
        layout.addLayout(horizontal_box)

        self.setLayout(layout)
        self.setGeometry(300, 80, 20, 120)
        self.animation_steps = 100
        self.current_step = 0
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_start)

    def show_profile(self):
        self.show()
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

    def load_image(self, image_path):
        image = Image.open(image_path)
        return np.array(image)

    def get_average_color(self, image_array):
        average_color = np.mean(image_array, axis=(0, 1)).astype(int)
        return average_color


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
        self.original_pixmap = QPixmap('images/profile_image.png').scaledToWidth(
            50, QtCore.Qt.TransformationMode.SmoothTransformation)
        self.scaled_pixmap = None

    def label_enter_event(self, event):
        self.timer_expand_animation.start(2)
        event.accept()

    def label_leave_event(self, event):
        self.timer_expand_animation.stop()
        if self.scaled_pixmap is not None:
            self.setPixmap(self.scaled_pixmap)
        else:
            # pixmap_scaled = self.original_pixmap.scaled(QtCore.QSize(
            #     32, 32), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.setPixmap(self.original_pixmap.scaledToWidth(
                32, QtCore.Qt.TransformationMode.SmoothTransformation))
            # self.setPixmap(pixmap_scaled)
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
        else:
            self.setPixmap(self.pixmap().scaledToWidth(
                70, QtCore.Qt.TransformationMode.SmoothTransformation))
            # print("Current size of the pixmap:", self.pixmap().size())
            self.current_step = 0
            self.timer_expand_animation.stop()


class QLabelMessage(QLabel):
    signal_profile_picture_clicked = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # Right Alignment
        self.original_size = self.sizeHint()
        self.enterEvent = self.label_enter_event
        self.leaveEvent = self.label_leave_event
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_start)
        self.timer_expand_animation.start(1)
        self.animation_steps = 100
        self.current_step = 0
        self.setStyleSheet(
            "QLabel {font: bold 0pt 'MS Shell Dlg 2'; background-color: rgba(0, 0, 0, 0);}")

    def label_enter_event(self, event):
        # self.timer_expand_animation.start(2)
        event.accept()

    def label_leave_event(self, event):
        pass
        # self.timer_expand_animation.stop()
        # if self.scaled_pixmap is not None:
        #     self.setPixmap(self.scaled_pixmap)
        # else:
        #     self.setPixmap(self.original_pixmap.scaledToWidth(
        #         32, QtCore.Qt.TransformationMode.SmoothTransformation))
        #     event.accept()

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            print("Text copied! -We need to add this funcionality- ")

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
            style_sheet = (
                "QLabel {"
                f"font: bold {4*factor*2}pt 'MS Shell Dlg 2';"
                "background-color: rgba(0, 0, 0, 0);"
                "}"
            )
            self.setStyleSheet(style_sheet)
        else:
            self.current_step = 0
            self.timer_expand_animation.stop()
