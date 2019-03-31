import serial
import time
# import cv2
import numpy as np
from Homographer import *

class UART_Handler():
    def __init__(self, portname, baudrate):
        self.ser = serial.Serial(port=portname, baudrate=baudrate, timeout=1, write_timeout=1)
        self.homographer = Homographer()

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

    def get_point(self):
        data = self.getData(9)

        if data != None:
            data = data.split(",")
            data_x = int(data[0])
            data_y = int(data[1])
            
        if data_x == 1023 and data_y == 1023:
            raise ValueError("Invalid Point")

        return [data_x, data_y]

    def calibration(self, dest_geometry):
        self.calib_pts_src = np.array([])

        # obtain calibration points
        for i in range(0, 4):
            np.append(self.calib_pts_src, self.get_point())

        self.calib_pts_dest = np.array([[dest_geometry.left(), dest_geometry.top()],
                                        [dest_geometry.right(), dest_geometry.top()],
                                        [dest_geometry.right(), dest_geometry.bottom()],
                                        [dest_geometry.left(), dest_geometry.bottom()]])

        self.transform = self.homographer.get_homography_matrix(self.calib_pts_src, self.calib_pts_dest)

            
if __name__ == "__main__":
    uart_handler = UART_Handler("/dev/ttyS0", 9600)
    # status = uart_handler.pairing()

    points = []

    while True:
        point = uart_handler.get_point()
        print(point)