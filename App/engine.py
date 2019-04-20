from functools import partial
from PyQt5.QtCore import QThread, pyqtSignal, QObject

"""
    Backend Engine for Spiria Raspberry Pi-based Application
"""

TITLE_STATE = 0
SPIRAL_PAIRING_STATE = 1
SPIRAL_CALIBRATION_STATE = 2
SPIRAL_TEST_STATE = 3
SPIRAL_FINISHED_STATE = 4
TREMOR_PAIRING_STATE = 5
TREMOR_TEST_START_STATE = 6
TREMOR_TEST_STATE = 7
TREMOR_FINISHED_STATE = 8
QUESTIONNAIRE_STATE = 9
COMPLETE_STATE = 10

STATE_COUNT = 11

class Thread_Sentinel(QObject):
    run_threads = pyqtSignal()
    kill_threads = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.qthreads = None
    
    def connect(self, run_function, kill_function):
        try:
            self.run_threads.connect(run_function)
            self.kill_threads.connect(kill_function)
        except:
            pass
        
    def disconnect(self):
        try:
            self.run_threads.disconnect()
            self.kill_threads.disconnect()
        except:
            pass        
        
    def run_all_threads(self):
        self.run_threads.emit()
    
    def kill_all_threads(self):
        self.kill_threads.emit()

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
        
class State():
    def __init__(self, ID, run_function, kill_function):
        self.ID = ID
        self.run_function = run_function
        self.kill_function = kill_function

class StateMachine():
    def __init__(self, ui, backend):
        self.ui = ui
        self.backend = backend

        self.title_state = State(TITLE_STATE, None, None)
        self.spiral_pairing_state = State(SPIRAL_PAIRING_STATE, None, None)

        # uncomment if need to use picam
        self.calibration_state = State(SPIRAL_CALIBRATION_STATE, self.backend.camera.run_threads, self.backend.camera.kill_threads)
        # self.calibration_state = State(SPIRAL_CALIBRATION_STATE, None, None)
        
        # Comment out if UART not enabled
        # self.spiral_test_state = State(SPIRAL_TEST_STATE, self.backend.uart_handler.qthreads)
        # Comment out if UART enabled
        self.spiral_test_state = State(SPIRAL_TEST_STATE, None, None)
        
        self.spiral_finished_state = State(SPIRAL_FINISHED_STATE, None, None)
        self.tremor_pairing_state = State(TREMOR_PAIRING_STATE, None, None)
        self.tremor_test_start_state = State(TREMOR_TEST_START_STATE, None, None)
        self.tremor_test_state = State(TREMOR_TEST_STATE, None, None)
        self.tremor_finished_state = State(TREMOR_FINISHED_STATE, None, None)
        self.questionnaire_state = State(QUESTIONNAIRE_STATE, None, None)
        self.complete_state = State(COMPLETE_STATE, None, None)
        
        self.states = [self.title_state, self.spiral_pairing_state, self.calibration_state,
                       self.spiral_test_state, self.spiral_finished_state, self.tremor_pairing_state,
                       self.tremor_test_start_state, self.tremor_test_state, self.tremor_finished_state,
                       self.questionnaire_state, self.complete_state]
        
        self.tremor_timer = Tremor_Display_Timer(self.ui.tremor_time_text)
        self.threaded_tremor_test = Threaded_Tremor_Test(self.backend)
        
        self.thread_sentinel = Thread_Sentinel()
        
        self.set_button_actions()
        self.state = None
        self.set_state(TITLE_STATE)

        self.paired = False

    def set_state(self, state_id):
        self.thread_sentinel.kill_all_threads()
        self.thread_sentinel.disconnect()
        self.state = self.states[state_id]
        self.ui.set_screen(self.state.ID)
        print("state: ", self.state.ID)
        self.thread_sentinel.connect(self.states[state_id].run_function, self.states[state_id].kill_function)
        self.thread_sentinel.run_all_threads()

    def get_state(self):
        return self.state

    def set_button_actions(self):
        self.ui.start_button.clicked.connect(partial(self.set_state, SPIRAL_PAIRING_STATE))

        # enable if UART not available
        self.ui.spiral_pairing_start_button.clicked.connect(partial(self.set_state, SPIRAL_CALIBRATION_STATE))

        # enable if UART available
        # self.ui.spiral_pairing_start_button.clicked.connect(self.spiral_pairing)
        # self.ui.spiral_pairing_failed_button.clicked.connect(partial(self.set_state, SPIRAL_PAIRING_STATE))
        # self.ui.spiral_pairing_continue_button.clicked.connect(partial(self.set_state, SPIRAL_CALIBRATION_STATE))
        # self.ui.spiral_painter.set_paint_device(self.backend.uart_handler)

        # enable if camera available
        self.ui.camera_widget.set_camera(self.backend.camera)

        self.ui.spiral_next_button.clicked.connect(partial(self.set_state, TREMOR_PAIRING_STATE))
        self.ui.spiral_save_exit_button.clicked.connect(partial(self.set_state, TITLE_STATE))

        # enable if BT not available
        self.ui.tremor_pairing_start_button.clicked.connect(partial(self.set_state, TREMOR_TEST_START_STATE))

        # enable if BT available
        # self.ui.tremor_pairing_start_button.clicked.connect(self.tremor_pairing)
        # self.ui.tremor_pairing_failed_button.clicked.connect(partial(self.set_state, TREMOR_PAIRING_STATE))
        # self.ui.tremor_pairing_continue_button.clicked.connect(partial(self.set_state, TREMOR_TEST_START_STATE))

        self.ui.tremor_test_start_button.clicked.connect(partial(self.tremor_timer.timer_start))
        # enable if bluetooth available
        # self.ui.tremor_test_start_button.clicked.connect(self.threaded_tremor_test.start)
        self.ui.tremor_test_start_button.clicked.connect(partial(self.set_state, TREMOR_TEST_STATE))

        self.ui.tremor_next_button.clicked.connect(partial(self.set_state, QUESTIONNAIRE_STATE))
        self.ui.tremor_save_exit_button.clicked.connect(partial(self.set_state, TITLE_STATE))

        self.ui.questionnaire_complete_button.clicked.connect(partial(self.set_state, COMPLETE_STATE))
        self.ui.questionnaire_complete_button.clicked.connect(partial(self.backend.questionnaire_calculator.calculate_score,
                                                                      self.ui.questionnaire_grouped_buttons))

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

    def debug_next_state(self):
        self.set_state((self.state.ID + 1) % STATE_COUNT)