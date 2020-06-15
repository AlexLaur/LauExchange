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
        MainWindow.resize(500, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.mailbox = QWidget()
        self.mailbox.setObjectName(u"mailbox")
        self.verticalLayout_9 = QVBoxLayout(self.mailbox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.splitter_2 = QSplitter(self.mailbox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.trw_mailbox = QTreeWidget(self.verticalLayoutWidget_2)
        self.trw_mailbox.setObjectName(u"trw_mailbox")
        self.trw_mailbox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.trw_mailbox.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.trw_mailbox.setProperty("showDropIndicator", False)
        self.trw_mailbox.setAlternatingRowColors(True)
        self.trw_mailbox.setItemsExpandable(False)

        self.verticalLayout_7.addWidget(self.trw_mailbox)

        self.splitter_2.addWidget(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget_3 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.txe_mailbox_content = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.txe_mailbox_content.setObjectName(u"txe_mailbox_content")
        self.txe_mailbox_content.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.txe_mailbox_content)

        self.pub_import_attachment = QPushButton(self.verticalLayoutWidget_3)
        self.pub_import_attachment.setObjectName(u"pub_import_attachment")

        self.verticalLayout_8.addWidget(self.pub_import_attachment)

        self.splitter_2.addWidget(self.verticalLayoutWidget_3)

        self.verticalLayout_9.addWidget(self.splitter_2)

        self.tabWidget.addTab(self.mailbox, "")
        self.outbox = QWidget()
        self.outbox.setObjectName(u"outbox")
        self.verticalLayout_6 = QVBoxLayout(self.outbox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.splitter = QSplitter(self.outbox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lie_search_receiver = QLineEdit(self.groupBox_3)
        self.lie_search_receiver.setObjectName(u"lie_search_receiver")

        self.verticalLayout_5.addWidget(self.lie_search_receiver)

        self.lst_all_receiver = QListWidget(self.groupBox_3)
        self.lst_all_receiver.setObjectName(u"lst_all_receiver")
        self.lst_all_receiver.setDragEnabled(True)
        self.lst_all_receiver.setDragDropMode(QAbstractItemView.DragDrop)
        self.lst_all_receiver.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_5.addWidget(self.lst_all_receiver)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lst_reiciver = QListWidget(self.groupBox)
        self.lst_reiciver.setObjectName(u"lst_reiciver")
        self.lst_reiciver.setDragEnabled(True)
        self.lst_reiciver.setDragDropMode(QAbstractItemView.DragDrop)
        self.lst_reiciver.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_3.addWidget(self.lst_reiciver)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txe_chat_view = QTextEdit(self.groupBox_2)
        self.txe_chat_view.setObjectName(u"txe_chat_view")
        self.txe_chat_view.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.txe_chat_view)

        self.pub_send = QPushButton(self.groupBox_2)
        self.pub_send.setObjectName(u"pub_send")

        self.verticalLayout_4.addWidget(self.pub_send)

        self.splitter.addWidget(self.groupBox_2)

        self.verticalLayout_6.addWidget(self.splitter)

        self.tabWidget.addTab(self.outbox, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LauExchange", None))
        ___qtreewidgetitem = self.trw_mailbox.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"From", None));
        self.pub_import_attachment.setText(QCoreApplication.translate("MainWindow", u"Import attachment", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mailbox), QCoreApplication.translate("MainWindow", u"Mailbox", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"All reiciver", None))
        self.lie_search_receiver.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Someone", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"To", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.pub_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.outbox), QCoreApplication.translate("MainWindow", u"Outbox", None))
    # retranslateUi

