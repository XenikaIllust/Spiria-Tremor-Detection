from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from backend.UART_Handler import *
from backend.Homographer import Homographer
import math

class Calibration_Widget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.setMinimumSize(1024, 768)
        
        self.setup_ui()

        self.points = []
        self.count = 0

    def setup_ui(self):
        self.canvas = QLabel(self)
        self.canvas_pixmap = QPixmap(self.width(), self.height()).scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.canvas_pixmap.fill(Qt.black)
        self.canvas.setPixmap(self.canvas_pixmap)

    def set_paint_device(self, device):
        self.device = device
        self.device.point_ready.connect(self.add_point)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self.canvas.pixmap())
        painter.pen().setWidth(100)
        painter.setPen(Qt.red)
        painter.setBrush(Qt.red)

        for i, point in enumerate(self.points):
            painter.drawEllipse(point, 5, 5)

            if i > 0:
                painter.drawLine(self.points[i-1], self.points[i])
            if i == 3:
                painter.drawLine(self.points[0], self.points[i])

        painter.end()

    def add_point(self):
        def distance(point1, point2):
            return math.sqrt((point1.x() - point2.x()) ** 2 + (point1.y() - point2.y()) ** 2)
    
        point = self.device.curr_point
        
        if point[1] == 1023:
            point = QPoint(point[0], 0)
        else:
            point = QPoint(point[0], 1023 - point[1] - 255)

        if point == None:
            return
        
        if point.x() == 1023 and point.y() == 0:
            return
        
        if len(self.points) > 0 and distance(point, self.points[len(self.points) - 1]) < 100:
            return
        
        print(self.points)
        print(len(self.points))

        if self.count < 4:
            self.curr_pos = point
            self.points.append(self.curr_pos)
            self.count += 1
            self.update()
            
    def points_to_array(self):
        return [[self.points[0][0], self.points[0][1]],
                [self.points[1][0], self.points[1][1]],
                [self.points[2][0], self.points[2][1]],
                [self.points[3][0], self.points[3][1]]]
            
    def reset_points(self):
        self.points = []
        self.count = 0
        painter = QPainter()
        painter.begin(self.canvas.pixmap())
        print("resetting " + str(self.geometry()))
        painter.fillRect(0, 0, self.geometry().width(), self.geometry().height(), Qt.black)
        painter.end()
        self.update()

    def mousePressEvent(self, event):
        if self.count < 4:
            self.curr_pos = event.pos()
            self.points.append(self.curr_pos)
            self.count += 1
            self.update()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    spiral_painter = Calibration_Widget()
    reset_button = QPushButton(spiral_painter)
    reset_button.setText("Reset Points")
    reset_button.clicked.connect(spiral_painter.reset_points)
    spiral_painter.show()
    app.exec_()