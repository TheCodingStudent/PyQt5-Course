from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import QRect, Qt, pyqtProperty, pyqtSignal

class CircularProgress(QWidget):
    def __init__(self, master=None):
        super().__init__(master)

        self._value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_color = '#ffffff'
        self.max_value = 100
        self.font_family = 'Segoe UI'
        self.font_size = 12
        self.suffix = '%'
        self.progress_rounded_cap = False
        self.text_color = '#ffffff'

        self.resize(self.width, self.height)
    
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        if value != self._value:
            self._value = value
            self.update()

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width // 2
        value = int(self._value * 360 // self.max_value)

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family, self.font_size))

        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        if self.progress_rounded_cap is True:
            pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f'{self.value}{self.suffix}')

        paint.end()
    
    value = pyqtProperty(int, getValue, setValue)
    valueChanged = pyqtSignal(int)