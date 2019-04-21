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
        self.uart_handler.start_threads()
        self.transform_device = Homographer()
        self.transform_device.set_source_points([[88, 210], [465, 72], [886, 383], [460, 604]])
        self.transform_device.set_destination_points([[self.geometry().left(), self.geometry().top()],
                                               [self.geometry().right(), self.geometry().top()],
                                               [self.geometry().right(), self.geometry().bottom()],
                                               [self.geometry().left(), self.geometry().bottom()]])
        self.transform_device.calculate_homography()
        
    def add_point(self):
        point = self.uart_handler.curr_point
        
        if point == None:
            return
        
        point = QPoint(point[0], 1023 - point[1])
        print("unedited point: " + str(point))
        point = QPoint(self.transform_device.transform_coordinates([point.x(), point.y()]))
        print("edited point: " + str(point))
        
        if self.last_pos == None:
            self.last_pos = point
            
        self.curr_pos = point
        self.update()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    integrated_spiral_painter = Integrated_Spiral_Painter()
    integrated_spiral_painter.setGeometry(0,0,693,660)
    integrated_spiral_painter.show()
    app.exec_()
    # status = uart_handler.pairing()