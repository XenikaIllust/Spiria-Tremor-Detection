from frontend.GUI import *
from backend.Backend_Services import *
from engine import *

'''
TODO: 
Spiral Painter Spiral Adjustment
Establish server
Test google cloud machine learning functions
'''

class Spiria_App(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setGeometry(QApplication.desktop().screenGeometry())
        self.ui.setup_ui(self)

        self.backend_services = BackendServices()
        self.state_machine = StateMachine(self.ui, self.backend_services)

        self.ui.exit_button.clicked.connect(self.close)


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