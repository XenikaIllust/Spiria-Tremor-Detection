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
        self.curr_pos = None
        self.points = []

    def setup_ui(self):
        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap("../assets/images/logo.png").scaled(self.width(), self.height(), Qt.KeepAspectRatio)))
        # self.setPalette(palette)
        self.pixmap = QPixmap("assets/images/template.jpg")
        self.resize(self.pixmap.width(), self.pixmap.height())
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio))

        self.canvas = QLabel(self)
        self.canvas_pixmap = QPixmap(self.width(), self.height()).scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.canvas_pixmap.fill(Qt.transparent)
        self.canvas.setPixmap(self.canvas_pixmap)
        
    def set_paint_device(self, device):
        self.device = device
        self.device.point_ready.connect(self.add_point)
        self.device.start_parallel_feed()

    def paintEvent(self, event):
        self.canvas.pixmap().fill(Qt.transparent)
        if self.curr_pos != None:
            cursor_painter = QPainter()
            cursor_painter.begin(self.canvas.pixmap())
            cursor_painter.pen().setWidth(100)
            cursor_painter.setPen(Qt.blue)
            cursor_painter.setBrush(Qt.blue)
            cursor_painter.drawEllipse(self.curr_pos, 5, 5)
            cursor_painter.drawText(QPoint(self.geometry().left() + 10, self.geometry().top() + 10), "pos: " + str(self.curr_pos))
            cursor_painter.end()

        if self.last_pos != None:
            self.points.append(self.last_pos)
            painter = QPainter()
            painter.begin(self.canvas.pixmap())
            painter.pen().setWidth(10)
            painter.setPen(Qt.red)
            for ind in range(0, len(self.points)-1):
                painter.drawLine(self.points[ind], self.points[ind+1])
            painter.end()
        
    def add_point(self):
        point = self.device.curr_point
        
        if point == None:
            return
        
        point = QPoint(point[0], point[1])
        
        if self.last_pos == None:
            self.last_pos = point
            
        self.curr_pos = point
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    spiral_painter = Spiral_Painter()
    spiral_painter.setGeometry(400,400,400,400)
    spiral_painter.show()
    app.exec_()