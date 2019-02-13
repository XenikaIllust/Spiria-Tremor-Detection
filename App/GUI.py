from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QFrame, QWidget, QStackedWidget, QHBoxLayout, QVBoxLayout, QGraphicsView, QLineEdit, QPushButton
from PyQt5.QtTest import QTest

from engine import *
from time import sleep

class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")

        self.fullscreen_dimensions = MainWindow.geometry()
        print(self.fullscreen_dimensions)

        VERTICAL_BORDERSIZE = self.fullscreen_dimensions.height() // 100
        HORIZONTAL_BORDERSIZE = self.fullscreen_dimensions.width() // 100

        self.bg = QGraphicsView(self.MainWindow)
        self.bg.setGeometry(self.MainWindow.geometry())

        self.frame = QFrame(self.MainWindow)
        self.frame.setGeometry(QRect(HORIZONTAL_BORDERSIZE, VERTICAL_BORDERSIZE,
                                     self.fullscreen_dimensions.width() - 2 * HORIZONTAL_BORDERSIZE,
                                     self.fullscreen_dimensions.height() - 2 * VERTICAL_BORDERSIZE))

        self.version = QLineEdit(self.frame)
        self.version.move(self.frame.geometry().left(), self.frame.geometry().height() - self.version.height())
        self.version.setObjectName("version")
        self.version.setText("Water Moccasin v0.01")
        self.version.setReadOnly(True)

        self.stacked_widget = QStackedWidget(self.frame)
        self.stacked_widget.setGeometry(self.frame.geometry())

        self.title_screen = QWidget()
        self.title_screen.setGeometry(self.frame.geometry())
        self.setup_title_screen()

        self.pairing_screen = QWidget()
        self.pairing_screen.setGeometry(self.frame.geometry())
        self.setup_pairing_screen()

        self.spiral_test_screen = QWidget()
        self.spiral_test_screen.setGeometry(self.frame.geometry())
        self.setup_spiral_test_screen()

        self.spiral_complete_test_screen = QWidget()
        self.spiral_complete_test_screen.setGeometry(self.frame.geometry())
        self.setup_test_complete_screen(self.spiral_complete_test_screen)

        self.tremor_test_screen = QWidget()
        self.tremor_test_screen.setGeometry(self.frame.geometry())
        self.setup_tremor_test_screen()

        #self.questionnaire_screen = QWidget()+

        self.tremor_complete_test_screen = QWidget()
        self.tremor_complete_test_screen.setGeometry(self.frame.geometry())
        self.setup_test_complete_screen(self.tremor_complete_test_screen)

        self.stacked_widget.addWidget(self.title_screen)
        self.stacked_widget.addWidget(self.pairing_screen)
        self.stacked_widget.addWidget(self.spiral_test_screen)
        self.stacked_widget.addWidget(self.spiral_complete_test_screen)
        self.stacked_widget.addWidget(self.tremor_test_screen)
        self.stacked_widget.addWidget(self.tremor_complete_test_screen)

        self.next_button = QPushButton(self.frame)
        self.next_button.move(self.fullscreen_dimensions.width() - self.next_button.width() - HORIZONTAL_BORDERSIZE,
                        VERTICAL_BORDERSIZE)
        self.next_button.setText("Next")

        self.exit_button = QPushButton(self.frame)
        self.exit_button.setGeometry(QRect(self.frame.geometry().right() - self.exit_button.geometry().width(),
                                           self.frame.geometry().bottom() - self.exit_button.geometry().height(),
                                           self.exit_button.geometry().width(), self.exit_button.geometry().height()))
        print(self.exit_button.geometry())
        self.exit_button.setText("Exit")

    def debug_flip_page(self):
        current = self.ui.stacked_widget.currentIndex()
        self.ui.set_screen(current + 1)

    def setup_title_screen(self):
        layout_widget = QWidget(self.title_screen)
        layout_widget.setGeometry(QRect(self.frame.geometry().width() // 3, self.frame.geometry().height() // 4, self.frame.geometry().width() // 3, self.frame.geometry().height() // 2))

        layout = QVBoxLayout(layout_widget)

        logo = QGraphicsView(layout_widget)
        logo.setObjectName("logo")
        logo.setFixedSize(3000, 3000)
        layout.addWidget(logo)

        title = QLineEdit(layout_widget)
        title.setObjectName("title")
        title.setText("SPIRIA")
        title.setReadOnly(True)
        layout.addWidget(title)

        subtitle = QLineEdit(layout_widget)
        subtitle.setObjectName("subtitle")
        subtitle.setText("Preliminary Parkinson's Detection Device")
        subtitle.setReadOnly(True)
        layout.addWidget(subtitle)

        start_button = QPushButton(layout_widget)
        start_button.setObjectName("start button")
        start_button.setText("Begin")
        layout.addWidget(start_button)

        layout_widget.setLayout(layout)

    def setup_pairing_screen(self):
        pairing_layout_widget = QWidget(self.pairing_screen)
        pairing_layout_widget.setGeometry(QRect(self.frame.geometry().width() // 3, self.frame.geometry().height() // 4,
                                        self.frame.geometry().width() // 3, self.frame.geometry().height() // 2))

        pairing_layout = QVBoxLayout(pairing_layout_widget)

        pairing_image = QGraphicsView(pairing_layout_widget)
        pairing_image.setObjectName("pairing_image")
        pairing_image.setFixedSize(3000, 3000)
        pairing_layout.addWidget(pairing_image)

        pairing_text = QLineEdit(pairing_layout_widget)
        pairing_text.setObjectName("title")
        pairing_text.setText("Pairing with Device")
        pairing_text.setReadOnly(True)
        pairing_layout.addWidget(pairing_text)

        pairing_layout_widget.setLayout(pairing_layout)

    def setup_spiral_test_screen(self):
        spiral_test_layout_widget = QWidget(self.spiral_test_screen)
        spiral_test_layout_widget.setGeometry(self.frame.geometry())

        spiral_test_layout = QVBoxLayout(spiral_test_layout_widget)

        spiral_test_title = QLineEdit(spiral_test_layout_widget)
        spiral_test_title.setObjectName("spiral_test_title")
        spiral_test_title.setText("Spiral Drawing Test")
        spiral_test_title.setReadOnly(True)
        spiral_test_layout.addWidget(spiral_test_title)

        spiral_test_text = QLineEdit(spiral_test_layout_widget)
        spiral_test_text.setObjectName("spiral_test_text")
        spiral_test_text.setText("Use the IR Pen to trace the spiral in the white area.")
        spiral_test_text.setReadOnly(True)
        spiral_test_layout.addWidget(spiral_test_text)

        # spiral_test_drawing_widget = Spiral_Painter()
        # spiral_test_layout.addWidget(spiral_test_drawing_widget)

    def setup_tremor_test_screen(self):
        tremor_test_layout_widget = QWidget(self.tremor_test_screen)
        tremor_test_layout_widget.setGeometry(self.frame.geometry())

        tremor_test_layout = QVBoxLayout(tremor_test_layout_widget)

        tremor_test_title = QLineEdit(tremor_test_layout_widget)
        tremor_test_title.setObjectName("tremor_test_title")
        tremor_test_title.setText("Tremor Test")
        tremor_test_title.setReadOnly(True)
        tremor_test_layout.addWidget(tremor_test_title)

        tremor_test_text = QLineEdit(tremor_test_layout_widget)
        tremor_test_text.setObjectName("tremor_test_text")
        tremor_test_text.setText("Use the IR Pen to trace the tremor in the white area.")
        tremor_test_text.setReadOnly(True)
        tremor_test_layout.addWidget(tremor_test_text)


    def setup_questionnaire_screen(self):
        pass

    def setup_test_complete_screen(self, screen_widget):
        complete_test_layout_widget = QWidget(screen_widget)
        complete_test_layout_widget.setGeometry(self.frame.geometry())

        complete_test_layout = QVBoxLayout(complete_test_layout_widget)

        complete_test_title = QLineEdit(complete_test_layout_widget)
        complete_test_title.setObjectName("complete_test_title")
        complete_test_title.setText("Test Complete")
        complete_test_title.setReadOnly(True)
        complete_test_layout.addWidget(complete_test_title)

        complete_test_text = QLineEdit(complete_test_layout_widget)
        complete_test_text.setObjectName("complete_test_text")
        complete_test_text.setText("Please click \"Continue\" to proceed or \"Save and Exit\" to save your progress and quit this session.")
        complete_test_text.setReadOnly(True)
        complete_test_layout.addWidget(complete_test_text)

        complete_test_button_layout_widget = QWidget()
        complete_test_button_layout = QHBoxLayout(complete_test_button_layout_widget)

        next_button = QPushButton(complete_test_button_layout_widget)
        next_button.setObjectName("next_button")
        next_button.setText("Next")
        complete_test_button_layout.addWidget(next_button)

        save_exit_button = QPushButton(complete_test_button_layout_widget)
        save_exit_button.setObjectName("save_exit_button")
        save_exit_button.setText("Save and Exit")
        complete_test_button_layout.addWidget(save_exit_button)

        complete_test_layout.addWidget(complete_test_button_layout_widget)

    def setup_complete_screen(self):
        pass

    def set_screen(self, screen):
        self.stacked_widget.setCurrentIndex(screen)

"""
def run():
    import sys
    app = QApplication(sys.argv)
    file = QFile("./styles/title_screen.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    MainWindow = QWidget()
    Ui = Ui_MainWindow()
    Ui.setup_ui(MainWindow)
    MainWindow.showMaximized()
    # MainWindow.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
"""

