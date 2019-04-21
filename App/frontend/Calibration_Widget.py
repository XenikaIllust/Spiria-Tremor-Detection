from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Calibration_Widget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.setMinimumSize(1024, 764)
        
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
        self.device.start_parallel_feed()

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
        point = self.device.curr_point

        if point == None:
            return

        if self.count < 4:
            point = QPoint(point[0], point[1])

            self.curr_pos = point
            self.points.append(self.curr_pos)
            self.count += 1
            self.update()
            
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