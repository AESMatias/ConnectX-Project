from PyQt6.QtGui import QIcon, QGuiApplication


def center_window(frame_to_center) -> None:
    # Principal monitor dimensions
    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.geometry()

    # Monitor dimensions
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    # calculate the center of the screen
    x_position = (screen_width - frame_to_center.width()) // 2
    y_position = (screen_height - frame_to_center.height()) // 2

    # Stablish the frame position in the center of the screen
    frame_to_center.setGeometry(x_position, y_position, 800, 600)
