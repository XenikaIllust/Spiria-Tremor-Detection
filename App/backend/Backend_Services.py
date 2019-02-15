from backend.Request_Handler import *
from backend.BluetoothHandler import *


class BackendServices():
    def __init__(self):
        # self.uart_listener = UART_Talker()
        self.request_handler = Request_Handler()
        self.bluetooth_handler = BluetoothHandler()

    def update(self, state):
        pass