""" Пример программы по взаимодействию PushButton, LineEdit, Label"""
""" Пример программы по взаимодействию PushButton, LineEdit, Label"""

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit, QPushButton, QTextEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QHBoxLayout, QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tf = True
        self.text = 'Нажмите Enter!'
        self.setWindowTitle("My App")
        self.resize(300, 300)

        layout = QVBoxLayout()

        widget0 = QLabel("Введите выражение, ") # Label "Введите число"
        font = widget0.font()
        font.setPointSize(10)
        widget0.setFont(font)
        widget0.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)


        widget1 = QLabel("нажмите Enter")  # Label "Нажимете Enter"
        font = widget1.font()
        font.setPointSize(10)
        widget1.setFont(font)
        widget1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.widget2 = QLineEdit() # LineEdit для ввода текста
        self.widget2.setMaxLength(20)

        # widget.setReadOnly(True) # раскомментируйте, чтобы сделать доступным только для чтения

        self.widget2.returnPressed.connect(self.return_pressed)
        self.widget2.selectionChanged.connect(self.selection_changed)
        self.widget2.textChanged.connect(self.text_changed)
        self.widget2.textEdited.connect(self.text_edited)
        self.widget2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        button = QPushButton("Результат!") # PushButton
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.label_result = QLabel() # Label для дублирования введенной строки

        self.qte = QTextEdit() # Виджет для получения результата                    ####################################
        self.qte.append("Здесь будет результат")                                    ####################################

        widgets = [widget0, widget1, self.widget2, button, self.label_result, self.qte]  ################################
        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.text = self.widget2.text()

    def selection_changed(self):
        print("Selection changed")

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    def the_button_was_clicked(self):
        print("Clicked!")
        self.label_result.setText(self.text)
        #####################################################################################
        try:
            res = str(eval(self.text)) # Заодно проверяется возможно ли введенное действие
            self.qte.append(res)
        except:
            pass
        #####################################################################################
        if self.tf:
            self.setWindowTitle('Result')
            self.tf = False
        else:
            self.tf = True
            self.setWindowTitle('MyApp')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()