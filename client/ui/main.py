# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 468)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.mailbox = QWidget()
        self.mailbox.setObjectName(u"mailbox")
        self.verticalLayout_2 = QVBoxLayout(self.mailbox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txe_chat_view = QTextEdit(self.mailbox)
        self.txe_chat_view.setObjectName(u"txe_chat_view")
        self.txe_chat_view.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.txe_chat_view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.lie_message = QLineEdit(self.mailbox)
        self.lie_message.setObjectName(u"lie_message")

        self.horizontalLayout.addWidget(self.lie_message)

        self.pub_send = QPushButton(self.mailbox)
        self.pub_send.setObjectName(u"pub_send")

        self.horizontalLayout.addWidget(self.pub_send)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.mailbox, "")
        self.outbox = QWidget()
        self.outbox.setObjectName(u"outbox")
        self.tabWidget.addTab(self.outbox, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 578, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pub_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mailbox), QCoreApplication.translate("MainWindow", u"Mailbox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.outbox), QCoreApplication.translate("MainWindow", u"Outbox", None))
    # retranslateUi

