from threading import Thread
from random import randint
import time

"""
class Worker(Thread):
    def __init__(self, val):
        super().__init__()
        self.val = val
        
    def run(self):
        for i in range(3):
            print('Value %d in thread %s\n' % (self.val, self.getName()))
 
            # Sleep for random time between 1 ~ 3 second
            secondsToSleep = randint(1, 5)
            print('%s sleeping fo %d seconds...\n' % (self.getName(), secondsToSleep))
            time.sleep(secondsToSleep)
        
worker1 = Worker(3)
worker1.setName("worker1")

worker2 = Worker(4)
worker2.setName("worker2")

worker1.start()
worker2.start()

worker1.join()
worker2.join()
"""

import threading
import time


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background')

            time.sleep(self.interval)

example = ThreadingExample()
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')
        