import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.numbers = ''
        self.number = ''
        self.btn0 = QPushButton('0', self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('2', self)
        self.btn3 = QPushButton('3', self)
        self.btn4 = QPushButton('4', self)
        self.btn5 = QPushButton('5', self)
        self.btn6 = QPushButton('6', self)
        self.btn7 = QPushButton('7', self)
        self.btn8 = QPushButton('8', self)
        self.btn9 = QPushButton('9', self)

        self.btn_div = QPushButton('/', self)
        self.btn_dot = QPushButton('.', self)
        self.btn_plusminus = QPushButton('±', self)
        self.btn_minus = QPushButton('-', self)
        self.btn_mult = QPushButton('*', self)
        self.btn_plus = QPushButton('+', self)

        self.btn_eq = QPushButton('=', self)
        self.btn_clear = QPushButton('C', self)

        self.table = QLabel('0', self)
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.minitext = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 320, 500)
        self.setWindowTitle('Калькуляторик')

        self.btn0.setGeometry(80, 340, 80, 80)
        self.btn1.setGeometry(0, 260, 80, 80)
        self.btn2.setGeometry(80, 260, 80, 80)
        self.btn3.setGeometry(160, 260, 80, 80)
        self.btn4.setGeometry(0, 180, 80, 80)
        self.btn5.setGeometry(80, 180, 80, 80)
        self.btn6.setGeometry(160, 180, 80, 80)
        self.btn7.setGeometry(0, 100, 80, 80)
        self.btn8.setGeometry(80, 100, 80, 80)
        self.btn9.setGeometry(160, 100, 80, 80)

        self.btn_div.setGeometry(240, 100, 80, 80)
        self.btn_dot.setGeometry(0, 340, 80, 80)
        self.btn_plusminus.setGeometry(160, 340, 80, 80)
        self.btn_minus.setGeometry(240, 260, 80, 80)
        self.btn_mult.setGeometry(240, 180, 80, 80)
        self.btn_plus.setGeometry(240, 340, 80, 80)

        self.btn_eq.setGeometry(160, 420, 160, 80)
        self.btn_clear.setGeometry(0, 420, 160, 80)

        self.table.setGeometry(0, 40, 320, 80)
        self.minitext.setGeometry(0, 0, 320, 40)

        self.btn0.clicked.connect(self.for_number0)
        self.btn1.clicked.connect(self.for_number1)
        self.btn2.clicked.connect(self.for_number2)
        self.btn3.clicked.connect(self.for_number3)
        self.btn4.clicked.connect(self.for_number4)
        self.btn5.clicked.connect(self.for_number5)
        self.btn6.clicked.connect(self.for_number6)
        self.btn7.clicked.connect(self.for_number7)
        self.btn8.clicked.connect(self.for_number8)
        self.btn9.clicked.connect(self.for_number9)

        self.btn_div.clicked.connect(self.div)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_plusminus.clicked.connect(self.plusminus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_plus.clicked.connect(self.plus)

        self.btn_eq.clicked.connect(self.eq)
        self.btn_clear.clicked.connect(self.clear_all)

    def for_number0(self):
        self.numbers += '0'
        self.number += '0'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number1(self):
        self.numbers += '1'
        self.number += '1'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number2(self):
        self.numbers += '2'
        self.number += '2'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number3(self):
        self.numbers += '3'
        self.number += '3'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number4(self):
        self.numbers += '4'
        self.number += '4'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number5(self):
        self.numbers += '5'
        self.number += '5'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number6(self):
        self.numbers += '6'
        self.number += '6'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number7(self):
        self.numbers += '7'
        self.number += '7'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number8(self):
        self.numbers += '8'
        self.number += '8'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def for_number9(self):
        self.numbers += '9'
        self.number += '9'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def div(self):
        self.numbers += ' / '
        self.number = ''
        self.minitext.setFont(QtGui.QFont("Helvetica [Cronyx]", 30))
        self.minitext.setText(self.numbers)
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText('0')

    def dot(self):
        self.numbers += '.'
        self.number += '.'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def plusminus(self):
        self.numbers += '-'
        self.number += '-'
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(self.number)

    def minus(self):
        self.numbers += ' - '
        self.number = ''
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.minitext.setFont(QtGui.QFont("Helvetica [Cronyx]", 30))
        self.minitext.setText(self.numbers)
        self.table.setText('0')

    def plus(self):
        self.numbers += ' + '
        self.number = ''
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.minitext.setFont(QtGui.QFont("Helvetica [Cronyx]", 30))
        self.minitext.setText(self.numbers)
        self.table.setText('0')

    def mult(self):
        self.numbers += ' * '
        self.number = ''
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.minitext.setFont(QtGui.QFont("Helvetica [Cronyx]", 30))
        self.minitext.setText(self.numbers)
        self.table.setText('0')

    def eq(self):
        result = eval(self.numbers)
        self.numbers = str(result)
        self.number = str(result)
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText(str(result))
        self.minitext.setFont(QtGui.QFont("Helvetica [Cronyx]", 30))
        self.minitext.setText('')

    def clear_all(self):
        self.numbers = ''
        self.number = ''
        self.table.setFont(QtGui.QFont("Helvetica [Cronyx]", 35))
        self.table.setText('0')
        self.minitext.setFont(QtGui.QFont("Helvetica [Cronyx]", 30))
        self.minitext.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    calc = Calc()
    calc.show()

    sys.exit(app.exec())
