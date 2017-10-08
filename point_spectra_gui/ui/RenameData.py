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
        self.renameDataLabel = QtWidgets.QLabel(self.groupBox)
        self.renameDataLabel.setObjectName("renameDataLabel")
        self.gridLayout.addWidget(self.renameDataLabel, 0, 0, 1, 1)
        self.renameDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.renameDataComboBox.setObjectName("renameDataComboBox")
        self.gridLayout.addWidget(self.renameDataComboBox, 0, 1, 1, 1)
        self.toDataLabel = QtWidgets.QLabel(self.groupBox)
        self.toDataLabel.setObjectName("toDataLabel")
        self.gridLayout.addWidget(self.toDataLabel, 0, 2, 1, 1)
        self.toDataLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.toDataLineEdit.setObjectName("toDataLineEdit")
        self.gridLayout.addWidget(self.toDataLineEdit, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Rename Data Set"))
        self.renameDataLabel.setText(("Rename Data"))
        self.toDataLabel.setText(("to"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

