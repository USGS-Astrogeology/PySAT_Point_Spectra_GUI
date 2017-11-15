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
        self.alphaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphaDoubleSpinBox)
        self.fit_interceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fit_interceptLabel.setObjectName("fit_interceptLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fit_interceptLabel)
        self.fit_interceptCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fit_interceptCheckBox.setObjectName("fit_interceptCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fit_interceptCheckBox)
        self.verboseLabel = QtWidgets.QLabel(self.formGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.precomputeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.precomputeLabel.setObjectName("precomputeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.precomputeLabel)
        self.precomputeComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.precomputeComboBox.setObjectName("precomputeComboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.precomputeComboBox)
        self.max_iterLabel = QtWidgets.QLabel(self.formGroupBox)
        self.max_iterLabel.setObjectName("max_iterLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.max_iterLabel)
        self.max_iterSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.max_iterSpinBox.setObjectName("max_iterSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.max_iterSpinBox)
        self.copy_XLabel = QtWidgets.QLabel(self.formGroupBox)
        self.copy_XLabel.setObjectName("copy_XLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.copy_XLabel)
        self.copy_XCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.copy_XCheckBox.setObjectName("copy_XCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.copy_XCheckBox)
        self.fit_pathLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fit_pathLabel.setObjectName("fit_pathLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.fit_pathLabel)
        self.fit_pathCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fit_pathCheckBox.setObjectName("fit_pathCheckBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fit_pathCheckBox)
        self.positiveLabel = QtWidgets.QLabel(self.formGroupBox)
        self.positiveLabel.setObjectName("positiveLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.positiveLabel)
        self.positiveCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.positiveCheckBox.setObjectName("positiveCheckBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.positiveCheckBox)
        self.cvLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cvLabel.setObjectName("cvLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.cvLabel)
        self.cvSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.cvSpinBox.setObjectName("cvSpinBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.cvSpinBox)
        self.max_n_alphasLabel = QtWidgets.QLabel(self.formGroupBox)
        self.max_n_alphasLabel.setObjectName("max_n_alphasLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.max_n_alphasLabel)
        self.max_n_alphasSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.max_n_alphasSpinBox.setObjectName("max_n_alphasSpinBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.max_n_alphasSpinBox)
        self.n_jobsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.n_jobsLabel.setObjectName("n_jobsLabel")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.n_jobsLabel)
        self.n_jobsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.n_jobsSpinBox.setObjectName("n_jobsSpinBox")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.n_jobsSpinBox)
        self.criterionLabel = QtWidgets.QLabel(self.formGroupBox)
        self.criterionLabel.setObjectName("criterionLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.criterionLabel)
        self.criterionComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.criterionComboBox.setObjectName("criterionComboBox")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.criterionComboBox)
        self.modelLabel = QtWidgets.QLabel(self.formGroupBox)
        self.modelLabel.setObjectName("modelLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.modelLabel)
        self.modelComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.modelComboBox.setObjectName("modelComboBox")
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.modelComboBox.addItem("")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.modelComboBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.alphaLabel.setText(("alpha"))
        self.alphaDoubleSpinBox.setToolTip(_translate("Form", "Constant that multiplies the penalty term. Defaults to 1.0. alpha = 0\n"
"is equivalent to an ordinary least square, solved by LinearRegression.\n"
"For numerical reasons, using alpha = 0 with the LassoLars object is not\n"
"advised and you should prefer the LinearRegression object."))
        self.alphaDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.fit_interceptLabel.setText(("fit_intercept"))
        self.fit_interceptCheckBox.setToolTip(_translate("Form", "whether to calculate the intercept for this model. If set to false,\n"
"no intercept will be used in calculations (e.g. data is expected to\n"
"be already centered)."))
        self.fit_interceptCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.verboseLabel.setText(("verbose"))
        self.verboseCheckBox.setToolTip(("Sets the verbosity amount"))
        self.verboseCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.normalizeLabel.setText(("normalize"))
        self.normalizeCheckBox.setToolTip(_translate("Form", "This parameter is ignored when fit_intercept is set to False. If True,\n"
"the regressors X will be normalized before regression by subtracting\n"
"the mean and dividing by the l2-norm. If you wish to standardize,\n"
"please use sklearn.preprocessing.StandardScaler before calling fit\n"
"on an estimator with normalize=False."))
        self.normalizeCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.precomputeLabel.setText(("precompute"))
        self.precomputeComboBox.setToolTip(_translate("Form", "Whether to use a precomputed Gram matrix to speed up calculations. If\n"
"set to \'auto\' let us decide. The Gram matrix can also be passed as\n"
"argument."))
        self.precomputeComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.max_iterLabel.setText(_translate("Form", "max_iter\n"
""))
        self.max_iterSpinBox.setToolTip(("Maximum number of iterations to perform."))
        self.max_iterSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.copy_XLabel.setText(_translate("Form", "copy_X\n"
""))
        self.copy_XCheckBox.setToolTip(("If True, X will be copied; else, it may be overwritten."))
        self.copy_XCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.fit_pathLabel.setText(_translate("Form", "fit_path\n"
""))
        self.fit_pathCheckBox.setToolTip(_translate("Form", "If True the full path is stored in the coef_path_ attribute. If you\n"
"compute the solution for a large problem or many targets, setting\n"
"fit_path to False will lead to a speedup, especially with a small\n"
"alpha."))
        self.fit_pathCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.positiveLabel.setText(("positive"))
        self.positiveCheckBox.setToolTip(_translate("Form", "Restrict coefficients to be >= 0. Be aware that you might want to\n"
"remove fit_intercept which is set True by default. Under the positive\n"
"restriction the model coefficients will not converge to the\n"
"ordinary-least-squares solution for small values of alpha. Only\n"
"coefficients up to the smallest alpha value\n"
"(alphas_[alphas_ > 0.].min() when fit_path=True) reached by the\n"
"stepwise Lars-Lasso algorithm are typically in congruence with the\n"
"solution of the coordinate descent Lasso estimator."))
        self.positiveCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.cvLabel.setText(_translate("Form", "cv\n"
""))
        self.cvSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.max_n_alphasLabel.setText(_translate("Form", "max_n_alphas\n"
""))
        self.max_n_alphasSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.n_jobsLabel.setText(("n_jobs"))
        self.n_jobsSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.criterionLabel.setText(("criterion "))
        self.criterionComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.modelLabel.setText(("Model"))
        self.modelComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html"))
        self.modelComboBox.setItemText(0, ("Lasso Lars"))
        self.modelComboBox.setItemText(1, ("Cross Validated Lasso Lars"))
        self.modelComboBox.setItemText(2, ("Information Criterion Lasso Lars"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

