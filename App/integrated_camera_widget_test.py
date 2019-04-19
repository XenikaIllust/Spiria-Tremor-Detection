import sys
from backend.Camera import *
from frontend.Camera_Widget import *

from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    camera_app = Camera_Widget()
    camera = Threaded_Camera()
    camera_app.set_camera(camera)
    camera_app.show()
    app.exec_()