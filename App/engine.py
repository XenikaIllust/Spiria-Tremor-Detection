from functools import partial

"""
    Backend Engine for Spiria Raspberry Pi-based Application
"""

TITLE_STATE = 0
PAIRING_STATE = 1
SPIRAL_TEST_STATE = 2
SPIRAL_FINISHED_STATE = 3
TREMOR_TEST_STATE = 4
TREMOR_FINISHED_STATE = 5
QUESTIONNAIRE_STATE = 6
COMPLETE_STATE = 7

STATE_COUNT = 8

class StateMachine():
    def __init__(self, ui, backend):
        self.ui = ui
        self.backend = backend
        self.set_actions()
        self.state = None
        self.set_state(TITLE_STATE)

    def set_state(self, state):
        self.state = state
        print("state: ", self.state)

        # self.update()

    def get_state(self):
        return self.state

    def set_actions(self):
        self.ui.start_button.clicked.connect(partial(self.ui.set_screen, PAIRING_STATE))
        self.ui.start_button.clicked.connect(partial(self.set_state, PAIRING_STATE))

        self.ui.debug_pairing_next_button.clicked.connect(partial(self.ui.set_screen, SPIRAL_TEST_STATE))
        self.ui.debug_pairing_next_button.clicked.connect(partial(self.set_state, SPIRAL_TEST_STATE))

        self.ui.spiral_next_button.clicked.connect(partial(self.set_state, TREMOR_TEST_STATE))
        self.ui.spiral_next_button.clicked.connect(partial(self.ui.set_screen, TREMOR_TEST_STATE))
        self.ui.spiral_save_exit_button.clicked.connect(partial(self.set_state, TITLE_STATE))
        self.ui.spiral_save_exit_button.clicked.connect(partial(self.ui.set_screen, TITLE_STATE))

        self.ui.debug_next_button.clicked.connect(self.ui.debug_flip_page)
        self.ui.debug_next_button.clicked.connect(self.debug_next_state)

    def update(self):
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

    def debug_next_state(self):
        self.set_state((self.state + 1) % STATE_COUNT)