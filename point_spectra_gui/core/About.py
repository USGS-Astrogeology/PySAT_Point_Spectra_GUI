# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtWidgets

from point_spectra_gui.__init__ import __version__
from point_spectra_gui.ui.About import Ui_Form
import sys


class About(Ui_Form):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.versionLabel.setText("Version " + __version__)


def main():

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = About()
    ui.setupUi(Form)
    Form.show()
    app.exec_()

if __name__ == '__main__':
    main()