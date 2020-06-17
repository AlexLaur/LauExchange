# -*- coding: utf-8 -*-
import os
import json
import getpass
import importlib
from datetime import datetime
from pprint import pprint
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtMultimedia
from PySide2 import QtNetwork

from utils.client import Client
from utils import custom_widgets as cw
from utils import utils
from ui import main as main_ui

__maintainer__ = "Alexandre Laurette"
__email__ = "laurette.alexandre@gmail.com"

SCRIPT_PATH = os.path.dirname(__file__)

URL = '127.0.0.1'
PORT = 1302
PATH_ATTACHMENT = '/users_roaming/alaurette/Documents/TESTS/attachements/'

class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None, software=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        # CONSTANTS
        self.user = getpass.getuser()
        self.software = software
        if self.software:
            mod = '.softs.%s.attachment' % self.software
            self.attachment_module = importlib.import_module(mod, 'client')
        # self.user = 'helloworld'
        # self.notif_sound = QtMultimedia.QSound(
        #     os.path.join(SCRIPT_PATH, 'src', 'notification.wav'))

        self.commands = {
            'fetch_messages': self.fetch_messages,
            'fetch_users': self.fetch_users,
            'new_message': self.new_message,
        }

        # CLIENT
        url = '%s:%s?user=%s' % (URL, PORT, self.user)
        self.client_manager = Client(url=url)

        # MAILBOX HEADER
        header_mailbox = QtWidgets.QHeaderView(
            QtCore.Qt.Horizontal, self.trw_mailbox)
        self.trw_mailbox.setHeader(header_mailbox)
        header_mailbox.setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        header_mailbox.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        header_mailbox.setSectionsClickable(True)

        # CASCADING STYLE SHEET
        self.set_style_sheet()

        # SIGNALS
        self.client_manager.client.textMessageReceived.connect(
            self._receive_data)

        self.pub_import_attachment.clicked.connect(self.import_attachment)
        self.pub_send.clicked.connect(self.send_message)
        self.lie_search_receiver.textChanged.connect(self.search_receiver)
        self.trw_mailbox.itemClicked.connect(self.show_message_from_mailbox)
        self.trw_mailbox.customContextMenuRequested.connect(
            self.context_menu_mailbox)

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

# RECEIVE FROM SERVER

    def fetch_users(self, data):
        """This method get all users and build the list of receiver

        :param data: The list of users
        :type data: list
        """
        for user in data:
            if user[1] == self.user:
                continue
            item = QtWidgets.QListWidgetItem(self.lst_all_receiver)
            item.setText(user[1])
            item.setData(32, user)
            self.lst_all_receiver.addItem(item)

    def fetch_messages(self, data):
        for message in data:
            message_id = message[0]
            message_content = message[1]
            message_sender_id = message[7]
            message_sender_username = message[8]
            message_attachment = message[4]
            message_readed = message[5]
            message_timestamp = message[6]
            dt_object = datetime.fromtimestamp(message_timestamp)
            item = cw.TreeWidgetItem(parent=self.trw_mailbox,
                                     text=[message_sender_username,
                                           str(dt_object)],
                                     message_id=message_id,
                                     content=message_content,
                                     attachment=message_attachment,
                                     readed=message_readed,
                                     checkable=True)
            self.trw_mailbox.addTopLevelItem(item)
        self.eval_mailbox()


    def new_message(self, data):
        """This method is called when a new message from the server is here

        :param data: The data of the message
        :type data: dict
        """
        if self.hasFocus():
            pass
            # self.notif_sound.play()
        dt_object = datetime.fromtimestamp(data['timestamp'])
        item = cw.TreeWidgetItem(parent=self.trw_mailbox,
                                 text=[data['sender'][1], str(dt_object)],
                                 message_id=data['id'],
                                 content=data['content'],
                                 attachment=data['attachment'],
                                 readed=0,
                                 checkable=True)
        self.trw_mailbox.addTopLevelItem(item)

# EMIT TO SERVER

    def send_message(self):
        """This method send a new message"""
        receivers = utils.get_all_list_items(list_widget=self.lst_receiver)
        to = [item.data(32) for item in receivers]
        if not to:
            return
        attachement = self.generate_attachment()
        data = {'sender': self.user,
                'content': self.txe_chat_view.toPlainText(),
                'attachment':attachement,
                'receiver': to,
                }
        command = {'command': 'new_message', 'data': data}
        self._send_data(data=command)
        self.clean_up_outbox()

    def show_message_from_mailbox(self, item):
        self.txe_mailbox_content.clear()
        message_content = item.content
        if not item.readed:
            item.readed = 1
            # item.setData(0, QtCore.Qt.BackgroundRole, None)
            command = {'command': 'message_readed',
                       'message_id': item.message_id}
            self._send_data(data=command)
        self.txe_mailbox_content.setPlainText(message_content)
        self.eval_mailbox()

    def delete_messages(self):
        """This method delete messages on the detabase"""
        all_messages = utils.get_all_tree_items(tree_widget=self.trw_mailbox)
        to_delete = []
        for message in all_messages:
            if message.checkState(0) == QtCore.Qt.Checked:
                to_delete.append(message.message_id)
                self.trw_mailbox.invisibleRootItem().removeChild(message)
        command = {'command': 'message_delete', 'messages': to_delete}
        if to_delete:
            self._send_data(data=command)

    def import_attachment(self):
        """This method import the attachment into the software

        :return: The path of the attachment
        :rtype: str or None
        """
        if self.software:
            item = self.trw_mailbox.currentItem()
            return self.attachment_module.run_import(path=item.attachment)
        return None

    def generate_attachment(self):
        """This method export the attachment from the software

        :return: The path of the attachment
        :rtype: str or None
        """
        if self.software:
            return self.attachment_module.run_export(path=PATH_ATTACHMENT)
        return None

# UTILS

    def eval_mailbox(self):
        """This method eval the number of unread messages and update the text
        on the the tab"""
        all_messages = utils.get_all_tree_items(tree_widget=self.trw_mailbox)
        unread = len([x for x in all_messages if x.readed != 1])
        if unread:
            text = 'Mailbox (%s)' % unread
            self.tabWidget.setTabText(
                self.tabWidget.indexOf(self.mailbox), text)

    def search_receiver(self):
        """This function is a simple filter for receiver"""
        filter_text = self.lie_search_receiver.text()
        items = self.lst_all_receiver.findItems(
            filter_text, QtCore.Qt.MatchContains)
        all_items = utils.get_all_list_items(list_widget=self.lst_all_receiver)
        utils.filter_listwidget(
            all_items=all_items, finding_item=items, text=filter_text)

    def clean_up_outbox(self):
        """This method clean up the outbox page after a mail."""
        self.txe_chat_view.clear()
        all_items = utils.get_all_list_items(list_widget=self.lst_receiver)
        for receiver in all_items:
            row = self.lst_receiver.row(receiver)
            item = self.lst_receiver.takeItem(row)
            self.lst_all_receiver.addItem(item)

    def set_style_sheet(self):
        """This function load the cascading style sheet (CSS) for the app"""
        self.style = utils.load_style_sheet(script_path=SCRIPT_PATH)
        self.setStyleSheet(self.style)

    def context_menu_mailbox(self, event):
        """This function create a menu when the user right click
        on the treewidget bbox assigner

        :param event: event obj
        :return: None
        """
        menu = QtWidgets.QMenu(self.trw_mailbox)
        delete_selected = menu.addAction('Delete selected messages.')
        delete_selected.triggered.connect(self.delete_messages)
        menu.exec_(QtGui.QCursor.pos())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
