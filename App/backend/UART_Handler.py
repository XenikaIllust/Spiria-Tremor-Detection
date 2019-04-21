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
            while self.parent.stop != True:
                self.parent.queue.put(self.parent.get_point())
            self.parent.stop = True
            
    class GetQueueThread(QThread):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            
        def run(self):
            while self.parent.stop != True:
                self.parent.curr_point = self.parent.queue.get()
                self.parent.point_ready.emit()
            self.parent.stop = True
    
    def __init__(self, portname, baudrate):
        super().__init__()
        self.ser = serial.Serial(port=portname, baudrate=baudrate, timeout=1, write_timeout=1)
        self.queue = queue.Queue()
        
        self.curr_point = None
        self.stop = False
        
        self.put_queue_thread = self.PutQueueThread(self)
        self.get_queue_thread = self.GetQueueThread(self)
        
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

        if paired == True:
            return True

        return False

    def get_point(self):
        data = self.getData(9)
        
        print(data)

        if data != None:
            data = data.split(",")
            data_x = int(data[0])
            data_y = int(data[1])
            
            return (data_x, data_y)
    
    def start_threads(self):
        self.put_queue_thread.start()
        self.get_queue_thread.start()
        
    def kill_threads(self):
        self.stop = True