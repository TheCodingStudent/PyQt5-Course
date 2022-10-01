import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu')
        self.resize(800, 500)

        self.menuBar = self.menuBar()

        file_menu = self.menuBar.addMenu('File')
        edit_menu = self.menuBar.addMenu('Edit')

        sub_menu = edit_menu.addMenu('Templates')
        sub_menu.addAction(QAction('Window', self))
        sub_menu.addAction(QAction('Frame', self))

        exit_action = QAction('Exit...', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(QApplication.quit)

        file_menu.addAction(exit_action)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())