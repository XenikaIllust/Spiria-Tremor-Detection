from functools import partial
from PyQt5.QtCore import QThread

"""
    Backend Engine for Spiria Raspberry Pi-based Application
"""

TITLE_STATE = 0
SPIRAL_PAIRING_STATE = 1
SPIRAL_TEST_STATE = 2
SPIRAL_FINISHED_STATE = 3
TREMOR_PAIRING_STATE = 4
TREMOR_TEST_START_STATE = 5
TREMOR_TEST_STATE = 6
TREMOR_FINISHED_STATE = 7
QUESTIONNAIRE_STATE = 8
COMPLETE_STATE = 9

STATE_COUNT = 10

class Tremor_Display_Timer():
    def __init__(self, tremor_time_text):
        from PyQt5.QtCore import QTimer
        self.tremor_time_text = tremor_time_text
        self.num_seconds = 90
        self.timer = QTimer(self.tremor_time_text)
        self.timer.timeout.connect(self.timer_update)

        self.curr_time = self.num_seconds

    def timer_start(self):
        self.reset()
        self.tremor_time_text.setText(str(self.curr_time))
        self.timer.start(1000)

    def timer_update(self):
        self.tremor_time_text.setText(str(self.curr_time))
        if self.curr_time > 0:
            self.curr_time -= 1
        else:
            self.tremor_time_text.setText("Complete")
            self.timer.stop()

    def kill_timer_explicit(self):
        print("timer killed explicitly")
        self.timer.stop()

    def reset(self):
        self.curr_time = self.num_seconds

class Threaded_Tremor_Test(QThread):
    def __init__(self, backend):
        super().__init__()
        self.backend = backend
    
    def run(self):
        self.backend.bluetooth_handler.tremor_test()
        

class StateMachine():
    def __init__(self, ui, backend):
        self.ui = ui
        self.backend = backend
        
        self.tremor_timer = Tremor_Display_Timer(self.ui.tremor_time_text)
        self.threaded_tremor_test = Threaded_Tremor_Test(self.backend)
        
        self.set_button_actions()
        self.state = None
        self.set_state(TITLE_STATE)

        self.paired = False

    def set_state(self, state):
        self.state = state
        self.ui.set_screen(self.state)
        print("state: ", self.state)

    def get_state(self):
        return self.state

    def set_button_actions(self):
        self.ui.start_button.clicked.connect(partial(self.set_state, SPIRAL_PAIRING_STATE))

        # enable if UART not available
        self.ui.spiral_pairing_start_button.clicked.connect(partial(self.set_state, SPIRAL_TEST_STATE))

        # enable if UART available
        # self.ui.spiral_pairing_start_button.clicked.connect(self.tremor_pairing)
        # self.ui.spiral_pairing_failed_button.clicked.connect(partial(self.set_state, TREMOR_PAIRING_STATE))
        # self.ui.spiral_pairing_continue_button.clicked.connect(partial(self.set_state, TREMOR_TEST_STATE))

        self.ui.spiral_next_button.clicked.connect(partial(self.set_state, TREMOR_PAIRING_STATE))
        self.ui.spiral_save_exit_button.clicked.connect(partial(self.set_state, TITLE_STATE))

        # enable if BT not available
        # self.ui.tremor_pairing_start_button.clicked.connect(partial(self.set_state, TREMOR_TEST_START_STATE))

        # enable if BT available
        self.ui.tremor_pairing_start_button.clicked.connect(self.tremor_pairing)
        self.ui.tremor_pairing_failed_button.clicked.connect(partial(self.set_state, TREMOR_PAIRING_STATE))
        self.ui.tremor_pairing_continue_button.clicked.connect(partial(self.set_state, TREMOR_TEST_START_STATE))

        self.ui.tremor_test_start_button.clicked.connect(partial(self.tremor_timer.timer_start))
        self.ui.tremor_test_start_button.clicked.connect(self.threaded_tremor_test.start)
        self.ui.tremor_test_start_button.clicked.connect(partial(self.set_state, TREMOR_TEST_STATE))

        self.ui.tremor_next_button.clicked.connect(partial(self.set_state, QUESTIONNAIRE_STATE))
        self.ui.tremor_save_exit_button.clicked.connect(partial(self.set_state, TITLE_STATE))

        self.ui.questionnaire_complete_button.clicked.connect(partial(self.set_state, COMPLETE_STATE))
        self.ui.questionnaire_complete_button.clicked.connect(self.backend.questionnaire_calculator.calculate_score)

        self.ui.complete_button.clicked.connect(partial(self.set_state, TITLE_STATE))

        self.ui.debug_next_button.clicked.connect(self.ui.debug_flip_page)
        self.ui.debug_next_button.clicked.connect(self.debug_next_state)


    def spiral_pairing(self):
        status = self.backend.UART_handler.pairing()
        print("pairing status: ", status)
        self.ui.spiral_pairing_start_button.setVisible(False)
        self.ui.spiral_pairing_continue_button.setVisible(status)
        self.ui.spiral_pairing_failed_button.setVisible(not(status))

    def tremor_pairing(self):
        status = self.backend.bluetooth_handler.pairing()
        print("pairing status: ", status)
        self.ui.tremor_pairing_start_button.setVisible(False)
        self.ui.tremor_pairing_continue_button.setVisible(status)
        self.ui.tremor_pairing_failed_button.setVisible(not(status))
        
    """
    def np_tremor_test(self):
        import multiprocessing
        from queue import Queue
        queue = Queue()
        np = multiprocessing.Process(target = self.tremor_test, args=(queue,))
        np.start()
        np.join()
        data = queue.get()
        return data
    
    def tremor_test(self, queue):
        data = self.backend.bluetooth_handler.tremor_test()
        queue.put(data)
    """

    def questionnaire_calculation(self):
        pass


    def debug_next_state(self):
        self.set_state((self.state + 1) % STATE_COUNT)