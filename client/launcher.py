from PySide2 import QtCore, QtGui, QtWidgets
import view

def run_nuke():
    app = QtWidgets.QApplication.instance()
    def getMainWindow():
        for widget in app.topLevelWidgets():
            if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
                return widget
    main_window = getMainWindow()

    window = view.MainWindow(main_window)
    window.show()


def run_maya():
    from maya.app.general import mayaMixin
    import view

    class LauExchange(mayaMixin.MayaQWidgetBaseMixin, view.MainWindow):
        def __init__(self, parent=None):
            super(LauExchange, self).__init__()

    window = LauExchange()
    window.show()

