import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys

class Window(qtw.QWidget):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.setWindowTitle('PyQt5 Testing')
        self.setMinimumSize(500, 300)

        layout = qtw.QFormLayout()
        self.setLayout(layout)

        self.label_1 = qtw.QLabel('Cool label row')
        self.label_1.setFont(qtg.QFont('Helvetica', 24))
        self.first_name = qtw.QLineEdit(self)
        self.last_name = qtw.QLineEdit(self)

        layout.addRow(self.label_1)
        layout.addRow('First Name', self.first_name)
        layout.addRow('Last Name', self.last_name)
        layout.addRow(qtw.QPushButton('Press Me!', clicked=self.press))

        self.show()

    def press(self):
        self.label_1.setText(f'Hi {self.first_name.text()} {self.last_name.text()}')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())