from UART_Handler import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

if __name__ == "__main__":
    uart_handler = UART_Handler("/dev/ttyS0", 9600)
    # status = uart_handler.pairing()
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(1,1,1)

    ax1.set_xlim([0, 1023])
    ax1.set_ylim([0, 1023])
        
    sc = ax1.scatter([], [], c="r")
    
    points = []
    
    def init():
        return [sc]

    def update(i):
        point = None
        try:
            point = uart_handler.get_point()
        except ValueError as e:
            return [sc]
        
        sc.set_offsets(np.array([point]))
        return [sc]


    ani = animation.FuncAnimation(fig, update, init_func=init, interval=4, blit=True)
    plt.show()
    
    
    """
    while True:
        point = uart_handler.get_point()
        print(point)
    """
