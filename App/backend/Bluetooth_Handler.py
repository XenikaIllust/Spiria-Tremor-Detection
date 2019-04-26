import bluetooth
import time
import re
import codecs
from PyQt5.QtCore import *

BT1 = "98:D3:41:FD:42:B8"
BT2 = "98:D3:31:FD:8B:99"
BT4 = "98:D3:51:FD:86:88"

class BluetoothHandler(QObject):
    test_finished = pyqtSignal()
    
    class Threaded_Tremor_Test(QThread):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
    
        def run(self):
            self.parent.tremor_test()
    
    def __init__(self):
        super().__init__()
        
        self.addr = BT1
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.port = 1
        self.socket.connect((self.addr, self.port))
        self.socket.settimeout(5)
        
        self.threaded_tremor_test = self.Threaded_Tremor_Test(self)
        self.tremor_frequency = None

    def getData(self, num_bytes):
        r_data = self.socket.recv(num_bytes)
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
        result_ready = False
                
        self.sendData("startnow")

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
        
        self.test_finished.emit()
        
    def get_frequency(self):
        print(self.tremor_frequency)
        return self.tremor_frequency

if __name__ == "__main__":
    from functools import partial
    def print_result(bt_handler):
        print("final: " + str(bt_handler.tremor_frequency))
        
    bt_handler = BluetoothHandler()
    bt_handler.finished.connect(partial(print_result, bt_handler))
    status = bt_handler.pairing()
    print(status)
    bt_handler.threaded_tremor_test.start()
    
