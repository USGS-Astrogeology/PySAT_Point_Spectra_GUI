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
        self.largestWaveletScaleLabel = QtWidgets.QLabel(self.groupbox)
        self.largestWaveletScaleLabel.setObjectName("largestWaveletScaleLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.largestWaveletScaleLabel)
        self.largestWaveletScaleSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.largestWaveletScaleSpinBox.setObjectName("largestWaveletScaleSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.largestWaveletScaleSpinBox)
        self.lowestWaveletScaleLabel = QtWidgets.QLabel(self.groupbox)
        self.lowestWaveletScaleLabel.setObjectName("lowestWaveletScaleLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lowestWaveletScaleLabel)
        self.lowestWaveletScaleSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.lowestWaveletScaleSpinBox.setObjectName("lowestWaveletScaleSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lowestWaveletScaleSpinBox)
        self.interpolationMethodLabel = QtWidgets.QLabel(self.groupbox)
        self.interpolationMethodLabel.setObjectName("interpolationMethodLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.interpolationMethodLabel)
        self.interpolationMethodComboBox = QtWidgets.QComboBox(self.groupbox)
        self.interpolationMethodComboBox.setObjectName("interpolationMethodComboBox")
        self.interpolationMethodComboBox.addItem("")
        self.interpolationMethodComboBox.addItem("")
        self.interpolationMethodComboBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.interpolationMethodComboBox)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.largestWaveletScaleLabel.setText(("Largest Wavelet Scale"))
        self.lowestWaveletScaleLabel.setText(("Lowest Wavelet Scale"))
        self.interpolationMethodLabel.setText(("Interpolation Method"))
        self.interpolationMethodComboBox.setItemText(0, ("Spline"))
        self.interpolationMethodComboBox.setItemText(1, ("Quadratic"))
        self.interpolationMethodComboBox.setItemText(2, ("Linear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

