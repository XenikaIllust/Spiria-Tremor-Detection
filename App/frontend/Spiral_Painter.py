from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Spiral_Painter(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.draw_enabled = False

        self.image = QImage()

        self.painter = QPainter()
        self.painter.begin(self.image)
        self.painter.setPen(Qt.red)
        self.painter.end()

    def setup_ui(self):
        self.geometry(QRect(400, 400, 400, 400))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw_enabled = True
            self.painter.begin(self.image)
            self.painter.drawPoint(event.pos())
            self.painter.end()

    def mouseMoveEvent(self, event):
        if event.button() == Qt.LeftButton and self.draw_enabled:
            self.painter.begin(self.image)
            self.painter.drawPoint(event.pos())
            self.painter.end()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.draw_enabled:
            self.draw_enabled = False





if __name__ == '__main__':
    app = QApplication(sys.argv)
    spiral_painter = Spiral_Painter()
    spiral_painter.show()
    app.exec_()