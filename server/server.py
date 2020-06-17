# -*- coding: utf-8 -*-
import argparse
import sqlite3
import signal
import json
import os
from time import time
from PySide2 import QtCore, QtWebSockets, QtNetwork, QtGui
from PySide2 import QtWidgets

from libs import utils
from libs import models

__maintainer__ = 'Alexandre Laurette'
__email__ = 'alexandre.laurette@fixstudio.com'

SERVER_PATH = os.path.dirname(__file__)

class WebSocketServer(QtCore.QObject):
    def __init__(self, parent, host=None, port=None):
        super(QtCore.QObject, self).__init__()
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

        self.server.newConnection.connect(self._on_new_connection)

        self.db_connection = sqlite3.connect(
            os.path.join(SERVER_PATH, 'db', 'database.db'))

    def _on_new_connection(self):
        # Get the client
        self.client_connection = self.server.nextPendingConnection()
        self.client_connection.textMessageReceived.connect(
            self.process_text_data)
        self.client_connection.binaryMessageReceived.connect(
            self.process_binary_data)
        self.client_connection.disconnected.connect(self._socket_disconnected)
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

        # Init the app by sending all users and last messages
        self.fetch_users()
        self.fetch_messages(user=client_user)

    def _socket_disconnected(self):
        if self.client_connection:
            old_client = None
            for user_id, client in self.clients_dict.items():
                if client != self.client_connection:
                    continue
                old_client = user_id
            self.clients_dict.pop(old_client, None)
            self.client_connection.deleteLater()

    def process_text_data(self, data):
        data = json.loads(data)
        if data['command'] == 'new_message':
            self.new_message(data=data['data'])
        elif data['command'] == 'fetch_users':
            self.fetch_users()
        elif data['command'] == 'fetch_messages':
            self.fetch_messages(user=data['user'])
        elif data['command'] == 'message_readed':
            models.update_message_read(db_connection=self.db_connection,
                                       message_id=data['message_id'])
        elif data['command'] == 'message_delete':
            self.delete_message(data=data['messages'])

    def process_binary_data(self, data):
        print("b:", data)
        if self.client_connection:
            self.client_connection.sendBinaryMessage(data)

    def fetch_users(self):
        all_users = models.get_all_users(db_connection=self.db_connection)
        result = {'command': 'fetch_users', 'result': all_users}
        if self.client_connection:
            self.client_connection.sendTextMessage(json.dumps(result))

    def fetch_messages(self, user):
        user = models.get_user(db_connection=self.db_connection,
                               user_username=user)
        messages = models.get_messages_for_user(
            db_connection=self.db_connection, user_id=user[0])
        result = {'command': 'fetch_messages', 'result': messages}
        if self.client_connection:
            self.client_connection.sendTextMessage(json.dumps(result))

    def new_message(self, data):
        timestamp = int(time()) # only seconds
        sender = models.get_user(db_connection=self.db_connection,
                                 user_username=data['sender'])
        for to in data['receiver']:
            receiver = to[0]
            message_id = models.create_message(
                db_connection=self.db_connection, sender=sender[0],
                receiver=receiver, content=data['content'],
                attachment=data['attachment'], timestamp=timestamp)
            result = {'command': 'new_message',
                      'result': {
                          'id': message_id,
                          'sender': sender,
                          'content': data['content'],
                          'attachment':data['attachment'],
                          'timestamp': timestamp,
                          },
                      }
            if self.client_connection:
                if receiver in self.clients_dict:
                    self.clients_dict[receiver].sendTextMessage(json.dumps(result))


    def delete_message(self, data):
        for message_id in data:
            models.delete_message(db_connection=self.db_connection,
                                  message_id=message_id)



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Launch Websocket server !\n',
                                     epilog='--host 10.10.9.69 --port 1302')
    parser.add_argument('--host', type=str, help='host', default='127.0.0.1')
    parser.add_argument('--port', type=int, help='port', default=1302)
    args = parser.parse_args()

    app = QtWidgets.QApplication([])
    signal.signal(signal.SIGINT, signal.SIG_DFL) # ENABLE CTRL+C to stop
    serverObject = QtWebSockets.QWebSocketServer(
        'LauExchange', QtWebSockets.QWebSocketServer.NonSecureMode)
    server = WebSocketServer(serverObject, host=args.host, port=args.port)
    serverObject.closed.connect(app.quit)
    app.exec_()