# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

from point_spectra_gui.ui.DataTable import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics
from point_spectra_gui.util.PandasModel import PandasModel
from point_spectra_gui.util.Worker import Worker


class DataTable(Ui_Form, Basics):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Basics.setupUi(self, Form)
        self.refreshTable = Worker(self.on_refreshTable)

    def get_widget(self):
        return self.dockWidget

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.chooseDataComboBox.currentIndexChanged.connect(lambda: self.refreshTable.start())
        self.refreshTablePushButton.clicked.connect(lambda: self.refreshTable.start())

    def function(self):
        self.on_refreshTable()

    def setDisabled(self, bool):
        """
        Override setDisabled since we don't want this table to be disabled.
        :param bool:
        :return:
        """
        pass

    def on_refreshTable(self):
        try:
            pandasModel = PandasModel(self.data[self.chooseDataComboBox.currentText()].df)
            self.tableView.setModel(pandasModel)
        except:
            print('KeyError: \'\': Cannot read from an empty string')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

