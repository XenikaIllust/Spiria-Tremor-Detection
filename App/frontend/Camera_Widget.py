from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Camera_Widget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setMinimumSize(320, 240)
        self.label = QLabel(self)
        self.label.setGeometry(self.geometry())
        
    def set_camera(self, camera):
        self.camera = camera
        self.camera.frame_ready.connect(self.update)
        
    def update(self):
        frame = self.camera.frame
        image = QImage(frame.data, 320, 240, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)