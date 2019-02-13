#! /usr/bin/python3

import bluetooth
import time

class BluetoothHandler:
    def __init__(self):
        self.addr = "98:D3:31:FD:8B:99"
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = 1
        self.socket.connect((self.addr, self.port))

    def getData(self):
        r_data = self.socket.recv(9)
        r_data = r_data.decode("utf-8") # convert bytes object to string
        return r_data

    def sendData(self, t_data):
        self.socket.send(t_data)

    def pairing(self):
        paired = False
        timeout = False
        while paired == False or timeout:
            # timeout after 5 seconds

            self.sendData("spairing")

            if self.getData() == "pairdone":
                paired = False

        if timeout == True:
            return False

        return True




    def close(self):
        self.port.close()