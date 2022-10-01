from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QPoint
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.status = 0
        self.string = None

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        main = QFrame(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setStyleSheet("""
            QFrame{
                background-color: #202020;
                border-radius: 10px
            }
        """)
        main.setMinimumSize(300, 500)
        self.setCentralWidget(main)        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main.setLayout(main_layout)

        self.top_frame = QFrame()
        self.top_frame.setMaximumHeight(30)
        self.top_frame.setStyleSheet("""
            QFrame{
                background-color: #323232;
                border-radius: 0px 0px 10px 0px
            }
        """)
        self.top_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.top_frame.mouseMoveEvent = moveWindow
        main_layout.addWidget(self.top_frame)

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)
        self.top_frame.setLayout(button_layout)
        self.minimize_button = QPushButton()
        self.minimize_button.setMinimumSize(45, 30)
        self.minimize_button.setIcon(QIcon("c:/users/angel/python/new gui/images/minimize.png"))
        self.minimize_button.setIconSize(QSize(16, 16))
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setStyleSheet("""
        QPushButton{
            border: 0px;
            border-radius: 10px
        }
        QPushButton:hover{
            background-color: "#505050"
        }
        """)
        button_layout.addWidget(self.minimize_button)

        self.maximize_button = QPushButton()
        self.maximize_button.setMinimumSize(45, 30)
        self.maximize_button.setIcon(QIcon("c:/users/angel/python/new gui/images/maximize.png"))
        self.maximize_button.setIconSize(QSize(16, 16))
        self.maximize_button.clicked.connect(self.maximize_restore)
        self.maximize_button.setStyleSheet("""
        QPushButton{
            border: 0px;
            border-radius: 10px
        }
        QPushButton:hover{
            background-color: "#505050"
        }
        """)
        button_layout.addWidget(self.maximize_button)

        self.close_button = QPushButton()
        self.close_button = QPushButton()
        self.close_button.setMinimumSize(45, 30)
        self.close_button.setIcon(QIcon('c:/users/angel/python/new gui/images/close.png'))
        self.close_button.setIconSize(QSize(16, 16))
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("""
        QPushButton{
            background-color: #323232;
            border: 0px;
            border-radius: 10px
        }
        QPushButton::hover{
            background-color: #ff0000
        }
        """)
        button_layout.addWidget(self.close_button)

        self.result_label = QLineEdit()
        self.result_label.setText('0')
        self.result_label.setFont(QFont('Helvetica', 24))
        self.result_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.result_label.textChanged.connect(self.update_string)
        self.result_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(self.result_label, stretch=2)

        options_layout = QHBoxLayout()
        for option in ['MC', 'MR', 'M+', 'M-', 'MS', 'M']:
            button = QPushButton(option)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setStyleSheet("""
                QPushButton{
                    color: "#808080";
                    border: 1px solid #404040;
                    font-family: Helvetica;
                    font-size: 16px
                }
                QPushButton:hover{
                    color: "#ffffff";
                    background-color: "#262626"
                }
                """)
            options_layout.addWidget(button)
        main_layout.addLayout(options_layout, stretch=1)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)
        buttons = [
            ['%', 'CE', 'C', 'X'],
            ['1/x', 'x^2', 'sqrt(x)', '/'],
            ['1', '2', '3', '*'],
            ['4', '5', '6', '-'],
            ['7', '8', '9', '+'],
            ['+/-', '0', '.', '=']
        ]

        for j in range(6):
            for i in range(4):
                symbol = buttons[j][i]
                button = QPushButton(symbol)
                button.setStyleSheet("""
                QPushButton{
                    color: "#808080";
                    border: 1px solid #404040;
                    font-family: Helvetica;
                    font-size: 16px
                }
                QPushButton:hover{
                    color: "#ffffff";
                    background-color: "#262626"
                }
                """)

                match symbol:
                    case 'X': button.clicked.connect(self.erase)
                    case '=': button.clicked.connect(self.equal)
                    case _: self.connect(button, symbol)

                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                grid_layout.addWidget(button, j, i)
        
        main_layout.addLayout(grid_layout, stretch=9)

        self.show()
    
    def maximize_restore(self):
        if self.status == 0:
            self.showMaximized()
        else:
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            
        self.status = not self.status
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def connect(self, button, key):
        button.clicked.connect(lambda: self.write(key))
    
    def update_string(self):
        self.string = self.result_label.text()
    
    def write(self, key):
        if self.string in (None, 'Error'): self.string = key
        else: self.string += key
        self.result_label.setText(self.string)

    def erase(self):
        if not self.string: return
        self.string = self.string[:-1]
        self.result_label.setText(self.string)
    
    def equal(self):
        try: self.string = str(eval(self.string))
        except SyntaxError: self.string = 'Error'
        self.result_label.setText(self.string)
    
    def keyPressEvent(self, event) -> None:
        try:
            if (key := chr(event.key())) in '0123456789.*+-/=()':
                if key == '=':
                    self.equal()
                else:
                    self.write(key)
        except ValueError: pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())