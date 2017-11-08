# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.dataSet1Label = QtWidgets.QLabel(self.formGroupBox)
        self.dataSet1Label.setObjectName("dataSet1Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dataSet1Label)
        self.dataSet1ComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.dataSet1ComboBox.setObjectName("dataSet1ComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dataSet1ComboBox)
        self.dataSet2Label = QtWidgets.QLabel(self.formGroupBox)
        self.dataSet2Label.setObjectName("dataSet2Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dataSet2Label)
        self.dataSet2ComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.dataSet2ComboBox.setObjectName("dataSet2ComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dataSet2ComboBox)
        self.outputToDataSetLabel = QtWidgets.QLabel(self.formGroupBox)
        self.outputToDataSetLabel.setObjectName("outputToDataSetLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.outputToDataSetLabel)
        self.outputToDataSetComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.outputToDataSetComboBox.setObjectName("outputToDataSetComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.outputToDataSetComboBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Combine Data Sets"))
        self.dataSet1Label.setText(("Data Set 1"))
        self.dataSet2Label.setText(("Data Set 2"))
        self.outputToDataSetLabel.setText(("Output to DataSet: "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
