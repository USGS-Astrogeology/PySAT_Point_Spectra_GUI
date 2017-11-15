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
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.alphaLabel = QtWidgets.QLabel(self.groupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.alphaDoubleSpinBox.setEnabled(False)
        self.alphaDoubleSpinBox.setMaximum(999999999.0)
        self.alphaDoubleSpinBox.setProperty("value", 1.0)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphaDoubleSpinBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(self.groupBox)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.maxNumOfIterationsSpinBox.setMaximum(999999999)
        self.maxNumOfIterationsSpinBox.setProperty("value", 1000)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.toleranceLabel = QtWidgets.QLabel(self.groupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.fitInterceptLabel = QtWidgets.QLabel(self.groupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.forcePositiveCoefficientsLabel = QtWidgets.QLabel(self.groupBox)
        self.forcePositiveCoefficientsLabel.setObjectName("forcePositiveCoefficientsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.forcePositiveCoefficientsLabel)
        self.forcePositiveCoefficientsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.forcePositiveCoefficientsCheckBox.setObjectName("forcePositiveCoefficientsCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.forcePositiveCoefficientsCheckBox)
        self.optimizeWCrossValidaitonLabel = QtWidgets.QLabel(self.groupBox)
        self.optimizeWCrossValidaitonLabel.setObjectName("optimizeWCrossValidaitonLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.optimizeWCrossValidaitonLabel)
        self.optimizeWCrossValidaitonCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.optimizeWCrossValidaitonCheckBox.setChecked(True)
        self.optimizeWCrossValidaitonCheckBox.setObjectName("optimizeWCrossValidaitonCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.optimizeWCrossValidaitonCheckBox)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.toleranceDoubleSpinBox.setDecimals(5)
        self.toleranceDoubleSpinBox.setMaximum(999999999.0)
        self.toleranceDoubleSpinBox.setProperty("value", 0.0001)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        self.optimizeWCrossValidaitonCheckBox.toggled['bool'].connect(self.alphaDoubleSpinBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.alphaDoubleSpinBox, self.maxNumOfIterationsSpinBox)
        Form.setTabOrder(self.maxNumOfIterationsSpinBox, self.toleranceDoubleSpinBox)
        Form.setTabOrder(self.toleranceDoubleSpinBox, self.fitInterceptCheckBox)
        Form.setTabOrder(self.fitInterceptCheckBox, self.forcePositiveCoefficientsCheckBox)
        Form.setTabOrder(self.forcePositiveCoefficientsCheckBox, self.optimizeWCrossValidaitonCheckBox)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.alphaLabel.setText(("Alpha"))
        self.alphaDoubleSpinBox.setToolTip(_translate("Form", "Constant that multiplies the L1 term. Defaults to 1.0. alpha = 0 is\n"
"equivalent to an ordinary least square, solved by the LinearRegression\n"
"object. For numerical reasons, using alpha = 0 with the Lasso object\n"
"is not advised. Given this, you should use the LinearRegression object."))
        self.alphaDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.maxNumOfIterationsLabel.setText(("Max # of iterations"))
        self.maxNumOfIterationsSpinBox.setToolTip(("The maximum number of iterations"))
        self.maxNumOfIterationsSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.toleranceLabel.setText(("Tolerance"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        self.fitInterceptCheckBox.setToolTip(_translate("Form", "whether to calculate the intercept for this model. If set to false,\n"
"no intercept will be used in calculations (e.g. data is expected to\n"
"be already centered)."))
        self.fitInterceptCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.forcePositiveCoefficientsLabel.setText(("Force positive coefficients"))
        self.forcePositiveCoefficientsCheckBox.setToolTip(("When set to True, forces the coefficients to be positive."))
        self.forcePositiveCoefficientsCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.optimizeWCrossValidaitonLabel.setText(("Optimize w/ Cross Validation (Ignores alpha)"))
        self.optimizeWCrossValidaitonCheckBox.setToolTip(("Optimize with Cross Validaiton"))
        self.optimizeWCrossValidaitonCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))
        self.toleranceDoubleSpinBox.setToolTip(("The tolerance for the optimization"))
        self.toleranceDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

