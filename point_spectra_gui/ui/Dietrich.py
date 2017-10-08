# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupbox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.halfWindowLabel = QtWidgets.QLabel(self.groupbox)
        self.halfWindowLabel.setObjectName("halfWindowLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.halfWindowLabel)
        self.halfWindowSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.halfWindowSpinBox.setObjectName("halfWindowSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.halfWindowSpinBox)
        self.numOfErosionsLabel = QtWidgets.QLabel(self.groupbox)
        self.numOfErosionsLabel.setObjectName("numOfErosionsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfErosionsLabel)
        self.numOfErosionsSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.numOfErosionsSpinBox.setObjectName("numOfErosionsSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfErosionsSpinBox)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.halfWindowLabel.setText(("Half Window:"))
        self.numOfErosionsLabel.setText(("Num of Erosions:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

