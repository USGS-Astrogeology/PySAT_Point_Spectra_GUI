


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 366)
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
        self.alphaDoubleSpinBox.setMaximum(9999999.0)
        self.alphaDoubleSpinBox.setSingleStep(1.0)
        self.alphaDoubleSpinBox.setProperty("value", 1.0)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphaDoubleSpinBox)
        self.l1RatioLabel = QtWidgets.QLabel(self.groupBox)
        self.l1RatioLabel.setObjectName("l1RatioLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l1RatioLabel)
        self.l1RatioDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.l1RatioDoubleSpinBox.setMaximum(9999999.0)
        self.l1RatioDoubleSpinBox.setSingleStep(0.5)
        self.l1RatioDoubleSpinBox.setProperty("value", 0.5)
        self.l1RatioDoubleSpinBox.setObjectName("l1RatioDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.l1RatioDoubleSpinBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.groupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.groupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.precomputeLabel = QtWidgets.QLabel(self.groupBox)
        self.precomputeLabel.setObjectName("precomputeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.precomputeLabel)
        self.precomputeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.precomputeComboBox.setObjectName("precomputeComboBox")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.precomputeComboBox)
        self.maxNumOfIterationsLabel = QtWidgets.QLabel(self.groupBox)
        self.maxNumOfIterationsLabel.setObjectName("maxNumOfIterationsLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.maxNumOfIterationsLabel)
        self.maxNumOfIterationsSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.maxNumOfIterationsSpinBox.setMaximum(99999)
        self.maxNumOfIterationsSpinBox.setProperty("value", 1000)
        self.maxNumOfIterationsSpinBox.setObjectName("maxNumOfIterationsSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.maxNumOfIterationsSpinBox)
        self.copyXLabel = QtWidgets.QLabel(self.groupBox)
        self.copyXLabel.setObjectName("copyXLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.copyXLabel)
        self.copyXCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.copyXCheckBox.setChecked(True)
        self.copyXCheckBox.setObjectName("copyXCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.copyXCheckBox)
        self.toleranceLabel = QtWidgets.QLabel(self.groupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.toleranceDoubleSpinBox.setDecimals(4)
        self.toleranceDoubleSpinBox.setSingleStep(0.0001)
        self.toleranceDoubleSpinBox.setProperty("value", 0.0001)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.warmStartLabel = QtWidgets.QLabel(self.groupBox)
        self.warmStartLabel.setObjectName("warmStartLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.warmStartLabel)
        self.warmStartCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.warmStartCheckBox.setObjectName("warmStartCheckBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.warmStartCheckBox)
        self.positiveLabel = QtWidgets.QLabel(self.groupBox)
        self.positiveLabel.setObjectName("positiveLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.positiveLabel)
        self.positiveCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.positiveCheckBox.setObjectName("positiveCheckBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.positiveCheckBox)
        self.selectionLabel = QtWidgets.QLabel(self.groupBox)
        self.selectionLabel.setObjectName("selectionLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.selectionLabel)
        self.selectionLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.selectionLineEdit.setObjectName("selectionLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.selectionLineEdit)
        self.randomStateLabel = QtWidgets.QLabel(self.groupBox)
        self.randomStateLabel.setObjectName("randomStateLabel")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.randomStateLabel)
        self.randomStateLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.randomStateLineEdit.setObjectName("randomStateLineEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.randomStateLineEdit)
        self.crossValidateLabel = QtWidgets.QLabel(self.groupBox)
        self.crossValidateLabel.setObjectName("crossValidateLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.crossValidateLabel)
        self.crossValidateCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.crossValidateCheckBox.setChecked(True)
        self.crossValidateCheckBox.setObjectName("crossValidateCheckBox")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.crossValidateCheckBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form"))
        self.alphaLabel.setText(_translate("Form", "Alpha"))
        self.l1RatioLabel.setText(_translate("Form", "L1 Ratio"))
        self.fitInterceptLabel.setText(_translate("Form", "Fit Intercept"))
        self.normalizeLabel.setText(_translate("Form", "Normalize"))
        self.precomputeLabel.setText(_translate("Form", "Precompute"))
        self.precomputeComboBox.setItemText(0, _translate("Form", "False"))
        self.precomputeComboBox.setItemText(1, _translate("Form", "True"))
        self.precomputeComboBox.setItemText(2, _translate("Form", "Array-like"))
        self.maxNumOfIterationsLabel.setText(_translate("Form", "Max Num of Iterations"))
        self.copyXLabel.setText(_translate("Form", "Copy X"))
        self.toleranceLabel.setText(_translate("Form", "Tolerance"))
        self.warmStartLabel.setText(_translate("Form", "Warm Start"))
        self.positiveLabel.setText(_translate("Form", "Positive"))
        self.selectionLabel.setText(_translate("Form", "Selection"))
        self.selectionLineEdit.setText(_translate("Form", "cyclic"))
        self.randomStateLabel.setText(_translate("Form", "Random State"))
        self.randomStateLineEdit.setText(_translate("Form", "None"))
        self.crossValidateLabel.setText(_translate("Form", "Cross Validate"))


    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

