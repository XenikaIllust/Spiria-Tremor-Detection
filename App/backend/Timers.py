from PyQt5.QtCore import QTimer

# Timer for Title Screen
class Title_Timer():
    def __init__(self):
        num_seconds = 5
        self.timer = QTimer()
        
    def start(self):
        self.timer.stop()
        self.timer.start(num_seconds * 1000)

# Timer for Display in Tremor Test
class Tremor_Display_Timer():
    def __init__(self, tremor_time_text):
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

# Wrapper Class for All Timers
class Timers():
    def __init__(self):
        self.title_timer = Title_Timer()
        self.tremor_display_timer = Tremor_Display_Timer()