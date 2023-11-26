from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor

from PyQt5 import QtWidgets, QtCore
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Git и случайные окружности")


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(500, 500, 500, 500)
        self.pushButton = QPushButton(self)
        self.pushButton.setText("Вроде кнопка")
        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        tru = QPixmap(500, 500)
        self.label.setPixmap(tru)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 10, 0)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x = randint(10, 400)
        y = randint(10, 400)
        h1 = randint(10, 100)
        h2 = h1
        color = ([randint(0, 255) for i in range(3)])

        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*color))
        painter.setPen(pen)
        painter.drawEllipse(x, y, h1, h2)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
