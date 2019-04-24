import sys
from backend.UART_Handler import *
from backend.Homographer import Homographer
from frontend.Calibration_Widget import *

from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uart_handler = UART_Handler("/dev/ttyS0", 9600)
    uart_handler.run_threads()
    calibration_widget = Calibration_Widget()
    calibration_widget.set_paint_device(uart_handler)
    reset_button = QPushButton(calibration_widget)
    reset_button.setText("Reset Points")
    reset_button.clicked.connect(calibration_widget.reset_points)
    calibration_widget.show()
    app.exec_()