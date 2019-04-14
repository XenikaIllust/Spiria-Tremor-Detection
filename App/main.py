"""
Spiria - A Parkinson's Preliminary Detection Experimental Device

Dependencies:
PyQt5
OpenCV-Python
Pybluez
PySerial
Picamera

To run the app: python3 main.py (However, by default configuration, the Raspberry Pi will be
configured to boot in kiosk mode.)

The app is to be run natively on Raspberry Pi with UART and Bluetooth enabled. It is configured to
pair with the custom PCBs created specifically for this device.

The files are split into the core files for the main directory, and the frontend and backend files
in their respective folders. All visual assets required by the app are stored in the assets folder.
These include images and fonts.
"""

from frontend.GUI import *
from backend.Backend_Services import *
from engine import *

class Spiria_App(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setGeometry(QApplication.desktop().screenGeometry())
        self.ui.setup_ui(self)

        self.backend_services = BackendServices()
        self.state_machine = StateMachine(self.ui, self.backend_services)

        #debug
        self.ui.exit_button.clicked.connect(self.close)


def run():
    import sys
    app = QApplication(sys.argv)
    file = QFile("./styles/title_screen.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    MainWindow = QWidget()
    spiria_app = Spiria_App(MainWindow)
    spiria_app.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()