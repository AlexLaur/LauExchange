# -*- coding: utf-8 -*-
import argparse
import sqlite3
import signal
import os
from PySide2 import QtCore, QtWebSockets, QtNetwork, QtGui
from PySide2 import QtWidgets

from libs import utils
from libs import models

__maintainer__ = 'Alexandre Laurette'
__email__ = 'alexandre.laurette@fixstudio.com'

SERVER_PATH = os.path.dirname(__file__)

class WebSocketServer(QtCore.QObject):
    def __init__(self, parent, host=None, port=None):
        super(QtCore.QObject, self).__init__(parent)
        # CONSTANTS
        self.clients_dict = {}
        self.client_connection = None

        self.server = QtWebSockets.QWebSocketServer(parent.serverName(),
                                                    parent.secureMode(),
                                                    parent)
        if self.server.listen(QtNetwork.QHostAddress(host), port):
            print('Connected: %s : %s:%s' % (
                self.server.serverName(),
                self.server.serverAddress().toString(),
                str(self.server.serverPort())))

        self.server.newConnection.connect(self.on_new_connection)

        self.db_connection = sqlite3.connect(
            os.path.join(SERVER_PATH, 'db', 'database.db'))

    def on_new_connection(self):
        # Get the client
        self.client_connection = self.server.nextPendingConnection()
        self.client_connection.textMessageReceived.connect(
            self.process_text_data)
        self.client_connection.binaryMessageReceived.connect(
            self.process_binary_data)
        self.client_connection.disconnected.connect(self.socket_disconnected)
        # Get url parameters
        params = utils.get_params_from_url(
            url=self.client_connection.requestUrl().url())
        client_user = params['user'][0]
        # Retrieve user in the database
        user_db = models.get_user(
            db_connection=self.db_connection, user_username=client_user)
        if not user_db:
            user_id = models.create_user(
                db_connection=self.db_connection, user_username=client_user)
        else:
            user_id = user_db[0]
        # Store the current client
        self.clients_dict[user_id] = self.client_connection

    def process_text_data(self, data):
        if self.client_connection:
            for user_id, client in self.clients_dict.items():
                client.sendTextMessage(data)

    def process_binary_data(self, data):
        print("b:", data)
        if self.client_connection:
            self.client_connection.sendBinaryMessage(data)

    def socket_disconnected(self):
        if self.client_connection:
            for user_id, client in self.clients_dict.items():
                if client != self.client_connection:
                    continue
                self.clients_dict.pop(user_id, None)
            self.client_connection.deleteLater()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Launch Websocket server !\n',
                                     epilog='--host 10.10.9.69 --port 1302')
    parser.add_argument('--host', type=str, help='host', default='127.0.0.1')
    parser.add_argument('--port', type=int, help='port', default=1302)
    args = parser.parse_args()

    app = QtWidgets.QApplication([])
    signal.signal(signal.SIGINT, signal.SIG_DFL) # ENABLE CTRL+C to stop
    serverObject = QtWebSockets.QWebSocketServer(
        'My Socket', QtWebSockets.QWebSocketServer.NonSecureMode)
    server = WebSocketServer(serverObject, host=args.host, port=args.port)
    serverObject.closed.connect(app.quit)
    app.exec_()