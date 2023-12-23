from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QLabel
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QHBoxLayout
from PIL import Image
import numpy as np
from PyQt6.QtGui import QPainter, QColor


class QLabel_Exit(QLabel):
    signal_profile_close = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setPixmap(QPixmap('images/undo64.png'))
        # hacemos que cuando hagamos click en qlabelpixamap, se envie un evento
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedHeight(64)
        self.setFixedWidth(64)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet(
            'background-color: rgba(0,0,0,0); border: 0px solid rgba(0,0,0,0)')
        # Definimos una función para manejar el evento de clic del mouse

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Acciones a realizar cuando se hace clic izquierdo
            self.signal_profile_close.emit()


def center_window(frame_to_center) -> None:
    '''This function does not works properly, it needs to be fixed, error example:
    QWindowsWindow::setGeometry: Unable to set geometry 1280x764+320+141 (frame: 1296x803+312+110) 
    on QWidgetWindow/"Frame1ClassWindow" on "{{{MONITOR_MODEL}}}". 
    Resulting geometry: 1280x797+320+141 (frame: 1296x836+312+110) 
    margins: 8, 31, 8, 8 minimum size: 349x764 MINMAXINFO(maxSize=POINT(x=0, y=0),
    maxpos=POINT(x=0, y=0), maxtrack=POINT(x=0, y=0), mintrack=POINT(x=365, y=803)))
    '''
    # Principal monitor dimensions
    try:
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        # Monitor dimensions
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # # calculate the center of the screen
        # x_position = (screen_width - frame_to_center.width()) // 2
        # y_position = (screen_height - frame_to_center.height()) // 2

        # # Stablish the frame position in the center of the screen
        # frame_to_center.setGeometry(x_position, y_position, 1280, 720)

        frame_to_center.setGeometry(0, 0, int(screen_width * 0.6),
                                    int(screen_height*0.6))
        frame_to_center.move(int(screen_width)-int(frame_to_center.width()*1.3),
                             int(screen_height)-int(frame_to_center.height()*1.5))

    except Exception as e:
        print("Error centering window:", str(e))
