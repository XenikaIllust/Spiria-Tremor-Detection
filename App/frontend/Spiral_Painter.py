from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Spiral_Painter(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.setup_ui()

        self.draw_enabled = False

        self.pixmap = QPixmap(self.width(), self.height())
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        self.last_pos = None

        self.painter = QPainter()

    def setup_ui(self):
        self.setGeometry(QRect(400, 400, 400, 400))
        self.show()

    def paintEvent(self, event):
        if self.last_pos != None:
            self.painter.begin(self.pixmap)
            self.painter.setPen(Qt.red)
            self.painter.pen().setWidth(10)
            self.painter.drawEllipse(self.last_pos, 50, 50)
            self.painter.end()
            self.label.setPixmap(self.pixmap)
            print("canvas repainted")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw_enabled = True
            print("Mouse press: ", event.pos())
            # self.painter.drawPoint(event.pos())
            self.last_pos = event.pos()
            #self.repaint()
            self.update()

    def mouseMoveEvent(self, event):
        if self.draw_enabled:
            print("Mouse move: ", event.pos())
            # self.painter.drawPoint(event.pos())
            self.last_pos = event.pos()
            #self.repaint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.draw_enabled:
            print("Mouse release: ", event.pos())
            self.draw_enabled = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    spiral_painter = Spiral_Painter()
    app.exec_()
