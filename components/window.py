import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton)


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()

    def init_gui(self):
        self.setGeometry(200, 200, 120, 120)
        self.setMaximumHeight(120)
        self.setMaximumWidth(120)
        # self.boton_1 = Button('Botón 1', (10, 20), 'Aprétame', self)
        # self.boton_2 = Button('Botón 2', (10, 60), 'Aprétame', self)
