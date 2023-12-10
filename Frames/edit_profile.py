from PyQt6.QtCore import QStandardPaths
import requests
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtWidgets
from io import BytesIO
from PyQt6 import QtCore
from PyQt6.QtWidgets import QStackedLayout, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap, QCursor
from components.buttons import EditProfileButton, Upload_file
from Frames.change_profile_pic import ChangeAvatar
from styles.styles import button_style, edit_profile_button, edit_profile_button_clicked
from components.input_user import ImageViewer
image_florence = 'images/florence.jpg'
aristotle_1 = 'images/aristotle_1.jpg'


class EditProfile(QWidget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.username = ''
        self.init_gui()

    def open_file(self) -> None:
        initial_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DocumentsLocation)
        self.upload_qfile = QFileDialog.getOpenFileName(
            self, 'Upload image', initial_dir, 'All files (*)')
        if self.upload_qfile:
            print(f'Selected file: {self.upload_qfile}')
            dir_image = self.upload_qfile[0]
            image_pixmap = QPixmap(dir_image)

            self.labels['label_image'].setPixmap(image_pixmap)
            self.labels['label_image'].setScaledContents(True)
            self.labels['label_image'].setGeometry(200, 200, 300, 300)
            self.labels['label_image'].setAlignment(
                QtCore.Qt.AlignmentFlag.AlignCenter)
            self.labels['label_image'].show()
            image = image_pixmap.toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)
            image.save(buffer, "PNG")
            image_bytes = buffer.data()
            url = 'http://localhost:8000/uploadimagen/'
            files = {'files': ('blob', BytesIO(image_bytes))}
            response = requests.post(url, files=files)
            print(f'Response from server: {response.json()}')

    def change_profile_pic(self) -> None:
        change_avatar_frame = ChangeAvatar(self)
        change_avatar_frame.show()

    def init_gui(self) -> None:
        window_size = self.size()
        self.labels = {}
        self.setGeometry(100, 200, 500, 600)
        self.setWindowTitle(f'ConectX Project - {self.username}')

        # QLabel image assignation
        window_size = self.size()
        self.labels['label_image'] = QLabel(self)
        self.labels['label_image'].hide()
        self.labels['label_image'].setMaximumSize(window_size)
        self.labels['label_image'].setGeometry(0, 0, 0, 0)
        self.labels['label_image'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        # Upload profile image
        self.image_viewer = ImageViewer()
        # self.upload_image = Upload_file(
        #     'uploadButton', (300, 250), 'Change profile picture', self)
        # self.upload_image.setCursor(
        #     QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        # self.upload_image.setStyleSheet(
        #     button_style)
        # self.upload_image.clicked.connect(self.open_file)
        # self.upload_image.clicked.connect(self.change_profile_pic)

        # 1 Button
        self.stack_button1 = EditProfileButton(
            'logoutnButton', 0, 'Profile', self)
        self.stack_button1.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button1.setStyleSheet(
            edit_profile_button)
        self.stack_button1.setStyleSheet(edit_profile_button_clicked)
        # 1 Layout
        # QLabel image assignation
        self.labels['label_image1'] = QLabel(self)
        self.labels['label_image1'].setMaximumSize(window_size)
        self.labels['label_image1'].setGeometry(50, 50, 300, 300)
        self.labels['label_image1'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = image_florence
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image1'].setPixmap(image_pixmap)
        self.labels['label_image1'].setMaximumSize(window_size)
        self.labels['label_image1'].setScaledContents(True)
        self.labels['label_image1'].setGeometry(200, 200, 300, 300)
        self.labels['label_image1'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image1'].show()
        # 2 Button
        self.stack_button2 = EditProfileButton(
            'logoutnButton', 1, 'Contacts', self)
        self.stack_button2.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button2.setStyleSheet(
            edit_profile_button)
        # 2 Layout
        # QLabel image assignation
        self.labels['label_image2'] = QLabel(self)
        self.labels['label_image2'].setMaximumSize(window_size)
        self.labels['label_image2'].setGeometry(50, 50, 300, 300)
        self.labels['label_image2'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image2 = aristotle_1
        image_pixmap = QPixmap(dir_image2)
        self.labels['label_image2'].setPixmap(image_pixmap)
        self.labels['label_image2'].setScaledContents(True)
        self.labels['label_image2'].setGeometry(200, 200, 300, 300)
        self.labels['label_image2'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image2'].show()
        # 3 Button
        self.stack_button3 = EditProfileButton(
            'logoutnButton', 2, 'Messages', self)
        self.stack_button3.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button3.setStyleSheet(
            edit_profile_button)
        # 3 Layout
        # QLabel image assignation
        self.labels['label_image3'] = QLabel(self)
        self.labels['label_image3'].setMaximumSize(window_size)
        self.labels['label_image3'].setGeometry(50, 50, 300, 300)
        self.labels['label_image3'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = image_florence
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image3'].setPixmap(image_pixmap)
        self.labels['label_image3'].setScaledContents(True)
        self.labels['label_image3'].setGeometry(200, 200, 300, 300)
        self.labels['label_image3'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image3'].show()
        # 4 Button
        self.stack_button4 = EditProfileButton(
            'logoutnButton', 3, 'Advanced', self)
        self.stack_button4.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button4.setStyleSheet(
            edit_profile_button)
        # 4 Layout
        # QLabel image assignation
        self.labels['label_image4'] = QLabel(self)
        self.labels['label_image4'].setMaximumSize(window_size)
        self.labels['label_image4'].setGeometry(50, 50, 300, 300)
        self.labels['label_image4'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image2 = aristotle_1
        image_pixmap = QPixmap(dir_image2)
        self.labels['label_image4'].setPixmap(image_pixmap)
        self.labels['label_image4'].setScaledContents(True)
        self.labels['label_image4'].setGeometry(200, 200, 300, 300)
        self.labels['label_image4'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image4'].show()
        # 5 Button
        self.stack_button5 = EditProfileButton(
            'logoutnButton', 4, 'Security', self)
        self.stack_button5.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stack_button5.setStyleSheet(
            edit_profile_button)
        # 5 Layout
        # QLabel image assignation
        self.labels['label_image5'] = QLabel(self)
        self.labels['label_image5'].setMaximumSize(window_size)
        self.labels['label_image5'].setGeometry(50, 50, 300, 300)
        self.labels['label_image5'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        dir_image = image_florence
        image_pixmap = QPixmap(dir_image)
        self.labels['label_image5'].setPixmap(image_pixmap)
        self.labels['label_image5'].setScaledContents(True)
        self.labels['label_image5'].setGeometry(200, 200, 300, 300)
        self.labels['label_image5'].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labels['label_image5'].show()

        # Buttons Grouped
        self.buttons_grouped = QHBoxLayout()
        self.buttons_grouped.addWidget(self.stack_button1)
        self.buttons_grouped.addWidget(self.stack_button2)
        self.buttons_grouped.addWidget(self.stack_button3)
        self.buttons_grouped.addWidget(self.stack_button4)
        self.buttons_grouped.addWidget(self.stack_button5)

        page1_layout = QHBoxLayout()
        page1_layout.addWidget(self.labels['label_image1'])
        page1_layout.addWidget(self.image_viewer)
        # page1_layout.addWidget(self.upload_image)
        self.labels['label_image']
        page1_layout.addWidget(self.labels['label_image'])
        container1 = QWidget()
        container1.setLayout(page1_layout)

        page2_layout = QVBoxLayout()
        page2_layout.addWidget(self.labels['label_image2'])
        container2 = QWidget()
        container2.setLayout(page2_layout)

        page3_layout = QVBoxLayout()
        page3_layout.addWidget(self.labels['label_image3'])
        container3 = QWidget()
        container3.setLayout(page3_layout)

        page4_layout = QVBoxLayout()
        page4_layout.addWidget(self.labels['label_image4'])
        container4 = QWidget()
        container4.setLayout(page4_layout)

        page5_layout = QVBoxLayout()
        page5_layout.addWidget(self.labels['label_image5'])
        container5 = QWidget()
        container5.setLayout(page5_layout)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container1)
        self.stacked_layout.addWidget(container2)
        self.stacked_layout.addWidget(container3)
        self.stacked_layout.addWidget(container4)
        self.stacked_layout.addWidget(container5)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.buttons_grouped)
        main_layout.addLayout(self.stacked_layout)
        self.setLayout(main_layout)
        self.setStyleSheet(f"""
            QWidget {{
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                            stop: 0 1, stop: 1 #000DFF);
            }}
            """)

    def change_page(self):
        sender = self.sender()
        self.stacked_layout.setCurrentIndex(sender.index)
        self.stack_button1.setStyleSheet(edit_profile_button)
        self.stack_button2.setStyleSheet(edit_profile_button)
        self.stack_button3.setStyleSheet(edit_profile_button)
        self.stack_button4.setStyleSheet(edit_profile_button)
        self.stack_button5.setStyleSheet(edit_profile_button)
        for i in range(5):
            if i == sender.index:
                sender.setStyleSheet(edit_profile_button_clicked)
