import sys
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QLabel, QPushButton,
                             QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from data_processing import (get_data_base, save_result)
from rotations_3 import get_main


# обработка ошибок
class MyErrorMain(Exception):
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
        self.f_name = QFileDialog.getOpenFileName(self, "Выбрать файл с исходными данными", "",
                                                  "All Files (*);;Excel Files (*.xls)")[0]

    def save_q(self):
        msgBox = QMessageBox(self)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setText("Решение найдено. Сохранить?")
        msgBox.setWindowTitle("Сохранить?")
        return msgBox.exec_()

    def save_file(self):
        self.f_name2 = QFileDialog.getSaveFileName(self, "Сохранить результат", "",
                                                             "All Files (*);;Excel Files (*.xls)")[0]

    def get_solution(self):
        try:
            # обработка ошибки чтения файла
            self.preferences = get_data_base(self.f_name)
            if type(self.preferences) is str:
                raise MyErrorMain()
            else:
                self.pic, self.solution = get_main(self.preferences)
                self.pic.show()

                if self.solution:
                    if QMessageBox.Yes == self.save_q():
                        self.save_file()
                        if self.f_name2:
                            info = save_result(self.solution, self.f_name2)
                            QMessageBox.information(self, "Сохранение", info, QMessageBox.Ok)
                        else:
                             QMessageBox.critical(self, "Ошибка", "Не был выбран файл!", QMessageBox.Ok)

        except MyErrorMain:
            QMessageBox.critical(self, "Ошибка ", self.preferences, QMessageBox.Ok)

        except:
            QMessageBox.critical(self, "Ошибка ", "Возникла непредвиденная ошибка!", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
