import bluetooth
import time
import re

class BluetoothHandler:
    def __init__(self):
        self.addr = "98:D3:31:FD:8B:99"
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = 1
        self.socket.connect((self.addr, self.port))

    def getData(self):
        r_data = self.socket.recv(8)
        r_data = r_data.decode("utf-8") # convert bytes object to string
        return r_data

    def sendData(self, t_data):
        self.socket.send(t_data)

    def pairing(self):
        paired = False
        timeout = False
        curr_time = int(time.time())
        while paired == False or timeout:
            # timeout after 5 seconds
            if int(time.time()) == curr_time + 5:
                timeout = True

            self.sendData("spairing")

            if self.getData() == "pairdone":
                paired = True

            time.sleep(0.001)

        if paired == True:
            return False

        if timeout == True:
            return False

    def startTest(self):
        started = False
        result_ready = False
        timeout = False
        curr_time = int(time.time())

        while started == False or timeout:
            # timeout after 5 seconds
            if int(time.time()) == curr_time + 5:
                timeout = True
                
            self.sendData("startnow")

            if self.getData() == "starting":
                started = True

        """
        while result_ready == False:
            data = self.getData()
            re.match(data, r"FE{}E{}")
        """

        return started

if __name__ == "__main__":
    bt_handler = BluetoothHandler()
    status = bt_handler.pairing()
    print(status)
    started = bt_handler.startTest()
    print(started)