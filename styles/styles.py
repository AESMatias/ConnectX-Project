

quote_style = """
QLabel {
    color: white;
    background-color: rgba(0, 0, 0, 70);
    border: 2px solid black;
    padding: 10px;
    border-radius: 5px;
}
"""
welcome_user_style = """
QLabel {
    color: white;
    font-size: 40px;
    background-color: rgba(0, 0, 0, 100);
    border: 1px solid black;
    padding: 10px;
    border-radius: 2px;
    font-weight: bold;
}
"""

button_style = """
    QPushButton {
        border: 2px solid white;
        border-radius: 5px;
        font-size: 40px;
        font-weight: bold;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: qradialgradient(cx: 0.5, cy: 0.5, fx: 0.5, fy: 0.5, radius: 1, stop: 0 #0000FF, stop: 0.7 #0000AA, stop: 1 #000088);
    }
    
    QPushButton:hover {
        border: 2px solid white;
        border-radius: 5px;
        font-size: 38px;
        font-weight: bold;
        background: qradialgradient(cx: 0.5, cy: 0.5, fx: 0.5, fy: 0.5, radius: 1, stop: 0 #0000FF, stop: 1 #3333AA);
    }
    QPushButton:pressed {
        background: rgba(0,0,0,40);
        color: white;
        font-size: 30px;
        font-weight: bold;
        border: 1.5px solid white;
        border-radius: 6px;
}

"""

global_style = """
    QWidget {
        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                     stop: 0 #6B73FF, stop: 1 #000DFF);
    }
"""
# global_style_changed = """
#     QWidget {
#         background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
#                                      stop: 0 #6B73FF, stop: 1 #FFFFFF);
#     }
# """
login_label = """
    QLabel {
        opacity: 0.5;
        font-size: 30px;
        background: rgba(0,0,0,0);

    }
"""


tag = """
    QLabel {
        opacity: 0;
        font-size: 22px;
        background: rgba(0,0,0,0);
        color: white;
        font-weight: bold;
        border: 1.5px solid white;
        border-radius: 6px;
}
"""
InputFieldStyle = """ InputField {
        opacity: 0.5;
        color: black;
        font-size: 20px;
        font-weight: bold;
        background: white;
    }
"""
login_label_wrong = """
    QLabel {
        opacity: 0;
        color: red;
        font-size: 30px;
        font-weight: bold;
        background: white;
    }
"""
login_label_ok = """
    QLabel {
        color: green;
        opacity: 0;
        font-size: 30px;
        font-weight: bold;
        background: white;
    }
"""
