from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Spiral_Painter(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.setAutoFillBackground(True)
        self.setup_ui()

        self.draw_enabled = False
        self.last_pos = None
        self.points = []

    def setup_ui(self):
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap("../assets/images/logo.png").scaled(self.width(), self.height(), Qt.KeepAspectRatio)))
        # self.setPalette(palette)
        self.pixmap = QPixmap("./assets/images/logo.png").scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio))

    def paintEvent(self, event):
        if self.last_pos != None:
            self.points.append(self.last_pos)

            painter = QPainter()
            painter.begin(self.image.pixmap())
            painter.setPen(Qt.red)
            painter.pen().setWidth(10)
            for ind in range(0, len(self.points)-1):
                painter.drawLine(self.points[ind], self.points[ind+1])
            painter.end()
            print("canvas repainted")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw_enabled = True
            print("Mouse press: ", event.pos())
            self.last_pos = event.pos()
            # self.repaint()
            self.update()

    def mouseMoveEvent(self, event):
        if self.draw_enabled:
            print("Mouse move: ", event.pos())
            self.last_pos = event.pos()
            # self.repaint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.draw_enabled:
            print("Mouse release: ", event.pos())
            self.draw_enabled = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    spiral_painter = Spiral_Painter()
    spiral_painter.setGeometry(400,400,400,400)
    spiral_painter.show()
    app.exec_()

"""
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys, random


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 190)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())()
"""