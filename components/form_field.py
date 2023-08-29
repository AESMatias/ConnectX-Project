import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout, QLineEdit)


class FormField(QHBoxLayout):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)

        label = QLabel(f"{text}: ")
        campo = QLineEdit("")

        self.addStretch(1)
        self.addWidget(label)
        self.addWidget(campo)
        self.addStretch(1)


class Form(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Form")
        self.setGeometry(200, 200, 400, 400)
        container = QVBoxLayout()
        container.addLayout(FormField("Username"))
        self.setLayout(container)
        self.show()
