button_style = """
    QPushButton {
        border: 1px solid white;
        border-radius: 5px;
        font-size: 40px;
        font-weight: bold;
        color: white;
        padding: 10px 10px;
        margin: 2px 2px;
    }
    
    QPushButton:hover {
        border: 2px solid white;
        background: #000DFF;
        border-radius: 10px;
        font-size: 32px;
        font-weight: bold;
    }
    QPushButton:pressed {
        border: 2px solid white;
        background: #000DFF;
        border-radius: 10px;
        font-size: 32px;
        font-weight: bold;
    }
"""
global_style = """
    QWidget {
        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                     stop: 0 #6B73FF, stop: 1 #000DFF);
    }
"""
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
