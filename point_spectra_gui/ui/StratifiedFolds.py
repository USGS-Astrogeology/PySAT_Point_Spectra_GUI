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
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.chooseDataToStratifyLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseDataToStratifyLabel.setObjectName("chooseDataToStratifyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseDataToStratifyLabel)
        self.chooseDataToStratifyComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataToStratifyComboBox.setObjectName("chooseDataToStratifyComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseDataToStratifyComboBox)
        self.chooseVarLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseVarLabel.setObjectName("chooseVarLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.chooseVarLabel)
        self.chooseVarComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseVarComboBox.setObjectName("chooseVarComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chooseVarComboBox)
        self.nFoldsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.nFoldsLabel.setObjectName("nFoldsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nFoldsLabel)
        self.nFoldsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.nFoldsSpinBox.setObjectName("nFoldsSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nFoldsSpinBox)
        self.testFoldsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.testFoldsLabel.setObjectName("testFoldsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.testFoldsLabel)
        self.testFoldsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.testFoldsSpinBox.setObjectName("testFoldsSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.testFoldsSpinBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Stratified Folds"))
        self.chooseDataToStratifyLabel.setText(("Choose data to stratify: "))
        self.chooseVarLabel.setText(("Choose variable on which to sort: "))
        self.nFoldsLabel.setText(("N Folds"))
        self.testFoldsLabel.setText(("Test Fold"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

