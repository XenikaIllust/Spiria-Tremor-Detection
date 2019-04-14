from picamera import PiCamera
from picamera.array import PiRGBArray
from PyQt5.QtCore import QObject, pyqtSignal, QThread
import time
import numpy as np
import cv2

class Threaded_Camera(QObject):
    frame_ready = pyqtSignal()
    
    class Worker(QThread):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            
        def run(self):
            self.parent.get_video_frame()
    
    def __init__(self):
        super().__init__()
        self.camera = PiCamera()
        self.camera.resolution = (320, 240)
        self.rawCapture = PiRGBArray(self.camera)
        self.frame = None
        time.sleep(0.1)
        
        self.worker = self.Worker(self)
        
        self.stop = False
        
    def get_video_frame(self):
        for frame in self.camera.capture_continuous(self.rawCapture, format='rgb', use_video_port=True):
            self.rawCapture.truncate(0)
            if self.stop == True:
                self.stop = False
                break
            
            self.frame = frame.array
            self.frame_ready.emit()
            
    def run_threads(self):
        self.worker.start()
            
    def kill_threads(self):
        self.stop = True
    
    
    