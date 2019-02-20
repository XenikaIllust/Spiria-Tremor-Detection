from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from engine import *
from frontend.Spiral_Painter import Spiral_Painter

PAGE_COUNT = STATE_COUNT

class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")

        self.fullscreen_dimensions = MainWindow.geometry()
        print(self.fullscreen_dimensions)

        VERTICAL_BORDERSIZE = self.fullscreen_dimensions.height() // 100
        HORIZONTAL_BORDERSIZE = self.fullscreen_dimensions.width() // 100

        font_db = QFontDatabase()
        font_db.addApplicationFont("./assets/fonts/Montserrat-SemiBold.ttf")
        #font_db.addApplicationFont("./assets/fonts/Montserrat-Regular.ttf")
        #font_db.addApplicationFont("./assets/fonts/Montserrat-Medium.ttf")
        #font_db.addApplicationFont("./assets/fonts/Montserrat-Black.ttf")
        #font_db.addApplicationFont("./assets/fonts/Montserrat-Bold.ttf")


        self.bg = QWidget(self.MainWindow)
        self.bg.setGeometry(self.MainWindow.geometry())
        self.bg.setObjectName("bg")

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
        self.setup_spiral_test_complete_screen(self.spiral_complete_test_screen)

        self.tremor_test_screen = QWidget()
        self.tremor_test_screen.setGeometry(self.frame.geometry())
        self.setup_tremor_test_screen()

        self.tremor_complete_test_screen = QWidget()
        self.tremor_complete_test_screen.setGeometry(self.frame.geometry())
        self.setup_tremor_test_complete_screen(self.tremor_complete_test_screen)

        self.questionnaire_screen = QWidget()
        self.questionnaire_screen.setGeometry(self.frame.geometry())
        self.setup_questionnaire_screen()

        self.complete_screen = QWidget()
        self.complete_screen.setGeometry(self.frame.geometry())
        self.setup_complete_screen()

        self.stacked_widget.addWidget(self.title_screen)
        self.stacked_widget.addWidget(self.pairing_screen)
        self.stacked_widget.addWidget(self.spiral_test_screen)
        self.stacked_widget.addWidget(self.spiral_complete_test_screen)
        self.stacked_widget.addWidget(self.tremor_test_screen)
        self.stacked_widget.addWidget(self.tremor_complete_test_screen)
        self.stacked_widget.addWidget(self.questionnaire_screen)
        self.stacked_widget.addWidget(self.complete_screen)

        self.debug_next_button = QPushButton(self.frame)
        self.debug_next_button.move(self.fullscreen_dimensions.width() - self.debug_next_button.width() - HORIZONTAL_BORDERSIZE,
                        VERTICAL_BORDERSIZE)
        self.debug_next_button.setText("Next")

        self.exit_button = QPushButton(self.frame)
        self.exit_button.setGeometry(QRect(self.frame.geometry().right() - self.exit_button.geometry().width(),
                                           self.frame.geometry().bottom() - self.exit_button.geometry().height(),
                                           self.exit_button.geometry().width(), self.exit_button.geometry().height()))
        print(self.exit_button.geometry())
        self.exit_button.setText("Exit")

        print(self.stacked_widget.currentIndex())

    def setup_title_screen(self):
        title_layout_widget = QWidget(self.title_screen)
        title_layout_widget.setGeometry(QRect(self.frame.geometry().width() // 3, self.frame.geometry().height() * 0.1, self.frame.geometry().width() // 3, self.frame.geometry().height() * 0.8))
        title_layout_widget.setObjectName("title_layout_widget")

        title_layout = QVBoxLayout(title_layout_widget)

        pixmap = QPixmap("./assets/images/logo.png")
        logo = QLabel(title_layout_widget)
        logo.setObjectName("logo")
        logo.setGeometry(title_layout_widget.geometry())
        logo.setPixmap(pixmap.scaled(logo.width(), logo.height(), Qt.KeepAspectRatio))
        title_layout.addWidget(logo)

        self.start_button = QPushButton(title_layout_widget)
        self.start_button.setObjectName("start_button")
        self.start_button.setText("Begin")
        title_layout.addWidget(self.start_button)


    def setup_pairing_screen(self):
        pairing_layout_widget = QWidget(self.pairing_screen)
        pairing_layout_widget.setGeometry(QRect(self.frame.geometry().width() // 3, self.frame.geometry().height() // 4,
                                        self.frame.geometry().width() // 3, self.frame.geometry().height() // 2))

        pairing_layout = QVBoxLayout(pairing_layout_widget)

        pixmap = QPixmap("./assets/images/pair1.png")
        pairing_image = QLabel(pairing_layout_widget)
        pairing_image.setObjectName("pairing_image")
        pairing_image.setGeometry(pairing_layout_widget.geometry())
        pairing_image.setPixmap(pixmap.scaled(pairing_image.width(), pairing_image.height(), Qt.KeepAspectRatio))
        pairing_layout.addWidget(pairing_image)

        pairing_text = QLineEdit(pairing_layout_widget)
        pairing_text.setObjectName("pairing_text")
        pairing_text.setText("Pairing with Device")
        pairing_text.setReadOnly(True)
        pairing_layout.addWidget(pairing_text)

        self.pairing_start_button = QPushButton(pairing_layout_widget)
        self.pairing_start_button.setObjectName("pairing_start_button")
        self.pairing_start_button.setText("START PAIRING")
        pairing_layout.addWidget(self.pairing_start_button)

        self.pairing_continue_button = QPushButton(pairing_layout_widget)
        self.pairing_continue_button.setObjectName("pairing_continue_button")
        self.pairing_continue_button.setText("CONTINUE")
        self.pairing_continue_button.setVisible(False)
        pairing_layout.addWidget(self.pairing_continue_button)


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

        self.spiral_test_drawing_widget = Spiral_Painter()
        self.spiral_test_drawing_widget.setObjectName("spiral_test_drawing_widget")
        self.spiral_test_drawing_widget.setGeometry(spiral_test_layout_widget.geometry())
        spiral_test_layout.addWidget(self.spiral_test_drawing_widget)


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
        questionnaire_layout_widget = QWidget(self.questionnaire_screen)
        questionnaire_layout_widget.setGeometry(self.frame.geometry())

        questionnaire_layout = QVBoxLayout(questionnaire_layout_widget)

        questionnaire_title = QLineEdit(questionnaire_layout_widget)
        questionnaire_title.setObjectName("questionnaire_title")
        questionnaire_title.setText("Questionnaire")
        questionnaire_title.setReadOnly(True)
        questionnaire_layout.addWidget(questionnaire_title)

    def setup_spiral_test_complete_screen(self, screen_widget):
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

        self.spiral_next_button = QPushButton(complete_test_button_layout_widget)
        self.spiral_next_button.setObjectName("spiral_next_button")
        self.spiral_next_button.setText("CONTINUE")
        complete_test_button_layout.addWidget(self.spiral_next_button)

        self.spiral_save_exit_button = QPushButton(complete_test_button_layout_widget)
        self.spiral_save_exit_button.setObjectName("save_exit_button")
        self.spiral_save_exit_button.setText("SAVE AND EXIT")
        complete_test_button_layout.addWidget(self.spiral_save_exit_button)

        complete_test_layout.addWidget(complete_test_button_layout_widget)

    def setup_tremor_test_complete_screen(self, screen_widget):
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

        self.tremor_next_button = QPushButton(complete_test_button_layout_widget)
        self.tremor_next_button.setObjectName("next_button")
        self.tremor_next_button.setText("Next")
        complete_test_button_layout.addWidget(self.tremor_next_button)

        self.tremor_save_exit_button = QPushButton(complete_test_button_layout_widget)
        self.tremor_save_exit_button.setObjectName("save_exit_button")
        self.tremor_save_exit_button.setText("Save and Exit")
        complete_test_button_layout.addWidget(self.tremor_save_exit_button)

        complete_test_layout.addWidget(complete_test_button_layout_widget)

    def setup_complete_screen(self):
        complete_layout_widget = QWidget(self.complete_screen)
        complete_layout_widget.setGeometry(self.frame.geometry())

        complete_layout = QVBoxLayout(complete_layout_widget)

        self.complete_button = QPushButton(complete_layout_widget)
        self.complete_button.setObjectName("complete_button")
        self.complete_button.setText("Finish")
        complete_layout.addWidget(self.complete_button)


    def set_screen(self, screen):
        self.stacked_widget.setCurrentIndex(screen)

    def debug_flip_page(self):
        self.set_screen((self.stacked_widget.currentIndex() + 1) % PAGE_COUNT)

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

