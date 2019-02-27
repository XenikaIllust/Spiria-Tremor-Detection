import serial
import time

class UART_Talker():
    def __init__(self, portname, baudrate):
        self.ser = serial.Serial(port=portname, baudrate=baudrate, timeout=5, write_timeout=5)

    def enable(self):
        self.ser.open()

    def disable(self):
        self.ser.close()

    def getData(self, num_bytes):
        return self.ser.read(num_bytes)

    def sendData(self, data):
        self.ser.write(data)

    def pairing(self):
        paired = False
        timeout = False
        curr_time = int(time.time())
        
        while paired == False and timeout == False:
            self.sendData(bytes("spairing".encode("utf-8")))
            
            data = None
            try:
                data = self.getData(8)
                data = data.decode("utf-8")
            except:
                pass
            
            print(data)
            
            if data == "":
                timeout = True

            if data == "pairdone":
                paired = True

            # time.sleep(0.001)

        if paired == True:
            return True

        return False
            
if __name__ == "__main__":
    uart_listener = UART_Talker("/dev/ttyS0", 9600)
    print(uart_listener.pairing())
        