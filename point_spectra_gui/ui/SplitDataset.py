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
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseDataLabel)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseDataComboBox)
        self.splitOnUniqueValuesOfLabel = QtWidgets.QLabel(self.formGroupBox)
        self.splitOnUniqueValuesOfLabel.setObjectName("splitOnUniqueValuesOfLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.splitOnUniqueValuesOfLabel)
        self.splitOnUniqueValuesOfComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.splitOnUniqueValuesOfComboBox.setObjectName("splitOnUniqueValuesOfComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.splitOnUniqueValuesOfComboBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Split Dataset"))
        self.chooseDataLabel.setText(("Choose Data"))
        self.splitOnUniqueValuesOfLabel.setText(("Split on unique values of"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

