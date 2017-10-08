# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataSetLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataSetLabel.setObjectName("chooseDataSetLabel")
        self.gridLayout.addWidget(self.chooseDataSetLabel, 0, 0, 1, 2)
        self.chooseDataSetComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataSetComboBox.setObjectName("chooseDataSetComboBox")
        self.gridLayout.addWidget(self.chooseDataSetComboBox, 1, 0, 1, 1)
        self.variablesToWriteLabel = QtWidgets.QLabel(self.groupBox)
        self.variablesToWriteLabel.setObjectName("variablesToWriteLabel")
        self.gridLayout.addWidget(self.variablesToWriteLabel, 2, 0, 1, 1)
        self.variablesToWriteListWidget = QtWidgets.QListWidget(self.groupBox)
        self.variablesToWriteListWidget.setObjectName("variablesToWriteListWidget")
        self.gridLayout.addWidget(self.variablesToWriteListWidget, 3, 0, 1, 2)
        self.specifyAFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.specifyAFilenameLabel.setObjectName("specifyAFilenameLabel")
        self.gridLayout.addWidget(self.specifyAFilenameLabel, 4, 0, 1, 1)
        self.specifyAFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.specifyAFilenameLineEdit.setObjectName("specifyAFilenameLineEdit")
        self.gridLayout.addWidget(self.specifyAFilenameLineEdit, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Write to CSV"))
        self.chooseDataSetLabel.setText(("Choose data set to write to *.csv:"))
        self.variablesToWriteLabel.setText(("Variables to write:"))
        self.specifyAFilenameLabel.setText(("Specify a filename:"))
        self.specifyAFilenameLineEdit.setText(("output.csv"))
        self.pushButton.setText(("..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

