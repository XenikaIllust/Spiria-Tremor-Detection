#! /usr/bin/python3

from GUI import *
from UART_Talker import *
from Request_Handler import *

"""
    Backend Engine for Spiria Raspberry Pi-based Application
"""

TITLE_STATE = 0
PAIRING_STATE = 1
SPIRAL_TEST_STATE = 2
SPIRAL_FINISHED_STATE = 3
TREMOR_TEST_STATE = 4
TREMOR_FINISHED_STATE = 4
QUESTIONNAIRE_STATE = 5
COMPLETE_STATE = 6

class StateMachine():
    def __init__(self):
        self.state = TITLE_STATE

    def set_state(self, state):
        self.state = state

        if self.state == TITLE_STATE:
            pass
        elif self.state == PAIRING_STATE:
            pass
        elif self.state == SPIRAL_TEST_STATE:
            pass
        elif self.state == SPIRAL_FINISHED_STATE:
            pass
        elif self.state == TREMOR_TEST_STATE:
            pass
        elif self.state == TREMOR_FINISHED_STATE:
            pass
        elif self.state == QUESTIONNAIRE_STATE:
            pass
        elif self.state == COMPLETE_STATE:
            pass

    def get_state(self):
        return self.state


class BackendServices():
    def __init__(self):
        self.uart_listener = UART_Talker()
        self.request_handler = Request_Handler()

    def update(self, state):
        pass


def spiral_evaluate():
    pass

def tremor_evaluate():
    pass

def questionnaire_evaluate():
    pass

def result_evaluate():
    pass