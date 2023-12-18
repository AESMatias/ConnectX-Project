from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
import os
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QTimer
import webbrowser


class MusicButton(QLabel):
    clicked_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('background:none')
        self.music_status = True
        self.name = 'musicButton'
        self.dir = os.path.join('images', 'volume.png')
        self.dir_muted = os.path.join('images', 'volume_muted.png')
        self.pixmap = QPixmap(self.dir)
        self.pixmap_muted = QPixmap(self.dir_muted)
        self.animation_duration = 200  # in milliseconds
        self.animation_steps = 30
        self.current_step = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.icon_pressed_animation)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked_signal.emit('musicButton')

            if self.music_status == True:
                # Si la música está activada, desactivarla y aplicar la animación de opacidad
                self.music_status = False
                self.setPixmap(self.pixmap_muted)
                self.current_opacity = 1.0
            elif self.music_status == False:
                # Si la música está desactivada, activarla y aplicar la animación de opacidad
                self.music_status = True
                self.setPixmap(self.pixmap)
                self.current_opacity = 0.4

            self.current_step = 0
            self.timer.start(self.animation_duration // self.animation_steps)

    def icon_pressed_animation(self):
        if self.current_step <= self.animation_steps:
            opacity_step = (0.4 - 1.0) / self.animation_steps
            self.current_opacity += opacity_step
            transparent_pixmap = self.change_pixmap_opacity(
                self.pixmap if self.music_status else self.pixmap_muted, self.current_opacity)
            self.setPixmap(transparent_pixmap)
            self.current_step += 1
        else:
            # Detener el temporizador cuando se completa la animación
            self.timer.stop()

    def change_pixmap_opacity(self, pixmap, opacity):
        result_pixmap = QPixmap(pixmap.size())
        result_pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(result_pixmap)
        if self.music_status == False:
            painter.setOpacity(opacity)
        elif self.music_status == True:
            painter.setOpacity(0.4 + self.current_step*1.3/100)
        print(self.current_step)

        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return result_pixmap


class ConnectXLogo(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('background:none')
        self.name = 'musicButton'
        self.dir = os.path.join('images', 'logo512.png')
        self.pixmap = QPixmap(self.dir).scaled(
            200, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.animation_duration = 500  # in milliseconds
        self.animation_steps = 30
        self.current_step = 0
        self.timer = QTimer(self)
        self.cycle_timer = QTimer(self)
        self.cycle_timer.timeout.connect(self.cycle_opacity)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.counter_inf_cycle = 0
        # Configuración inicial de opacidad
        self.current_opacity = 1.0
        self.setPixmap(self.pixmap)
        # Iniciar el temporizador de ciclo cada 5 segundos
        self.cycle_timer.start(30)
        # Iniciar el cambio de opacidad al instanciar el objeto
        self.timer.start(self.animation_duration // self.animation_steps)
        self.timer.stop()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.open_link()

    def open_link(self):
        link_to_open = "https://github.com/AESMatias/ConnectX-Project"
        webbrowser.open(link_to_open)

    def change_pixmap_opacity(self, pixmap, opacity):
        result_pixmap = QPixmap(pixmap.size())
        result_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(result_pixmap)
        if painter.isActive():
            painter.end()

        painter.begin(result_pixmap)
        painter.setOpacity(opacity)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return result_pixmap

    def cycle_opacity(self):
        if self.counter_inf_cycle >= 0:
            self.current_opacity -= 0.01
            transparent_pixmap = self.change_pixmap_opacity(
                self.pixmap, self.current_opacity)
            self.setPixmap(transparent_pixmap)
            self.counter_inf_cycle += 1
            if self.counter_inf_cycle == 70:
                self.counter_inf_cycle = -70
        elif self.counter_inf_cycle <= 0:
            self.current_opacity += 0.01
            transparent_pixmap = self.change_pixmap_opacity(
                self.pixmap, self.current_opacity)
            self.setPixmap(transparent_pixmap)
            self.counter_inf_cycle += 1
            if self.counter_inf_cycle == 70:
                self.counter_inf_cycle = 0

        # Reiniciar el temporizador de animación cada vez que se completa el ciclo
        self.timer.start(self.animation_duration // self.animation_steps)

        # Actualizar la opacidad del pixmap directamente
        transparent_pixmap = self.change_pixmap_opacity(
            self.pixmap, self.current_opacity)
        self.setPixmap(transparent_pixmap)
