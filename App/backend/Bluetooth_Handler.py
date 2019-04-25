import bluetooth
import time
import re
import codecs
from PyQt5.QtCore import *

BT1 = "98:D3:41:FD:42:B8"
BT2 = "98:D3:31:FD:8B:99"
BT4 = "98:D3:51:FD:86:88"

class BluetoothHandler(QObject):
    finished = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self.addr = BT1
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = 1
        self.socket.connect((self.addr, self.port))
        self.socket.settimeout(5)
        
        self.tremor_frequency = None

    def getData(self, num_bytes):
            r_data = self.socket.recv(num_bytes)
            # r_data = r_data.decode("utf-8") # convert bytes object to string
            print(r_data)
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
            
            data = None
            try:
                data = self.getData(8)
                data = data.decode("utf-8")
            except:
                pass

            if data == "pairdone":
                print(data)
                paired = True

            # time.sleep(0.001)

        if paired == True:
            return True

        return False


    def tremor_test(self):        
        started = False
        result_ready = False
        timeout = False
        curr_time = int(time.time())
                
        self.sendData("startnow")

        #TODO: FIND SOURCE OF BLUETOOTH ERROR IN SPARE TIME

        data_str = ""
        while result_ready == False:
            if len(data_str) > 50:
                data_str = ""
            
            data = self.getData(8)
            data = data.decode('utf-8')
            data_str += data
            
            searches = re.search(r"FE(\d{1,3}\.?\d{0,2})EI", data_str)
            
            if searches != None and len(searches.groups()) > 0:
                result_ready = True
                
        self.sendData("finished")
        
        print(searches.group(1))
        
        self.tremor_frequency = float(searches.group(1))
        print(self.tremor_frequency)
        
        self.finished.emit()
        
    def get_frequency(self):
        print(self.tremor_frequency)
        return self.tremor_frequency

if __name__ == "__main__":
    bt_handler = BluetoothHandler()
    status = bt_handler.pairing()
    print(status)
    data = bt_handler.tremor_test()
    print(data)
