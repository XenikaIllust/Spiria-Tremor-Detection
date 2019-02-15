import bluetooth
import time
import re
import codecs

class BluetoothHandler:
    def __init__(self):
        self.addr = "98:D3:31:FD:8B:99"
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = 1
        self.socket.connect((self.addr, self.port))
        self.socket.settimeout(5)

    def getData(self, num_bytes):
            r_data = self.socket.recv(num_bytes)
            # r_data = r_data.decode("utf-8") # convert bytes object to string
            return r_data

    def sendData(self, t_data):
        self.socket.send(t_data)

    def pairing(self):
        paired = False
        timeout = False
        curr_time = int(time.time())
        
        while paired == False and timeout == False:
            print(int(time.time()) - curr_time)
            
            # timeout after 5 seconds
            if int(time.time()) >= (curr_time + 5):
                timeout = True

            self.sendData("spairing")
            
            data = self.getData(8)
            data = data.decode("utf-8")

            if data == "pairdone":
                print(data)
                paired = True

            # time.sleep(0.001)

        if paired == True:
            return True

        if timeout == True:
            return False


    def test(self):
        started = False
        result_ready = False
        timeout = False
        curr_time = int(time.time())
                
        self.sendData("startnow")

        #TODO: FIND SOURCE OF BLUETOOTH ERROR IN SPARE TIME

        while result_ready == False:
            data = self.getData(14)
            data = data.decode('utf-8')
            print("raw: ", data)
            data = data.strip()
            print("stripped: ", data)
            
            if data == "FE5.00EI":
                result_ready = True
                
        self.sendData("finished")
                
        return data
        

if __name__ == "__main__":
    bt_handler = BluetoothHandler()
    status = bt_handler.pairing()
    print(status)
    data = bt_handler.test()
    print(data)
    # started = bt_handler.startTest()
    # print(started)
