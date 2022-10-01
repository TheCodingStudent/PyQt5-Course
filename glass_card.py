from PyQt5.QtWidgets import QApplication, QFrame, QMainWindow, QGraphicsBlurEffect, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QParallelAnimationGroup
from PyQt5.QtGui import QColor
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 400)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet('background-color: black')

        self.purple = QFrame(self)
        self.purple.setFixedSize(300, 300)
        self.purple.setStyleSheet('background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ff0080, stop: 1 #00ffff); border-radius: 150px')
        self.purple.move(400, -130)

        self.orange = QFrame(self)
        self.orange.setFixedSize(300, 300)
        self.orange.setStyleSheet('background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ff0000, stop: 1 #ffff00); border-radius: 150px')
        self.orange.move(-100, 200)

        self.card_background = QFrame(self)
        self.card_background.setFixedSize(460, 300)
        self.card_background.move(70, 50)
        self.card_background.setStyleSheet("""
            background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgba(255, 255, 255, 0.2), stop: 1 rgba(255, 255, 255, 0));
            border: 1px solid rgba(255, 255, 255, 0.5);
            border-radius: 30px
        """)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor('#000000'))
        self.card_background.setGraphicsEffect(self.shadow)

        self.card = QFrame(self)
        self.card.setFixedSize(460, 300)
        self.card.setStyleSheet('background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgba(255, 255, 255, 0.2), stop: 1 rgba(255, 255, 255, 0.1)); border-radius: 30px')
        self.card.move(70, 50)

        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(20)
        self.card.setGraphicsEffect(self.blur_effect)

        self.animations = QParallelAnimationGroup()

        self.orange_animation = QPropertyAnimation(self.orange, b'pos')
        self.orange_animation.setStartValue(QPoint(-100, 200))
        self.orange_animation.setEndValue(QPoint(250, -350))
        self.orange_animation.setDuration(20000)
        self.orange_animation.setEasingCurve(QEasingCurve.Linear)

        self.purple_animation = QPropertyAnimation(self.purple, b'pos')
        self.purple_animation.setStartValue(QPoint(400, -130))
        self.purple_animation.setEndValue(QPoint(300, 550))
        self.purple_animation.setDuration(20000)
        self.purple_animation.setEasingCurve(QEasingCurve.Linear)

        self.animations.addAnimation(self.orange_animation)
        self.animations.addAnimation(self.purple_animation)
        self.animations.start()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())