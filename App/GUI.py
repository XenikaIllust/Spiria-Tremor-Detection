from PyQt5.QtCore import QRect, QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QGraphicsView, QTextEdit

from engine import *

class Ui_MainWindow(object):
    def __init__(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")

        self.fullscreen_dimensions = app.desktop().screenGeometry()

        self.clear_screen(MainWindow)
        self.title_screen(MainWindow)

    def title_screen(self, MainWindow):
        self.layout = QGridLayout(MainWindow)
        self.layout.setGeometry(self.fullscreen_dimensions)

        self.bg = QGraphicsView(MainWindow)
        self.bg.setGeometry(QRect(self.fullscreen_dimensions))
        self.bg.setObjectName("bg")

        self.logo = QGraphicsView(MainWindow)
        self.logo.setGeometry(QRect(370, 220, 256, 192))
        self.logo.setObjectName("logo")

        self.title = QTextEdit(MainWindow)
        self.title.setGeometry(QRect(410, 490, 104, 75))
        self.title.setObjectName("title")
        self.title.setText("SPIRIA")
        self.title.setReadOnly(True)

        self.subtitle = QTextEdit(MainWindow)
        self.subtitle.setGeometry(QRect(410, 630, 104, 75))
        self.subtitle.setObjectName("subtitle")
        self.subtitle.setText("Preliminary Parkinson's Detection Device")
        self.subtitle.setReadOnly(True)

    def pairing_screen(self, MainWindow):
        self.fullscreen = QGraphicsView(MainWindow)
        self.fullscreen.setGeometry(QRect(MainWindow.geometry()))
        self.fullscreen.setObjectName("fullscreen")

    def spiral_test_screen(self, MainWindow):
        self.fullscreen = QGraphicsView(MainWindow)
        self.fullscreen.setGeometry(QRect(MainWindow.geometry()))
        self.fullscreen.setObjectName("fullscreen")

    def tremor_test_screen(self, MainWindow):
        self.fullscreen = QGraphicsView(MainWindow)
        self.fullscreen.setGeometry(QRect(MainWindow.geometry()))
        self.fullscreen.setObjectName("fullscreen")

    def questionnaire_screen(self, MainWindow):
        self.fullscreen = QGraphicsView(MainWindow)
        self.fullscreen.setGeometry(QRect(MainWindow.geometry()))
        self.fullscreen.setObjectName("fullscreen")

    def transition(self, MainWindow):
        self.fullscreen = QGraphicsView(MainWindow)
        self.fullscreen.setGeometry(QRect(MainWindow.geometry()))
        self.fullscreen.setObjectName("fullscreen")

    def clear_screen(self, MainWindow):
        self.fullscreen = QGraphicsView(MainWindow)
        self.fullscreen.setGeometry(QRect(MainWindow.geometry()))
        self.fullscreen.setObjectName("fullscreen")

def run():
    import sys
    app = QApplication(sys.argv)
    file = QFile("./styles/title_screen.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    MainWindow = QWidget()
    Ui_MainWindow(MainWindow, app)
    MainWindow.showMaximized()
    # MainWindow.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()


