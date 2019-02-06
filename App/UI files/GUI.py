# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 910)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1051, 861))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1031, 831))
        self.stackedWidget.setObjectName("stackedWidget")
        self.title_page = QtWidgets.QWidget()
        self.title_page.setObjectName("title_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.title_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 230, 501, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.stackedWidget.addWidget(self.title_page)
        self.pairing_page = QtWidgets.QWidget()
        self.pairing_page.setObjectName("pairing_page")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.pairing_page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 200, 501, 401))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logo_3 = QtWidgets.QGraphicsView(self.verticalLayoutWidget_2)
        self.logo_3.setObjectName("logo_3")
        self.verticalLayout_3.addWidget(self.logo_3)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_3.addWidget(self.lineEdit_6)
        self.stackedWidget.addWidget(self.pairing_page)
        self.version = QtWidgets.QLineEdit(self.frame)
        self.version.setGeometry(QtCore.QRect(10, 830, 113, 27))
        self.version.setObjectName("version")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

