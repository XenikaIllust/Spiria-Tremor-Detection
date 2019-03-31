from backend.Request_Handler import *
from backend.Bluetooth_Handler import *
# from backend.UART_Handler import *

class BackendServices():
    def __init__(self):
        # Comment out if not using UART
        # self.uart_handler = UART_Handler("/dev/ttyS0", 9600)

        self.request_handler = Request_Handler()

        # Comment out if not using BT
        self.bluetooth_handler = BluetoothHandler()

    def update(self, state):
        pass