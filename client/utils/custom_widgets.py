from PySide2 import QtCore, QtGui, QtWidgets

class TreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent=None, text=None, **kwargs):
        super(TreeWidgetItem, self).__init__(parent, text)
        self.__dict__.update(kwargs)

        readed = kwargs.get('readed', 1)
        checkable = kwargs.get('checkable', True)

        if checkable:
            self.setCheckState(0, QtCore.Qt.Unchecked)

        # if not readed:
        #     self.setBackgroundColor(0, QtGui.QColor(98, 144, 200))
        #     self.setBackgroundColor(1, QtGui.QColor(98, 144, 200))
