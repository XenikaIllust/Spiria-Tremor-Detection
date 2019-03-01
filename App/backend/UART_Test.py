from UART_Handler import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

if __name__ == "__main__":
    # uart_handler = UART_Handler("/dev/ttyS0", 9600)
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

    def animate(i):
        point = uart_handler.get_point()

        x_pt = point[0]
        y_pt = point[1]

        # if pts != None:
        #     pts.remove()

        ax1.clear()
        ax1.scatter(x_pt, y_pt, c="r")
        ax1.set_xlim([0, 1023])
        ax1.set_ylim([0, 1023])


    ani = animation.FuncAnimation(fig, animate, interval=1)
    plt.show()
