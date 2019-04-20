from backend.Request_Handler import *
from backend.Bluetooth_Handler import *
from backend.UART_Handler import *
from backend.Homographer import *
from backend.Questionnaire_Score_Calculation import *
from backend.Camera import Threaded_Camera

class BackendServices():
    def __init__(self):
        # Comment out if not using UART
        # self.uart_handler = UART_Handler("/dev/ttyS0", 9600)

        self.camera = Threaded_Camera()
        self.request_handler = Request_Handler()

        # Comment out if not using BT
        # self.bluetooth_handler = BluetoothHandler()

        self.questionnaire_calculator = Questionnaire_Calculator()

    def update(self, state):
        pass