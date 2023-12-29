button_style_contacts = """
    QPushButton {
        border: 1px solid rgba(100,100,100,1);
        border-radius: 2px;
        font-size: 18px;
        font-weight: 550;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: rgba(30,30,30,0.7);
    }
    
    QPushButton:hover {
        margin: 1.4px 1.4px;
        border: 1px solid white;
        font-size: 20px;
        font-weight: bold;
        background: rgba(50,160,250,0.7);
    }
    QPushButton:pressed {
        border-radius: 1px;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid white;
        background: rgba(50,160,255,0.8);
}

"""
button_style_contacts_selected = """
    QPushButton {
        border: 1px solid rgba(100,100,100,1);
        border-radius: 2px;
        font-size: 18px;
        font-weight: 550;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: rgba(50,160,250,0.4);
    }
    
    QPushButton:hover {
        margin: 1.4px 1.4px;
        border: 1px solid white;
        font-size: 20px;
        font-weight: bold;
        background: rgba(50,160,250,0.7);
    }
    QPushButton:pressed {
        border-radius: 1px;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid white;
        background: rgba(50,160,255,0.8);
}
"""

quote_style = """
QLabel {
    color: white;
    background-color: rgba(0, 0, 0, 70);
    border: 1px solid black;
    padding: 10px;
    border-radius: 5px;
}
"""
welcome_user_style = """
QLabel {
    color: white;
    font-size: 40px;
    background-color: rgba(140, 140, 140, 70);
    border: 1px solid rgba(180, 180, 180, 180);
    padding: 10px;
    border-radius: 3px;
    font-weight: bold;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
"""

button_style_upload = """
    QPushButton {
        border: 1px solid rgba(170,170,255,1);
        border-radius: 1px;
        font-size: 20px;
        font-weight: 550;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: rgba(15,15,150,0.8);
    }
    
    QPushButton:hover {
        font-size: 19px;
        font-weight: bold;
        background: rgba(10,10,80,0.8);
    }
    QPushButton:pressed {
        margin: 1.4px 1.4px;
        border-radius: 1px;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border: 2px solid white;
}
"""

button_style = """
    QPushButton {
        border: 1px solid rgba(170,170,255,1);
        border-radius: 1px;
        font-size: 40px;
        font-weight: 550;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: rgba(15,15,150,0.8);
    }
    
    QPushButton:hover {
        margin: 1.5px 1.5px;
        border: 1.2px solid white;
        font-size: 38px;
        font-weight: bold;
        background: rgba(10,10,80,0.8);
    }
    QPushButton:pressed {
        margin: 1.4px 1.4px;
        border-radius: 1px;
        color: white;
        font-size: 30px;
        font-weight: bold;
        border: 2px solid white;
}
"""
button_style_logged = """
    QPushButton {
        border: 1px solid rgba(100,100,100,1);
        border-radius: 2px;
        font-size: 30px;
        font-weight: 550;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: rgba(30,30,30,0.7);
    }
    
    QPushButton:hover {
        margin: 1.4px 1.4px;
        border: 1px solid white;
        font-size: 28px;
        font-weight: bold;
        background: rgba(10,10,180,1);
    }
    QPushButton:pressed {
        border-radius: 1px;
        color: white;
        font-size: 25px;
        font-weight: bold;
        border: 2px solid white;
}
"""
edit_profile_button = """
    QPushButton {
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 1px;
        font-size: 20px;
        font-weight: 600;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: qradialgradient(cx: 0.5, cy: 0.5, fx: 0.5, fy: 0.5, radius: 1, stop: 0 #0000FF, stop: 0.7 #0000AA, stop: 1 #000088);
    }
    
    QPushButton:hover {
        
    }
    QPushButton:pressed {
        background-color: rgba(255, 255, 255, 0.6);
        color: white;
        font-size: 18px;
        border: 1px solid white;
        border-radius: 0px;
        margin: 2px 2px;
}
"""

edit_profile_button_clicked = """
    QPushButton {
        border: 1px solid rgba(255,255,255,0);
        border-radius: 2px;
        font-size: 18px;
        font-weight: 700;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    QPushButton:hover {
        
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
        opacity: 0.6;
        font-size: 30px;
        background: rgba(0,0,0,0);

    }
"""


tag = """
    QLabel {
        opacity: 0;
        font-size: 22px;
        background: rgba(50,80,255,.6);
        color: white;
        font-weight: bold;
        border: 1.5px solid rgba(255,255,255,.8);
        border-radius: 2.5px;
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
        font-size: 23px;
        font-weight: bold;
        background: rgba(255,255,255,0.8);
    }
"""
messages_buttons = """
    QPushButton {
        border: 1px solid rgba(100,100,100,1);
        border-radius: 2px;
        font-size: 30px;
        font-weight: 550;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
        background: rgba(30,30,30,0.7);
    }
    
    QPushButton:hover {
        margin: 1.4px 1.4px;
        border: 1px solid white;
        font-size: 28px;
        font-weight: bold;
        background: rgba(10,10,180,1);
    }
    QPushButton:pressed {
        border-radius: 1px;
        color: white;
        font-size: 25px;
        font-weight: bold;
        border: 2px solid white;
}
"""
