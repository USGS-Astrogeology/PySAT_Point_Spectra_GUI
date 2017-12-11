# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataLabel = QtWidgets.QLabel(Form)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(Form)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.refreshTablePushButton = QtWidgets.QPushButton(Form)
        self.refreshTablePushButton.setObjectName("refreshTablePushButton")
        self.gridLayout.addWidget(self.refreshTablePushButton, 2, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 4, 0, 1, 2)
        self.refreshDataPushButton = QtWidgets.QPushButton(Form)
        self.refreshDataPushButton.setObjectName("refreshDataPushButton")
        self.gridLayout.addWidget(self.refreshDataPushButton, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.chooseDataLabel.setText(("Choose Data"))
        self.refreshTablePushButton.setText(("Refresh Table"))
        self.refreshDataPushButton.setText(("Refresh Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

