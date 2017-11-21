# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dockWidget = QtWidgets.QDockWidget(Form)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.dockWidgetContents)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.refreshTablePushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.refreshTablePushButton.setObjectName("refreshTablePushButton")
        self.gridLayout.addWidget(self.refreshTablePushButton, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(self.dockWidgetContents)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.verticalLayout.addWidget(self.dockWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.chooseDataLabel.setText(("choose Data"))
        self.refreshTablePushButton.setText(("Refresh Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

