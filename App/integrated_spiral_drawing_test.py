from backend.UART_Handler import *
from backend.Homographer import Homographer
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from frontend.Spiral_Painter import *

class Integrated_Spiral_Painter(Spiral_Painter):
    def __init__(self):
        super().__init__()
        self.uart_handler = UART_Handler("/dev/ttyS0", 9600)
        # status = uart_handler.pairing()
        
        self.uart_handler.point_ready.connect(self.add_point)
        self.uart_handler.run_threads()
        self.transform_device = Homographer()
        self.transform_device.set_source_points([QPoint(0, 255), QPoint(1023, 255), QPoint(1023, 1023), QPoint(0, 1023)])
        # self.transform_device.set_destination_points([[0, 0], [693, 0], [693, 660], [0, 660]])
        self.transform_device.set_destination_points([self.geometry().topLeft(),
                                                      self.geometry().topRight(),
                                                      self.geometry().bottomRight(),
                                                      self.geometry().bottomLeft()])
        self.transform_device.calculate_homography()
        
        self.points = []
        
        self.clicked = False
        
    def paintEvent(self, event):
        self.canvas.pixmap().fill(Qt.transparent)
        if self.curr_pos != None:
            cursor_painter = QPainter()
            cursor_painter.begin(self.canvas.pixmap())
            cursor_painter.pen().setWidth(100)
            cursor_painter.setPen(Qt.blue)
            cursor_painter.setBrush(Qt.blue)
            # cursor_painter.drawEllipse(self.curr_pos, 5, 5)
            for point in self.points:
                cursor_painter.drawEllipse(point, 5, 5)
            cursor_painter.drawText(QPoint(self.geometry().left() + 10, self.geometry().top() + 10), "pos: " + str(self.curr_pos))
            cursor_painter.end()
    
        '''
        if self.last_pos != None:
            self.points.append(self.last_pos)
            painter = QPainter()
            painter.begin(self.canvas.pixmap())
            painter.pen().setWidth(10)
            painter.setPen(Qt.blue)
            for ind in range(0, len(self.points)-1):
                painter.drawLine(self.points[ind], self.points[ind+1])
            painter.end()
        '''
    
    def add_point(self):
        point = self.uart_handler.curr_point
        
        if point == None:
            return
        
        point = QPoint(point[0], 1023 - point[1])
        print("unedited point: " + str(point))
        transformed_point = self.transform_device.transform_coordinates([[point.x(), point.y(), 1]])
        print(transformed_point)
        point = QPoint(transformed_point[0], transformed_point[1])
        print("edited point: " + str(point))
        
        if self.last_pos == None:
            self.last_pos = point
            
        self.curr_pos = point
        self.points.append(self.curr_pos)
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    integrated_spiral_painter = Integrated_Spiral_Painter()
    # integrated_spiral_painter.setGeometry(0,0,693,660)
    # integrated_spiral_painter.setGeometry(0, 0, 1024, 768)
    integrated_spiral_painter.show()
    app.exec_()
    # status = uart_handler.pairing()