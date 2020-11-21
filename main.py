import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class YellowCircle:
    def __init__(self, x, y, s, color):
        self.x = x
        self.y = y
        self.s = s
        self.color = color

    def draw(self, painter):
        painter.setPen(QPen(self.color, 3))
        painter.drawEllipse(self.x, self.y, self.s, self.s)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.circles = []

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in self.circles:
            i.draw(qp)
        qp.end()

    def run(self):
        self.circles.append(YellowCircle(randrange(400), randrange(400),
                                         randrange(10, 200), QColor(randrange(255),
                                         randrange(255), randrange(255))))
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())