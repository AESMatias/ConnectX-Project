import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout, QLineEdit)


class InputField(QLineEdit):
    def __init__(self, name: str, text: str, *args, **kwargs):
        super().__init__(text, *args, **kwargs)
        self.name = name
        self.text = ''
        self.textChanged.connect(self.change_text)

    def change_text(self, text_field: str):
        print('text changed at', text_field)
        self.text = text_field


# class FormField(QHBoxLayout):
#     def __init__(self, text, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         label = QLabel(f"{text}: ")
#         campo = QLineEdit("")

#         self.addStretch(1)
#         self.addWidget(label)
#         self.addWidget(campo)
#         self.addStretch(1)


# class Form(QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle("Form")
#         self.setGeometry(200, 200, 400, 400)
#         container = QVBoxLayout()
#         container.addLayout(FormField("Username"))
#         self.setLayout(container)
#         self.show()
