from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QHBoxLayout
from PIL import Image
import numpy as np


class MessagesBoxWidget(QWidget):
    def __init__(self, parent=None, username=None):
        super().__init__(parent, flags=Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.username = username
        self.setWindowTitle("Mesages Frame")
        self.profile_image = QPixmap(f'profiles/images/{self.username}.png')
        # This is the average color of the image
        image_array = self.load_image(f'profiles/images/{self.username}.png')
        average_color = self.get_average_color(image_array)
        # Makes the background transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.username_label = QLabel(self.username)
        self.username_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_label.setStyleSheet(
            'color: white;text-align: center;font: 75 25pt "MS Shell Dlg 2";')
        self.add_friend = QPushButton("Friend Request")
        self.add_friend.setStyleSheet(f'QPushButton {{ \
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
            stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
            stop:1 rgba({average_color[0]}, {average_color[1]}, {average_color[2]}, 1)); \
            color: white; font: bold 12pt "MS Shell Dlg 2";border:1px solid black;border-radius:2px;}} \
            QPushButton:pressed {{color: rgb(0, 0, 0); background-color: white;}}')
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
            color: white; font: bold 12pt "MS Shell Dlg 2"; border:1px solid black;border-radius:2px;}} \
            QPushButton:pressed {{color: rgb(0, 0, 128); background-color: white;}}')
        self.send_message.setFixedHeight(30)
        self.add_friend.setFixedHeight(30)
        # Create a container widget for the layout
        container_widget = QWidget(self)
        container_widget.setGeometry(0, 0, 320, 400)

        container_widget.setStyleSheet(
            f'background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \
                stop:0 rgba({average_color[0]-40}, {average_color[1]-40}, {average_color[2]-40}, 1), \
                    stop:1 rgba({average_color[0]+20}, {average_color[1]+20}, {average_color[2]+20}, 1)); \
    border: 1px solid white; border-radius: 2px;')
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
        self.setGeometry(150, 100, 400, 320)
        self.animation_steps = 100
        self.animation_steps_close = 100
        self.current_step = 0
        self.current_step_close = 0
        self.timer_expand_animation = QtCore.QTimer(self)
        self.timer_expand_animation.timeout.connect(self.animate_size_start)
        self.timer_close_animation = QtCore.QTimer(self)
        self.timer_close_animation.timeout.connect(self.animate_size_close)

    def change_pixmap(self, username: str):
        ''' TODO AQUI LA IDEA ES DE ALGUNA FORMA CAMBIAR EL PIXMAP CADA VEZ QUE
        LLEGUE UN NUEVO MENSAJE, PERO DESDE FUERA NO SE PUEDE ACTUALIZAR
        NI TAMPOCO LLAMANDO A ESTA FUNCION (podría probarse haciendo .self de las variables de __init__)
        ASI QUE LA SOLUCION MAS FACTIBLE PARECE SER INGRESAR A ESTA INSTANCIA EL NOMBRE DE USUARIO
        Y MANEJARLO DIRECTAMENTE DESDE AQUI, PARA QUE EN CADA NUEVO MENSAJE SE INSTANCIE UN NUEVO OBJETO DE ESTE TIPO
        Y SE PUEDA ENLAZAR CON CIERTA LAYOUT HORIZONTAL QUE COMPONE CADA MENSAJE.
        RECORDAR QUE LUEGO DE CREARSE LA INSTANCIA DEBE ENLAZARSE  AL self.pixmaps_profiles_array del frame CHAT.
        '''
        path_username = f'profiles/images/{username}.png'
        self.profile_image = QPixmap(path_username)
        self.update()
        print('CHANGING PIXMAP AT ChatWidget.change_pixmap method!')

    def show_profile(self):
        self.show()
        self.raise_()
        self.timer_expand_animation.start(1)

    def hide_profile(self):
        self.timer_close_animation.start(2)

    def animate_size_start(self):
        self.current_step += 1
        if self.current_step <= self.animation_steps:
            factor = 1.0 + self.current_step / self.animation_steps * 0.6
            scaled_width = int(25 * factor*8)
            scaled_height = int(125 * factor*2)
            # self.setFixedSize(scaled_width, scaled_height)
            # Expanding the pixmap as well
            # self.setGeometry(self.current_step,
            #                  self.current_step, scaled_width, scaled_height)
            self.setGeometry(0+self.current_step, 0 +
                             self.current_step, scaled_width, scaled_height)
            # self.setGeometry(400, 80, scaled_width, scaled_height)
        else:
            self.current_step = 0
            print(self.height(), self.width())
            self.timer_expand_animation.stop()

    def animate_size_close(self):
        self.current_step_close += 1
        if self.current_step_close <= self.animation_steps_close:
            factor = 1.0 - self.current_step / self.animation_steps_close * 0.6
            scaled_width = int(25 * factor*8)
            scaled_height = int(125 * factor*2)
            # self.setFixedSize(scaled_width, scaled_height)
            # Expanding the pixmap as well
            self.setGeometry(self.current_step_close*10,
                             self.current_step_close*3, scaled_width+30, scaled_height+10)
        else:
            self.current_step_close = 0
            print(self.height(), self.width())
            self.timer_close_animation.stop()
            self.hide()

    def load_image(self, image_path):
        # TODO We need to check if the image exists and retrieve it from the cache
        # if the image does not exist, we return a default image
        try:
            image = Image.open(image_path)
            return np.array(image)
        except:
            return np.array(Image.open('images/profile_image.png'))

    def get_average_color(self, image_array):
        average_color = np.mean(image_array, axis=(0, 1)).astype(int)
        return average_color
