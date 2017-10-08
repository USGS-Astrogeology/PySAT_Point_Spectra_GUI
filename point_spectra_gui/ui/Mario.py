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
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.polynomialOrderLabel = QtWidgets.QLabel(self.groupbox)
        self.polynomialOrderLabel.setObjectName("polynomialOrderLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.polynomialOrderLabel)
        self.polynomialOrderSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.polynomialOrderSpinBox.setObjectName("polynomialOrderSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.polynomialOrderSpinBox)
        self.maximumNumOfIterationsLabel = QtWidgets.QLabel(self.groupbox)
        self.maximumNumOfIterationsLabel.setObjectName("maximumNumOfIterationsLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maximumNumOfIterationsLabel)
        self.maximumNumOfIterationsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.maximumNumOfIterationsDoubleSpinBox.setObjectName("maximumNumOfIterationsDoubleSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maximumNumOfIterationsDoubleSpinBox)
        self.toleranceLabel = QtWidgets.QLabel(self.groupbox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.polynomialOrderLabel.setText(("Polynomial Order"))
        self.maximumNumOfIterationsLabel.setText(("Maximum num of Iterations"))
        self.toleranceLabel.setText(("Tolerance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

