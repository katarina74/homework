import sys
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QLabel, QPushButton,
                             QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from data_processing import (get_data_base, save_result)
from rotations_3 import get_main


# обработка ошибок
class MyError(Exception):
    pass


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.pic = None

    def init_ui(self):

        # 1 строка
        self.lbl1 = QLabel('Выберите файл:', self)
        self.lbl1.setFont(QFont("Verdana", 18, QFont.StyleItalic))
        self.lbl1.adjustSize()
        self.lbl1.setFixedWidth(300)
        self.lbl1.setAlignment(Qt.AlignCenter)
        self.lbl1.move(210, 30)

        # 2 строка
        self.button = QPushButton('Выбрать файл!', self)
        self.button.setFont(QFont("Verdana", 28, QFont.StyleItalic))
        self.button.adjustSize()
        self.button.move(200, 80)
        self.button.clicked.connect(self.open_file)

        # 2 строка
        self.button2 = QPushButton('Найти решение!', self)
        self.button2.setFont(QFont("Verdana", 28, QFont.StyleItalic))
        self.button2.adjustSize()
        self.button2.move(185, 160)
        self.button2.clicked.connect(self.get_solution)

        # параметры окна
        self.setGeometry(500, 100, 800, 300)
        self.setWindowTitle('Алгоритм Ирвинга')
        self.show()

    def open_file(self):
        self.f_name = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Excel Files (*.xls)")[0]

    def get_solution(self):
        try:
            # обработка ошибки чтения файла
            self.preferences = get_data_base(self.f_name)
            if type(self.preferences) is str:
                raise MyError()
            else:
                self.pic, self.solution = get_main(self.preferences)
                self.pic.show()

                msgBox = QMessageBox(self)
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                if self.solution:
                    msgBox.setText("Решение найдено. Сохранить?")
                    msgBox.setWindowTitle("Сохранить?")
                    result = msgBox.exec_()
                    if QMessageBox.Yes == result:
                        self.open_file()
                        test = save_result(self.solution, self.f_name)
                        if test:
                            QMessageBox.critical(self, "Ошибка", test, QMessageBox.Ok)

        except MyError:
            QMessageBox.critical(self, "Ошибка ", self.preferences, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
