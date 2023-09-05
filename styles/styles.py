new_login_button = """
            QPushButton {
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100vh;
                display: flex;
                flex-direction: row;
                justify-content: center;
                align-items: center;
                background: #000;
            }
            QPushButton:hover {
                width: 220px;
                height: 50px;
                border: none;
                outline: none;
                color: #fff;
                background: #111;
                cursor: pointer;
                position: relative;
                z-index: 0;
                border-radius: 10px;
            }
            QPushButton:hover:before {
                content: '';
                background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
                position: absolute;
                top: -2px;
                left: -2px;
                background-size: 400%;
                z-index: -1;
                filter: blur(5px);
                width: calc(100% + 4px);
                height: calc(100% + 4px);
                animation: glowing 20s linear infinite;
                opacity: 0;
                transition: opacity .3s ease-in-out;
                border-radius: 10px;
            }
            QPushButton:hover:active {
                color: #000;
            }
            QPushButton:hover:active:after {
                background: transparent;
            }
            QPushButton:hover:before {
                opacity: 1;
            }
            QPushButton:hover:after {
                z-index: -1;
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background: #111;
                left: 0;
                top: 0;
                border-radius: 10px;
            }
        """

# @keyframes glowing {
#     0% { background-position: 0 0; }
#     50% { background-position: 400% 0; }
#     100% { background-position: 0 0; }
# }"""


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
