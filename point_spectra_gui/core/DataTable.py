# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtWidgets

from point_spectra_gui.ui.DataTable import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics
from point_spectra_gui.util.PandasModel import PandasModel
from point_spectra_gui.util.Worker import Worker


class DataTable(QtWidgets.QWidget, Ui_Form, Basics):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.connectWidgets()
        self.refreshTable = Worker(self.on_refreshTable)

    def get_widget(self):
        return self.dockWidget

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.chooseDataComboBox.currentIndexChanged.connect(lambda: self.on_refreshTable())
        self.refreshDataPushButton.clicked.connect(lambda: self.connectWidgets())
        self.refreshTablePushButton.clicked.connect(lambda: self.on_refreshTable())

    def on_refreshTable(self):
        try:
            pandasModel = PandasModel(self.data[self.chooseDataComboBox.currentText()].df)
            self.tableView.setModel(pandasModel)
        except:
            print('KeyError: \'\': Cannot read from an empty string')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = DataTable()
    Form.show()
    sys.exit(app.exec_())
