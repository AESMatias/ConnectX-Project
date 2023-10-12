from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
import os
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt


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

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked_signal.emit('musicButton')

            if self.music_status == True:
                self.music_status = False
            elif self.music_status == False:
                self.music_status = True
