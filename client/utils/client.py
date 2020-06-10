# -*- coding: utf-8 -*-
__maintainer__ = "Alexandre Laurette"
__email__ = "alexandre.laurette@fixstudio.com"

from PySide2 import QtCore, QtWebSockets, QtNetwork


class Client(QtCore.QObject):
    def __init__(self, parent=None, url=None):
        super(Client, self).__init__(parent=parent)

        self.client = QtWebSockets.QWebSocket(
            origin='', version=QtWebSockets.QWebSocketProtocol.Version13,
            parent=None)
        self.client.error.connect(self.error)

        self.client.open(QtCore.QUrl("ws://%s" % url))
        self.client.pong.connect(self.on_pong)

    def do_ping(self):
        print("client: do_ping")
        self.client.ping(b"foo")

    def send_message(self, message):
        print("client: send_message")
        self.client.sendTextMessage(message)

    def send_binary_message(self, message):
        print("client: send_binary_message")
        self.client.sendBinaryMessage(message)

    def on_pong(self, elapsed_time, payload):
        print("onPong - time: %s ; payload: %s" % (elapsed_time, payload))

    def error(self, error_code):
        print("error code: %s" % error_code)
        print(self.client.errorString())

    def close(self):
        self.client.close()
