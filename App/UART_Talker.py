#! /usr/bin/python3

import serial

class UART_Talker():
    def __init__(self, portname, baudrate):
        self.port = serial.Serial(portname)
        self.port.baudrate = baudrate

    def enable(self):
        self.port.open()

    def disable(self):
        self.port.close()

    def getData(self):
        pass

    def sendData(self):
        pass

    def pairing(self):
        pass

    def close(self):
        self.port.close()