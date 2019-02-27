import serial
import time

class UART_Handler():
    def __init__(self, portname, baudrate):
        self.ser = serial.Serial(port=portname, baudrate=baudrate, timeout=5, write_timeout=5)

    def enable(self):
        self.ser.open()

    def disable(self):
        self.ser.close()

    def getData(self, num_bytes):
        data = self.ser.read(num_bytes)
        data = data.decode("utf-8")
        return data

    def sendData(self, data):
        data = bytes(data.encode("utf-8"))
        self.ser.write(data)

    def pairing(self):
        paired = False
        timeout = False
        
        while paired == False and timeout == False:
            self.sendData("spairing")
            
            data = None
            try:
                data = self.getData(8)
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

    def get_coordinates(self, stop, points):
        invalid = False
        while stop != True:
            data_x = int(self.getData(4))
            data_y = int(self.getData(4))

            if data_x == 1023 and data_y == 1023:
                invalid = True

            if invalid == False:
                points.append((data_x, data_y))

            
if __name__ == "__main__":
    uart_listener = UART_Handler("/dev/ttyS0", 9600)
    print(uart_listener.pairing())