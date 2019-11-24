import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout
import re

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Culc(QWidget):
    def __init__(self, parent=None):
        super(Culc, self).__init__(parent)
        self.setWindowTitle("culc")
        self.resize(250, 150)
        self.move(300, 300)

        self.text_edit = ""

        self.edit1 = QLineEdit(self.text_edit)
        self.button0 = QPushButton("0")
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button_plus = QPushButton("+")
        self.button_min = QPushButton("-")
        self.button_div = QPushButton("/")
        self.button_mul = QPushButton("*")
        self.button_C = QPushButton("C")
        self.button_eq = QPushButton("=")
        self.button_dot = QPushButton(".")


        layout = QGridLayout()
        layout.addWidget(self.edit1,0,0,1,0)
        layout.addWidget(self.button0,1,1)
        layout.addWidget(self.button1,1,2)
        layout.addWidget(self.button2,1,3)
        layout.addWidget(self.button3,1,4)
        layout.addWidget(self.button4,2,1)
        layout.addWidget(self.button5,2,2)
        layout.addWidget(self.button6,2,3)
        layout.addWidget(self.button7,2,4)
        layout.addWidget(self.button8,3,1)
        layout.addWidget(self.button9,3,2)
        layout.addWidget(self.button_plus,3,3)
        layout.addWidget(self.button_min,3,4)
        layout.addWidget(self.button_div,4,1)
        layout.addWidget(self.button_mul,4,2)
        layout.addWidget(self.button_C,4,3)
        layout.addWidget(self.button_eq,4,4)
        layout.addWidget(self.button_dot, 5, 1)

        self.button0.clicked.connect(self.insert_0)
        self.button1.clicked.connect(self.insert_1)
        self.button2.clicked.connect(self.insert_2)
        self.button3.clicked.connect(self.insert_3)
        self.button4.clicked.connect(self.insert_4)
        self.button5.clicked.connect(self.insert_5)
        self.button6.clicked.connect(self.insert_6)
        self.button7.clicked.connect(self.insert_7)
        self.button8.clicked.connect(self.insert_8)
        self.button9.clicked.connect(self.insert_9)
        self.button_dot.clicked.connect(self.insert_dot)

        self.button_plus.clicked.connect(self.plus)
        self.button_min.clicked.connect(self.minus)
        self.button_div.clicked.connect(self.div)
        self.button_mul.clicked.connect(self.mul)
        self.button_C.clicked.connect(self.clear)

        self.button_eq.clicked.connect(self.get_answer)

        self.setLayout(layout)

    def insert_0(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "0"
        self.edit1.setText(self.text_edit)
    def insert_1(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "1"
        self.edit1.setText(self.text_edit)
    def insert_2(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "2"
        self.edit1.setText(self.text_edit)
    def insert_3(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "3"
        self.edit1.setText(self.text_edit)
    def insert_4(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "4"
        self.edit1.setText(self.text_edit)
    def insert_5(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "5"
        self.edit1.setText(self.text_edit)
    def insert_6(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "6"
        self.edit1.setText(self.text_edit)
    def insert_7(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "7"
        self.edit1.setText(self.text_edit)
    def insert_8(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "8"
        self.edit1.setText(self.text_edit)
    def insert_9(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "9"
        self.edit1.setText(self.text_edit)
    def insert_dot(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "."
        self.edit1.setText(self.text_edit)

    def plus(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "+"
        self.edit1.setText(self.text_edit)
    def minus(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "-"
        self.edit1.setText(self.text_edit)
    def mul(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "*"
        self.edit1.setText(self.text_edit)
    def div(self):
        if self.text_edit == "ошибка":
            self.text_edit = ""
        self.text_edit = self.text_edit + "/"
        self.edit1.setText(self.text_edit)
    def clear(self):
        self.text_edit = ""
        self.edit1.setText(self.text_edit)

    def get_answer(self):
        if self.text_edit == "ошибка" or self.text_edit == "":
            self.text_edit = "0"
        else:
            z = set(list(filter(lambda a: a != "", re.split("[\w|^.]", self.text_edit))))
            try:
                if z.issubset({"+","-","/","*","+-","-+","*-","*+","/+","/-"}):
                    while not isint(self.text_edit[-1]):
                            self.text_edit = self.text_edit[:-2]
                    self.text_edit = str(eval(self.text_edit))
                    self.edit1.setText(self.text_edit)
                else:
                    print("else")
                    self.text_edit = "ошибка"
                    self.edit1.setText(self.text_edit)
            except:
                print("ex")
                self.text_edit = "ошибка"
                self.edit1.setText(self.text_edit)



if __name__ == '__main__':
    app = QApplication()
    culc = Culc()
    culc.show()
    sys.exit(app.exec_())