# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/users_roaming/alaurette/Desktop/Documents/WebScocketPyside/client/ui/main.ui'
#
# Created: Fri Jun  5 15:03:52 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txe_chat_view = QtWidgets.QTextEdit(self.centralwidget)
        self.txe_chat_view.setReadOnly(True)
        self.txe_chat_view.setObjectName("txe_chat_view")
        self.verticalLayout.addWidget(self.txe_chat_view)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lie_message = QtWidgets.QLineEdit(self.centralwidget)
        self.lie_message.setObjectName("lie_message")
        self.horizontalLayout.addWidget(self.lie_message)
        self.pub_send = QtWidgets.QPushButton(self.centralwidget)
        self.pub_send.setObjectName("pub_send")
        self.horizontalLayout.addWidget(self.pub_send)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pub_send.setText(QtWidgets.QApplication.translate("MainWindow", "Send", None, -1))

