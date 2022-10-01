from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from circular_progress import CircularProgress


class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(380, 380)

        self.container = QFrame()
        self.container.setLayout(QVBoxLayout())

        self.background = QFrame()
        # self.background.setContentsMargins(20, 100, 20, 0)
        self.background.setStyleSheet("""
        QFrame{
            background-color: #202020
        }
        """)

        self.layout = QVBoxLayout()
        # self.title_image = QFrame(self.background)
        # self.title_image.setMaximumSize(300, 120)
        # self.title_image.setMinimumSize(300, 120)
        # self.title_image.setStyleSheet("""
        # QFrame{
        #     background-image: url('c:/users/angel/desktop/mafer/images/final logo.png');
        #     background-repeat: no-repeat;
        # }
        # """)
        # self.title_image.move(QPoint(30, 50))

        self.progress = CircularProgress()
        self.progress.width = 250
        self.progress.height = 250
        self.progress._value = 50
        self.progress.setMinimumSize(250, 250)

        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(1)
        self.progress.setGraphicsEffect(self.effect)

        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)

        self.background.setLayout(self.layout)
        self.container.layout().addWidget(self.background)
        self.setCentralWidget(self.container)

        print(self.geometry())

        self.show()

    
    def animate(self):

        self.group = QSequentialAnimationGroup()

        self.progress_animation = QPropertyAnimation(self.progress, b'value', self.progress)
        self.progress_animation.setDuration(1000)
        self.progress_animation.setStartValue(0)
        self.progress_animation.setEndValue(100)
        self.group.addAnimation(self.progress_animation)
        
        self.parallel = QParallelAnimationGroup()
        start_geometry = self.geometry()
        final_geometry = QRect(start_geometry.left(), start_geometry.top()-100, 380, 580)
        self.window_animation = QPropertyAnimation(self, b'geometry')
        self.window_animation.setDuration(500)
        self.window_animation.setStartValue(start_geometry)
        self.window_animation.setEndValue(final_geometry)
        self.window_animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.parallel.addAnimation(self.window_animation)

        print(self.progress.geometry())
        self.opacity_animation = QPropertyAnimation(self.progress, b'opacity')
        self.opacity_animation.setDuration(500)
        self.opacity_animation.setStartValue(0)
        self.opacity_animation.setEndValue(1)
        self.parallel.addAnimation(self.opacity_animation)

        self.group.addAnimation(self.parallel)
        self.group.start()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.animate()
    sys.exit(app.exec_())