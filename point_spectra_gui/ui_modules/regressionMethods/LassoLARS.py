# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\LassoLARS.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.alphaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphaDoubleSpinBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.positiveLabel = QtWidgets.QLabel(self.formGroupBox)
        self.positiveLabel.setObjectName("positiveLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.positiveLabel)
        self.positiveCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.positiveCheckBox.setObjectName("positiveCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.positiveCheckBox)
        self.verboseLabel = QtWidgets.QLabel(self.formGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setChecked(True)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.copyXLabel = QtWidgets.QLabel(self.formGroupBox)
        self.copyXLabel.setObjectName("copyXLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.copyXLabel)
        self.copyXCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.copyXCheckBox.setChecked(True)
        self.copyXCheckBox.setObjectName("copyXCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.copyXCheckBox)
        self.precomputeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.precomputeLabel.setObjectName("precomputeLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.precomputeLabel)
        self.precomputeComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.precomputeComboBox.setObjectName("precomputeComboBox")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.precomputeComboBox)
        self.maxIterationsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.maxIterationsLabel)
        self.maxIterationsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.maxIterationsSpinBox.setMaximum(9999999)
        self.maxIterationsSpinBox.setProperty("value", 500)
        self.maxIterationsSpinBox.setObjectName("maxIterationsSpinBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.maxIterationsSpinBox)
        self.epsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.epsLabel.setObjectName("epsLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.epsLabel)
        self.epsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.epsDoubleSpinBox.setDecimals(16)
        self.epsDoubleSpinBox.setProperty("value", 2.220446)
        self.epsDoubleSpinBox.setObjectName("epsDoubleSpinBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.epsDoubleSpinBox)
        self.fitPathLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fitPathLabel.setObjectName("fitPathLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.fitPathLabel)
        self.fitPathCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fitPathCheckBox.setChecked(True)
        self.fitPathCheckBox.setObjectName("fitPathCheckBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.fitPathCheckBox)
        self.modelLabel = QtWidgets.QLabel(self.formGroupBox)
        self.modelLabel.setObjectName("modelLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.modelLabel)
        self.modelComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.modelComboBox.setObjectName("modelComboBox")
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.modelComboBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.alphaLabel.setText(_translate("Form", "Alpha "))
        self.fitInterceptLabel.setText(_translate("Form", "Fit Intercept"))
        self.positiveLabel.setText(_translate("Form", "Positive"))
        self.verboseLabel.setText(_translate("Form", "Verbose"))
        self.normalizeLabel.setText(_translate("Form", "Normalize"))
        self.copyXLabel.setText(_translate("Form", "Copy X"))
        self.precomputeLabel.setText(_translate("Form", "Precompute"))
        self.precomputeComboBox.setItemText(0, _translate("Form", "Auto"))
        self.precomputeComboBox.setItemText(1, _translate("Form", "True"))
        self.precomputeComboBox.setItemText(2, _translate("Form", "False"))
        self.precomputeComboBox.setItemText(3, _translate("Form", "array-like"))
        self.maxIterationsLabel.setText(_translate("Form", "Max Iterations"))
        self.epsLabel.setText(_translate("Form", "Eps"))
        self.fitPathLabel.setText(_translate("Form", "Fit Path"))
        self.modelLabel.setText(_translate("Form", "Model"))
        self.modelComboBox.setItemText(0, _translate("Form", "Lasso Lars"))
        self.modelComboBox.setItemText(1, _translate("Form", "Cross Validated Lasso Lars"))
        self.modelComboBox.setItemText(2, _translate("Form", "Information Criterion Lasso Lars"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

