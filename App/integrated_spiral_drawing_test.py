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
        self.set_paint_device(self.uart_handler)
        self.transform_device = Homographer()
        self.transform_device.set_source_points(self.give_source_points)
        self.transform_device.set_destination_points(self.give_dest_points)
        self.transform_device.calculate_homography()
        
        self.points = []
        
        self.clicked = False
        
    def give_source_points(self):
        return [QPoint(0, 255), QPoint(1023, 255), QPoint(1023, 1023), QPoint(0, 1023)]
        
    def give_dest_points(self):
        return [self.geometry().topLeft(),
                self.geometry().topRight(),
                self.geometry().bottomRight(),
                self.geometry().bottomLeft()]
        
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
            
        if len(self.points) == 200:
            self.save_drawing()
    
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    integrated_spiral_painter = Integrated_Spiral_Painter()
    integrated_spiral_painter.setGeometry(0,0,693,660)
    # integrated_spiral_painter.setGeometry(0, 0, 1024, 768)
    integrated_spiral_painter.show()
    app.exec_()
    # status = uart_handler.pairing()