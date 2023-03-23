# 2 windows

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Window1')
        self.setMinimumWidth(200)
        self.setMinimumHeight(50)
        self.setGeometry(200, 200, 350, 250)
        self.button = QPushButton(self)
        self.button.setText('OK1')
        self.button.show()

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        self.setGeometry(300, 300, 350, 250)
        self.button = QPushButton(self)
        self.button.setText('OK2')
        self.button.setGeometry(100, 100, 100, 100)
        self.button.show()



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')
        self.setGeometry(100, 100, 350, 250)

    def show_window_1(self):

        self.w1 = Window1()
        self.w1.button.clicked.connect(self.show_window_2)
        self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.button.clicked.connect(self.show_window_1)
        self.w2.button.clicked.connect(self.w2.close)
        self.w2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.show_window_1()
    sys.exit(app.exec())