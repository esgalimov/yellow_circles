import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class YellowCircle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def draw(self, painter):
        painter.setPen(QPen(QColor(239, 225, 100), 3))
        painter.drawEllipse(self.x, self.y, self.s, self.s)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.circles = []

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in self.circles:
            i.draw(qp)
        qp.end()

    def run(self):
        self.circles.append(YellowCircle(randrange(400), randrange(400), randrange(10, 200)))
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())