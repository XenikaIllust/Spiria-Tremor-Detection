from backend.Request_Handler import *
from backend.BluetoothHandler import *


class BackendServices():
    def __init__(self):
        # Comment out if not using UART
        self.uart_listener = UART_Talker(9600)

        self.request_handler = Request_Handler()

        # Comment out if not using BT
        # self.bluetooth_handler = BluetoothHandler()

    def update(self, state):
        pass