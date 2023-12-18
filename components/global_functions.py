from PyQt6.QtGui import QGuiApplication


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
