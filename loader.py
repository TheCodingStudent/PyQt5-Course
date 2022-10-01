from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from circular_progress import CircularProgress
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.container = QFrame()
        self.container.setStyleSheet("""
        QFrame{
            background-color: QLinearGradient(x1: 0, y1: 0 x2: 1, y2: 1, stop: 0 #ff0080, stop: 1 #00ffff);
            border-radius: 10px
        }
        """)
        self.layout = QVBoxLayout()

        self.progress = CircularProgress()
        self.progress.value = 50
        self.progress.progress_color = '#8000ff'
        self.progress.progress_rounded_cap = True

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.progress.set_value)

        self.slider_animation = QPropertyAnimation(self.slider, b'value')
        self.slider_animation.setDuration(2000)
        self.slider_animation.setStartValue(0)
        self.slider_animation.setEndValue(100)
        self.slider_animation.setEasingCurve(QEasingCurve.Linear)
        self.slider_animation.start()

        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.slider, Qt.AlignCenter, Qt.AlignCenter)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())