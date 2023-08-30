import sys
from PyQt6.QtWidgets import (QPushButton)


class Button(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.counter_clicks = 0
        self.resize(self.sizeHint())
        self.move(*pos)
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.counter_clicks += 1
        print(f'Button {self.name} clicked {self.counter_clicks} times.')


class Register_Button(QPushButton):
    def __init__(self, name: str, pos: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.counter_clicks = 0
        self.resize(self.sizeHint())
        self.setGeometry(300, 250, 400, 150)
        self.move(*pos)
        self.clicked.connect(self.button_clicked)
        self.status = False  # Has been clicked?

    def button_clicked(self):
        print('Register button pressed!')

        return self.status
