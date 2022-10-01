from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsBlurEffect, QFrame, QVBoxLayout, QLineEdit, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
import sys
from BlurWindow.blurWindow import blur

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(360, 640)

        blur(self.winId(), hexColor='#00000000', Acrylic=False)

        self.layout = QVBoxLayout()

        self.background = QFrame()
        self.setCentralWidget(self.background)
        self.background.setStyleSheet("""
        QFrame{
            background-color: none;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.3)
        }
        """)
        self.setCentralWidget(self.background)

        self.container = QFrame(self)
        self.container.setFixedSize(360, 640)
        self.container.move(0, 0)
        self.container.setLayout(self.layout)
        self.container.setStyleSheet("""
        QFrame{
            border-radius: 16px;
            
        }
        """)

        self.username_label = QLabel()
        self.username_label.setText('Username')
        self.username_label.setStyleSheet("""
        QLabel{
            font-family: Segoe UI;
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: none
        }
        """)
        self.layout.addWidget(self.username_label, alignment=Qt.AlignLeft)

        self.username_entry = QLineEdit()
        self.username_entry.setFixedSize(280, 60)
        self.username_entry.setTextMargins(10, 0, 10, 0)
        self.username_entry.setPlaceholderText('Enter Your Username')
        self.username_entry.setStyleSheet("""
        QLineEdit{
            border-radius: 5px;
            border: 0px;
            background-color: rgba(255, 255, 255, 0.1);
            color: rgba(255, 255, 255, 0.8);
            font-family: Segoe UI;
            font-size: 14px;
        }
        """)
        self.layout.addWidget(self.username_entry, alignment=Qt.AlignCenter)

        self.layout.addSpacing(40)

        self.password_label = QLabel()
        self.password_label.setText('Password')
        self.password_label.setStyleSheet("""
        QLabel{
            font-family: Segoe UI;
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: none;
        }
        """)
        self.layout.addWidget(self.password_label, alignment=Qt.AlignLeft)

        self.password_entry = QLineEdit()
        self.password_entry.setFixedSize(280, 60)
        self.password_entry.setPlaceholderText('Enter Your Password')
        self.password_entry.setTextMargins(10, 0, 10, 0)
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_entry.setStyleSheet("""
        QLineEdit{
            border-radius: 5px;
            border: 0px;
            background-color: rgba(255, 255, 255, 0.1);
            color: rgba(255, 255, 255, 0.8);
            font-family: Segoe UI;
            font-size: 14px;
        }
        """)
        self.layout.addWidget(self.password_entry, alignment=Qt.AlignCenter)

        self.layout.setSpacing(15)
        self.layout.setContentsMargins(40, 190, 40, 190)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
