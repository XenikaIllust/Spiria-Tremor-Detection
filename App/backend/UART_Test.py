from UART_Handler import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from .frontend.Spiral_Painter import *

class Test_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.uart_handler = UART_Handler("/dev/ttyS0", 9600)
        # status = uart_handler.pairing()
    
        self.display()
        
        self.uart_handler.point_ready.connect(self.get_point)
        self.uart_handler.start_parallel_feed()
        
    def keyPressEvent(self, event):
        print("pressed keyboard")
        if event.key() == Qt.Key_Return:
            print("pressed enter")
            self.uart_handler.kill_threads()
            
    def get_point(self):
        return self.uart_handler.curr_point
    
    """
    def display(self):
        fig = plt.figure()
    
        ax1 = fig.add_subplot(1,1,1)

        ax1.set_xlim([0, 1023])
        ax1.set_ylim([0, 1023])
            
        sc = ax1.scatter([], [], c="r")
        
        points = []
        
        def init():
            return [sc]

        def update(i):
            point = None
            try:
                point = self.get_point()
            except ValueError as e:
                return [sc]
            
            sc.set_offsets(np.array([point]))
            return [sc]


        ani = animation.FuncAnimation(fig, update, init_func=init, interval=4, blit=True)
        plt.show()
    """
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    spiral_painter = Spiral_Painter()
    spiral_painter.setGeometry(400,400,400,400)
    spiral_painter.show()
    app.exec_()
    # status = uart_handler.pairing()
