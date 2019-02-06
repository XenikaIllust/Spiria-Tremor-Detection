from PyQt5.QtCore import QFile, QRect, QTextStream
from PyQt5.QtWidgets import QApplication
from GUI import *

class Spiria_App(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setGeometry(QApplication.desktop().screenGeometry())
        self.ui.setup_ui(self)

        self.ui.exit_button.clicked.connect(self.close)
        self.ui.next_button.clicked.connect(self.flip_page)

    def flip_page(self):
        current = self.ui.stacked_widget.currentIndex()
        self.ui.stacked_widget.setCurrentIndex(current + 1)


def run():
    import sys
    app = QApplication(sys.argv)
    file = QFile("./styles/title_screen.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    MainWindow = QWidget()
    spiria_app = Spiria_App(MainWindow)
    spiria_app.showFullScreen()
    # spiria_app.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()