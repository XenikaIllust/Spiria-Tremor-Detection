from UART_Handler import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

if __name__ == "__main__":
    uart_handler = UART_Handler("/dev/ttyS0", 9600)
    # status = uart_handler.pairing()

    """
    x_pt = 0
    y_pt = 0

    ax = plt.axes(xlim=(0,1023), ylim=(0,1023))

    h1, = plt.plot([], [])

    pts = None
    
    while True:
        point = uart_handler.get_point()
        
        if point == None:
            continue
        
        x_pt = point[0]
        y_pt = point[1]

        h1.set_xdata(x_pt)
        h1.set_ydata(y_pt)

        # if pts != None:
        #    pts.remove()

        pts = plt.scatter(x_pt, y_pt, c="r")

        plt.draw()
        plt.pause(0.0001)
    """
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(1,1,1)

    ax1.set_xlim([0, 1023])
    ax1.set_ylim([0, 1023])
        
    sc = ax1.scatter([], [], c="r")
    
    def init():
        sc.set_offsets(np.array([[-1,-1]]))
        
        return [sc]

    def update(i):
        ts1 = time.perf_counter()
        point = None
        try:
            point = uart_handler.get_point()
        except ValueError as e:
            print(e)
            sc.set_offsets(np.array([[-1,-1]]))
            return [sc]

        x_pt = point[0]
        y_pt = point[1]

        # if pts != None:
        #     pts.remove()
        
        sc.set_offsets(np.array([x_pt, y_pt]))
        ts2 = time.perf_counter()
        print("update time: ", ts2-ts1)
        return [sc]


    ani = animation.FuncAnimation(fig, update, init_func=init, interval=0, blit=True)
    plt.show()
    
    
    """
    while True:
        point = uart_handler.get_point()
        print(point)
    """
