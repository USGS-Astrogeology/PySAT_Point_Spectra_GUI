# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.vectorFileLabel = QtWidgets.QLabel(self.groupBox)
        self.vectorFileLabel.setObjectName("vectorFileLabel")
        self.gridLayout.addWidget(self.vectorFileLabel, 1, 0, 1, 1)
        self.vectorFileLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.vectorFileLineEdit.setObjectName("vectorFileLineEdit")
        self.gridLayout.addWidget(self.vectorFileLineEdit, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Multiply By Vector"))
        self.chooseDataLabel.setText(("Choose data"))
        self.vectorFileLabel.setText(("Vector file"))
        self.vectorFileLineEdit.setText(("*.csv"))
        self.pushButton.setText(("..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

