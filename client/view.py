# -*- coding: utf-8 -*-
__maintainer__ = "Alexandre Laurette"
__email__ = "alexandre.laurette@fixstudio.com"

import os
import json
import getpass
from pprint import pprint
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtMultimedia
from PySide2 import QtNetwork

from utils.client import Client
from utils import utils
from ui import main as main_ui

SCRIPT_PATH = os.path.dirname(__file__)

URL = '127.0.0.1'
PORT = 1302

class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.user = getpass.getuser()
        self.user_id = None
        self.client_manager = Client(url='%s:%s?user=%s' % (URL, PORT, self.user))
        self.notif_sound = QtMultimedia.QSound(os.path.join(SCRIPT_PATH, 'src', 'notification.wav'))

        self.pub_send.clicked.connect(self.send_message)
        # self.lie_message.returnPressed.connect(self.send_message)
        self.client_manager.client.textMessageReceived.connect(self._receive_data)

        self.commands = {
            'fetch_messages': self.fetch_messages,
            'new_message': self.new_message,
            'fetch_users': self.fetch_users,
        }

        self.timer = QtCore.QTimer()
        self.timer.singleShot(200,
                              lambda: self.client_manager.send_message(
                                  message=json.dumps(
                                      {'command': 'fetch_users'})))
        self.timer.singleShot(400,
                              lambda: self.client_manager.send_message(
                                  message=json.dumps(
                                      {'command': 'fetch_messages',
                                       'user_id': self.user_id})))

    def _send_data(self, data):
        """This private method send data to the server

        :param data: The data to send
        :type data: dict
        """
        self.client_manager.send_message(message=json.dumps(data))

    def _receive_data(self, data):
        """This private method receive data from the server and make an
        action

        :param data: The data from the server
        :type data: str
        """
        data = json.loads(data)
        self.commands[data['command']](data=data['result'])

    def fetch_users(self, data):
        """This method get all users and build the list of receiver

        :param data: The list of users
        :type data: list
        """
        pprint(data)
        for user in data:
            if user[1] == self.user:
                self.user_id = user[0]
                continue
            item = QtWidgets.QListWidgetItem(self.lst_all_receiver)
            item.setText(user[1])
            item.setData(32, user[0])
            self.lst_all_receiver.addItem(item)

    def fetch_messages(self, data):
        pprint(data)

    def new_message(self, data):
        """This method is called when a new message from the server is here

        :param data: The data of the message
        :type data: dict
        """
        if self.hasFocus():
            self.notif_sound.play()
        # self.txe_chat_view.append('<b>%s</b>: %s' % (data['author'], data['content']))
        pprint(data)

    def send_message(self):
        """This method send a new message
        """
        to_users = utils.get_all_list_items(list_widget=self.lst_reiciver)
        to = [item.data(32) for item in to_users]
        if not to:
            return
        message = self.txe_chat_view.toPlainText()
        data = {'command': 'new_message',
                'data': {'from': self.user, 'content': message, 'to': to}}
        self._send_data(data=data)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()