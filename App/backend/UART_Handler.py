import serial
import time
import queue
# import cv2
import numpy as np
# from Homographer import *
from threading import Thread
from functools import partial

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UART_Handler(QObject):
    point_ready = pyqtSignal()
    
    class PutQueueThread(QThread):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            
        def run(self):
            while True:
                self.parent.queue.put(self.parent.get_point())
            
    class GetQueueThread(QThread):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            
        def run(self):
            while True:
                self.parent.curr_point = self.parent.queue.get()
                self.parent.point_ready.emit()
                # tablet_event = PointReadyEvent(self.parent.curr_point)
                # tablet_event = QMouseEvent(QEvent.MouseButtonPress, QPoint(0, 0), 0, Qt.LeftButton, Qt.NoModifier)
                # status = QCoreApplication.postEvent(self.parent, tablet_event)
                # QCoreApplication.sendPostedEvents(self.parent, 0)
    
    def __init__(self, portname, baudrate):
        super().__init__()
        self.ser = serial.Serial(port=portname, baudrate=baudrate, timeout=1, write_timeout=1)
        self.queue = queue.Queue()
        
        self.curr_point = None
        
        self.put_queue_thread = self.PutQueueThread(self)
        self.get_queue_thread = self.GetQueueThread(self)
        
        self.start_parallel_feed()
        
        # self.homographer = Homographer()

    def enable(self):
        self.ser.open()

    def disable(self):
        self.ser.close()

    def getData(self, num_bytes):
        data = self.ser.read(num_bytes)
        data = data.decode("utf-8")
        return data

    def sendData(self, data):
        data = bytes(data.encode("utf-8"))
        self.ser.write(data)

    def pairing(self):
        paired = False
        timeout = False
        
        while paired == False and timeout == False:
            self.sendData("spairing")
            
            data = None
            try:
                data = self.getData(8)
            except:
                pass
            
            if data == "":
                timeout = True

            if data == "pairdone":
                paired = True

            # time.sleep(0.001)

        if paired == True:
            return True

        return False

    def get_point(self):
        data = self.getData(9)

        if data != None:
            data = data.split(",")
            data_x = int(data[0])
            data_y = int(data[1])

        return (data_x, data_y)

    def calibration(self, dest_geometry):
        self.calib_pts_src = np.array([])

        # obtain calibration points
        for i in range(0, 4):
            np.append(self.calib_pts_src, self.get_point())

        self.calib_pts_dest = np.array([[dest_geometry.left(), dest_geometry.top()],
                                        [dest_geometry.right(), dest_geometry.top()],
                                        [dest_geometry.right(), dest_geometry.bottom()],
                                        [dest_geometry.left(), dest_geometry.bottom()]])

        # self.transform = self.homographer.get_homography_matrix(self.calib_pts_src, self.calib_pts_dest)
    
    """
    def loop_load_queue(self):
        while True:
            self.queue.put(self.get_point())
    
    def loop_get_queue(self):
        while True:
            self.curr_point = self.queue.get()
            self.point_ready.emit()
    """
    
    def start_parallel_feed(self):
        self.put_queue_thread.start()
        self.get_queue_thread.start()
        
    """
    def customEvent(self, event):
        print("event running")
        print(event)
        if event.type == QEvent:
            print("signal triggered")
            print(event.point)
    """