


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(442, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.cLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cLabel.setObjectName("cLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cLabel)
        self.cDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.cDoubleSpinBox.setProperty("value", 1.0)
        self.cDoubleSpinBox.setObjectName("cDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cDoubleSpinBox)
        self.epsilonLabel = QtWidgets.QLabel(self.formGroupBox)
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.epsilonLabel)
        self.epsilonDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.epsilonDoubleSpinBox.setProperty("value", 0.1)
        self.epsilonDoubleSpinBox.setObjectName("epsilonDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.epsilonDoubleSpinBox)
        self.kernelLabel = QtWidgets.QLabel(self.formGroupBox)
        self.kernelLabel.setObjectName("kernelLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.kernelLabel)
        self.kernelComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.kernelComboBox.setObjectName("kernelComboBox")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kernelComboBox)
        self.degreeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.degreeLabel.setObjectName("degreeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.degreeLabel)
        self.degreeSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.degreeSpinBox.setObjectName("degreeSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.degreeSpinBox)
        self.gammaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.gammaLabel.setObjectName("gammaLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.gammaLabel)
        self.gammaComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.gammaComboBox.setObjectName("gammaComboBox")
        self.gammaComboBox.addItem("")
        self.gammaComboBox.addItem("")
        self.gammaComboBox.addItem("")
        self.gammaComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gammaComboBox)
        self.coeff0Label = QtWidgets.QLabel(self.formGroupBox)
        self.coeff0Label.setObjectName("coeff0Label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.coeff0Label)
        self.coeff0DoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.coeff0DoubleSpinBox.setObjectName("coeff0DoubleSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.coeff0DoubleSpinBox)
        self.shrinkingLabel = QtWidgets.QLabel(self.formGroupBox)
        self.shrinkingLabel.setObjectName("shrinkingLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.shrinkingLabel)
        self.shrinkingCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.shrinkingCheckBox.setObjectName("shrinkingCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.shrinkingCheckBox)
        self.toleranceLabel = QtWidgets.QLabel(self.formGroupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.toleranceDoubleSpinBox.setDecimals(3)
        self.toleranceDoubleSpinBox.setProperty("value", 0.001)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.cacheSizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cacheSizeLabel.setObjectName("cacheSizeLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.cacheSizeLabel)
        self.cacheSizeSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.cacheSizeSpinBox.setMaximum(999)
        self.cacheSizeSpinBox.setProperty("value", 200)
        self.cacheSizeSpinBox.setObjectName("cacheSizeSpinBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.cacheSizeSpinBox)
        self.verboseLabel = QtWidgets.QLabel(self.formGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.maxIterationsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.maxIterationsLabel)
        self.maxIterationsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.maxIterationsSpinBox.setMinimum(-1)
        self.maxIterationsSpinBox.setMaximum(9999999)
        self.maxIterationsSpinBox.setProperty("value", -1)
        self.maxIterationsSpinBox.setObjectName("maxIterationsSpinBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.maxIterationsSpinBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cLabel.setText(_translate("Form", "C"))
        self.epsilonLabel.setText(_translate("Form", "Epsilon"))
        self.kernelLabel.setText(_translate("Form", "Kernel"))
        self.kernelComboBox.setItemText(0, _translate("Form", "rbf"))
        self.kernelComboBox.setItemText(1, _translate("Form", "poly"))
        self.kernelComboBox.setItemText(2, _translate("Form", "sigmoid"))
        self.kernelComboBox.setItemText(3, _translate("Form", "linear"))
        self.kernelComboBox.setItemText(4, _translate("Form", "precomputed"))
        self.degreeLabel.setText(_translate("Form", "Degree"))
        self.gammaLabel.setText(_translate("Form", "Gamma"))
        self.gammaComboBox.setItemText(0, _translate("Form", "auto"))
        self.gammaComboBox.setItemText(1, _translate("Form", "rbf"))
        self.gammaComboBox.setItemText(2, _translate("Form", "poly"))
        self.gammaComboBox.setItemText(3, _translate("Form", "sigmoid"))
        self.coeff0Label.setText(_translate("Form", "Coeff 0"))
        self.shrinkingLabel.setText(_translate("Form", "Shrinking"))
        self.toleranceLabel.setText(_translate("Form", "Tolerance"))
        self.cacheSizeLabel.setText(_translate("Form", "Cache Size"))
        self.verboseLabel.setText(_translate("Form", "Verbose"))
        self.maxIterationsLabel.setText(_translate("Form", "Max Iterations"))


    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

