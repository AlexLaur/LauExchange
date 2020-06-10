# -*- coding: utf-8 -*-
__maintainer__ = "Alexandre Laurette"
__email__ = "alexandre.laurette@fixstudio.com"

import os
import json
import getpass
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtMultimedia

from utils.client import Client
from ui import main as main_ui

SCRIPT_PATH = os.path.dirname(__file__)

URL = '127.0.0.1'
PORT = 1302
CHANNEL = ''

class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.user = getpass.getuser()
        # self.user = 'rrootmaster'
        self.client_manager = Client(url='%s:%s?user=%s' % (URL, PORT, self.user))
        self.notif_sound = QtMultimedia.QSound(os.path.join(SCRIPT_PATH, 'src', 'notification.wav'))

        self.pub_send.clicked.connect(self.send_data)
        self.lie_message.returnPressed.connect(self.send_data)
        self.client_manager.client.textMessageReceived.connect(self.receive_data)

    def send_data(self):
        message = self.lie_message.text()
        data = {'author': self.user, 'content':message}
        self.client_manager.send_message(message=json.dumps(data))
        self.lie_message.clear()

    def receive_data(self, data):
        if self.hasFocus():
            self.notif_sound.play()
        data = json.loads(data)
        self.txe_chat_view.append('<b>%s</b>: %s' % (data['author'], data['content']))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()