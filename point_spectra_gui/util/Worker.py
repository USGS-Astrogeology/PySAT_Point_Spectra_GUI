from PyQt5 import QtCore

from PyQt5.QtCore import QThread


class Worker(QThread):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self, func, parent=None):
        QThread.__init__(self, parent)
        self.func = func

    def __del__(self):
        self.wait()

    def run(self):
        self.func()
