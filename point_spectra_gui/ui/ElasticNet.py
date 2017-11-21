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
        self.ENLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.ENLayout.setObjectName("ENLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.elasticNetCVGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.elasticNetCVGroupBox.setObjectName("elasticNetCVGroupBox")
        self.ElasticNetCV_2 = QtWidgets.QFormLayout(self.elasticNetCVGroupBox)
        self.ElasticNetCV_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.ElasticNetCV_2.setObjectName("ElasticNetCV_2")
        self.l1_ratioLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.l1_ratioLabel.setObjectName("l1_ratioLabel")
        self.ElasticNetCV_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l1_ratioLabel)
        self.l1_ratioDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.elasticNetCVGroupBox)
        self.l1_ratioDoubleSpinBox.setObjectName("l1_ratioDoubleSpinBox")
        self.ElasticNetCV_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.l1_ratioDoubleSpinBox)
        self.epsLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.epsLabel.setObjectName("epsLabel")
        self.ElasticNetCV_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.epsLabel)
        self.epsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.elasticNetCVGroupBox)
        self.epsDoubleSpinBox.setObjectName("epsDoubleSpinBox")
        self.ElasticNetCV_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.epsDoubleSpinBox)
        self.n_alphasLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.n_alphasLabel.setObjectName("n_alphasLabel")
        self.ElasticNetCV_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.n_alphasLabel)
        self.n_alphasSpinBox = QtWidgets.QSpinBox(self.elasticNetCVGroupBox)
        self.n_alphasSpinBox.setObjectName("n_alphasSpinBox")
        self.ElasticNetCV_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.n_alphasSpinBox)
        self.alphasLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.alphasLabel.setObjectName("alphasLabel")
        self.ElasticNetCV_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alphasLabel)
        self.alphasLineEdit = QtWidgets.QLineEdit(self.elasticNetCVGroupBox)
        self.alphasLineEdit.setObjectName("alphasLineEdit")
        self.ElasticNetCV_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alphasLineEdit)
        self.fit_interceptLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.fit_interceptLabel.setObjectName("fit_interceptLabel")
        self.ElasticNetCV_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fit_interceptLabel)
        self.fit_interceptCheckBox = QtWidgets.QCheckBox(self.elasticNetCVGroupBox)
        self.fit_interceptCheckBox.setObjectName("fit_interceptCheckBox")
        self.ElasticNetCV_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fit_interceptCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.ElasticNetCV_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.elasticNetCVGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.ElasticNetCV_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.precomputeLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.precomputeLabel.setObjectName("precomputeLabel")
        self.ElasticNetCV_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.precomputeLabel)
        self.precomputeComboBox = QtWidgets.QComboBox(self.elasticNetCVGroupBox)
        self.precomputeComboBox.setObjectName("precomputeComboBox")
        self.ElasticNetCV_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.precomputeComboBox)
        self.max_iterLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.max_iterLabel.setObjectName("max_iterLabel")
        self.ElasticNetCV_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.max_iterLabel)
        self.max_iterSpinBox = QtWidgets.QSpinBox(self.elasticNetCVGroupBox)
        self.max_iterSpinBox.setObjectName("max_iterSpinBox")
        self.ElasticNetCV_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.max_iterSpinBox)
        self.tolLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.tolLabel.setObjectName("tolLabel")
        self.ElasticNetCV_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.tolLabel)
        self.tolDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.elasticNetCVGroupBox)
        self.tolDoubleSpinBox.setObjectName("tolDoubleSpinBox")
        self.ElasticNetCV_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.tolDoubleSpinBox)
        self.copy_XLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.copy_XLabel.setObjectName("copy_XLabel")
        self.ElasticNetCV_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.copy_XLabel)
        self.copy_XCheckBox = QtWidgets.QCheckBox(self.elasticNetCVGroupBox)
        self.copy_XCheckBox.setObjectName("copy_XCheckBox")
        self.ElasticNetCV_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.copy_XCheckBox)
        self.verboseLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.ElasticNetCV_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.elasticNetCVGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.ElasticNetCV_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.n_jobsLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.n_jobsLabel.setObjectName("n_jobsLabel")
        self.ElasticNetCV_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.n_jobsLabel)
        self.n_jobsSpinBox = QtWidgets.QSpinBox(self.elasticNetCVGroupBox)
        self.n_jobsSpinBox.setObjectName("n_jobsSpinBox")
        self.ElasticNetCV_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.n_jobsSpinBox)
        self.positiveLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.positiveLabel.setObjectName("positiveLabel")
        self.ElasticNetCV_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.positiveLabel)
        self.positiveCheckBox = QtWidgets.QCheckBox(self.elasticNetCVGroupBox)
        self.positiveCheckBox.setObjectName("positiveCheckBox")
        self.ElasticNetCV_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.positiveCheckBox)
        self.selectionLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.selectionLabel.setObjectName("selectionLabel")
        self.ElasticNetCV_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.selectionLabel)
        self.selectionComboBox = QtWidgets.QComboBox(self.elasticNetCVGroupBox)
        self.selectionComboBox.setObjectName("selectionComboBox")
        self.ElasticNetCV_2.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.selectionComboBox)
        self.cVLabel = QtWidgets.QLabel(self.elasticNetCVGroupBox)
        self.cVLabel.setObjectName("cVLabel")
        self.ElasticNetCV_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.cVLabel)
        self.cVSpinBox = QtWidgets.QSpinBox(self.elasticNetCVGroupBox)
        self.cVSpinBox.setObjectName("cVSpinBox")
        self.ElasticNetCV_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.cVSpinBox)
        self.horizontalLayout.addWidget(self.elasticNetCVGroupBox)
        self.elasticNetGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.elasticNetGroupBox.setObjectName("elasticNetGroupBox")
        self.ElasticNet = QtWidgets.QFormLayout(self.elasticNetGroupBox)
        self.ElasticNet.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.ElasticNet.setObjectName("ElasticNet")
        self.enalphaLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enalphaLabel.setObjectName("enalphaLabel")
        self.ElasticNet.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.enalphaLabel)
        self.enalphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.elasticNetGroupBox)
        self.enalphaDoubleSpinBox.setObjectName("enalphaDoubleSpinBox")
        self.ElasticNet.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.enalphaDoubleSpinBox)
        self.enl1_ratioLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enl1_ratioLabel.setObjectName("enl1_ratioLabel")
        self.ElasticNet.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.enl1_ratioLabel)
        self.enl1_ratioDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.elasticNetGroupBox)
        self.enl1_ratioDoubleSpinBox.setObjectName("enl1_ratioDoubleSpinBox")
        self.ElasticNet.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enl1_ratioDoubleSpinBox)
        self.enfit_interceptLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enfit_interceptLabel.setObjectName("enfit_interceptLabel")
        self.ElasticNet.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.enfit_interceptLabel)
        self.enfit_interceptCheckBox = QtWidgets.QCheckBox(self.elasticNetGroupBox)
        self.enfit_interceptCheckBox.setObjectName("enfit_interceptCheckBox")
        self.ElasticNet.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enfit_interceptCheckBox)
        self.ennormalizeLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.ennormalizeLabel.setObjectName("ennormalizeLabel")
        self.ElasticNet.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ennormalizeLabel)
        self.ennormalizeCheckBox = QtWidgets.QCheckBox(self.elasticNetGroupBox)
        self.ennormalizeCheckBox.setObjectName("ennormalizeCheckBox")
        self.ElasticNet.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ennormalizeCheckBox)
        self.enprecomputeLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enprecomputeLabel.setObjectName("enprecomputeLabel")
        self.ElasticNet.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.enprecomputeLabel)
        self.enprecomputeCheckBox = QtWidgets.QCheckBox(self.elasticNetGroupBox)
        self.enprecomputeCheckBox.setObjectName("enprecomputeCheckBox")
        self.ElasticNet.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.enprecomputeCheckBox)
        self.enmax_iterLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enmax_iterLabel.setObjectName("enmax_iterLabel")
        self.ElasticNet.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.enmax_iterLabel)
        self.enmax_iterSpinBox = QtWidgets.QSpinBox(self.elasticNetGroupBox)
        self.enmax_iterSpinBox.setObjectName("enmax_iterSpinBox")
        self.ElasticNet.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.enmax_iterSpinBox)
        self.encopy_XLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.encopy_XLabel.setObjectName("encopy_XLabel")
        self.ElasticNet.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.encopy_XLabel)
        self.encopy_XCheckBox = QtWidgets.QCheckBox(self.elasticNetGroupBox)
        self.encopy_XCheckBox.setObjectName("encopy_XCheckBox")
        self.ElasticNet.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.encopy_XCheckBox)
        self.entolLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.entolLabel.setObjectName("entolLabel")
        self.ElasticNet.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.entolLabel)
        self.entolDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.elasticNetGroupBox)
        self.entolDoubleSpinBox.setObjectName("entolDoubleSpinBox")
        self.ElasticNet.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.entolDoubleSpinBox)
        self.enwarm_startLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enwarm_startLabel.setObjectName("enwarm_startLabel")
        self.ElasticNet.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.enwarm_startLabel)
        self.enwarm_startCheckBox = QtWidgets.QCheckBox(self.elasticNetGroupBox)
        self.enwarm_startCheckBox.setObjectName("enwarm_startCheckBox")
        self.ElasticNet.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.enwarm_startCheckBox)
        self.enpositiveLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enpositiveLabel.setObjectName("enpositiveLabel")
        self.ElasticNet.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.enpositiveLabel)
        self.enpositiveCheckBox = QtWidgets.QCheckBox(self.elasticNetGroupBox)
        self.enpositiveCheckBox.setObjectName("enpositiveCheckBox")
        self.ElasticNet.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.enpositiveCheckBox)
        self.enselectionLabel = QtWidgets.QLabel(self.elasticNetGroupBox)
        self.enselectionLabel.setObjectName("enselectionLabel")
        self.ElasticNet.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.enselectionLabel)
        self.enselectionComboBox = QtWidgets.QComboBox(self.elasticNetGroupBox)
        self.enselectionComboBox.setObjectName("enselectionComboBox")
        self.enselectionComboBox.addItem("")
        self.enselectionComboBox.addItem("")
        self.ElasticNet.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.enselectionComboBox)
        self.horizontalLayout.addWidget(self.elasticNetGroupBox)
        self.ENLayout.addLayout(self.horizontalLayout)
        self.CVCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.CVCheckBox.setObjectName("CVCheckBox")
        self.ENLayout.addWidget(self.CVCheckBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        self.CVCheckBox.toggled['bool'].connect(self.elasticNetCVGroupBox.setVisible)
        self.CVCheckBox.toggled['bool'].connect(self.elasticNetGroupBox.setHidden)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.elasticNetCVGroupBox.setTitle(("Elastic Net CV"))
        self.l1_ratioLabel.setText(_translate("Form", "l1_ratio\n"
""))
        self.l1_ratioDoubleSpinBox.setToolTip(_translate("Form", "The ElasticNet mixing parameter, with 0 <= l1_ratio <= 1. For l1_ratio\n"
"= 0 the penalty is an L2 penalty. For l1_ratio = 1 it is an L1 penalty.\n"
"For 0 < l1_ratio < 1, the penalty is a combination of L1 and L2."))
        self.l1_ratioDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.epsLabel.setText(_translate("Form", "eps\n"
""))
        self.epsDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.n_alphasLabel.setText(_translate("Form", "n_alphas\n"
""))
        self.n_alphasSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.alphasLabel.setText(_translate("Form", "alphas\n"
""))
        self.alphasLineEdit.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.fit_interceptLabel.setText(_translate("Form", "fit_intercept\n"
""))
        self.fit_interceptCheckBox.setToolTip(_translate("Form", "Whether the intercept should be estimated or not. If False, the data\n"
"is assumed to be already centered."))
        self.fit_interceptCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.normalizeLabel.setText(_translate("Form", "normalize\n"
""))
        self.normalizeCheckBox.setToolTip(_translate("Form", "This parameter is ignored when fit_intercept is set to False. If True,\n"
"the regressors X will be normalized before regression by subtracting\n"
"the mean and dividing by the l2-norm. If you wish to standardize,\n"
"please use sklearn.preprocessing. StandardScaler before calling fit on\n"
"an estimator with normalize=False."))
        self.normalizeCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.precomputeLabel.setText(_translate("Form", "precompute\n"
""))
        self.precomputeComboBox.setToolTip(_translate("Form", "Whether to use a precomputed Gram matrix to speed up calculations.\n"
"The Gram matrix can also be passed as argument. For sparse input this\n"
"option is always True to preserve sparsity."))
        self.precomputeComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.max_iterLabel.setText(_translate("Form", "max_iter\n"
""))
        self.max_iterSpinBox.setToolTip(("The maximum number of iterations"))
        self.max_iterSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.tolLabel.setText(_translate("Form", "tol\n"
""))
        self.tolDoubleSpinBox.setToolTip(("The tolerance for the optimization:"))
        self.tolDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.copy_XLabel.setText(_translate("Form", "copy_X\n"
""))
        self.copy_XCheckBox.setToolTip(("If True, X will be copied; else, it may be overwritten."))
        self.copy_XCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.verboseLabel.setText(_translate("Form", "verbose\n"
""))
        self.verboseCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.n_jobsLabel.setText(_translate("Form", "n_jobs\n"
""))
        self.n_jobsSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.positiveLabel.setText(_translate("Form", "positive\n"
""))
        self.positiveCheckBox.setToolTip(("When set to True, forces the coefficients to be positive."))
        self.positiveCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.selectionLabel.setText(("selection"))
        self.selectionComboBox.setToolTip(_translate("Form", "If set to \'random\', a random coefficient is updated every iteration\n"
"rather than looping over features sequentially by default. This\n"
"(setting to \'random\') often leads to significantly faster convergence\n"
"especially when tol is higher than 1e-4."))
        self.selectionComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.cVLabel.setText(("cv"))
        self.cVSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.elasticNetGroupBox.setTitle(("Elastic Net"))
        self.enalphaLabel.setText(_translate("Form", "alpha\n"
""))
        self.enalphaDoubleSpinBox.setToolTip(_translate("Form", "Constant that multiplies the penalty terms. Defaults to 1.0. See the\n"
"notes for the exact mathematical meaning of this parameter. alpha = 0\n"
"is equivalent to an ordinary least square, solved by the\n"
"LinearRegression object. For numerical reasons, using alpha = 0 with\n"
"the Lasso object is not advised. Given this, you should use the\n"
"LinearRegression object."))
        self.enalphaDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enl1_ratioLabel.setText(_translate("Form", "l1_ratio\n"
""))
        self.enl1_ratioDoubleSpinBox.setToolTip(_translate("Form", "The ElasticNet mixing parameter, with 0 <= l1_ratio <= 1. For l1_ratio\n"
"= 0 the penalty is an L2 penalty. For l1_ratio = 1 it is an L1 penalty.\n"
"For 0 < l1_ratio < 1, the penalty is a combination of L1 and L2."))
        self.enl1_ratioDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enfit_interceptLabel.setText(_translate("Form", "fit_intercept\n"
""))
        self.enfit_interceptCheckBox.setToolTip(_translate("Form", "Whether the intercept should be estimated or not. If False, the data\n"
"is assumed to be already centered."))
        self.enfit_interceptCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.ennormalizeLabel.setText(_translate("Form", "normalize\n"
""))
        self.ennormalizeCheckBox.setToolTip(_translate("Form", "This parameter is ignored when fit_intercept is set to False. If True,\n"
"the regressors X will be normalized before regression by subtracting\n"
"the mean and dividing by the l2-norm. If you wish to standardize,\n"
"please use sklearn.preprocessing. StandardScaler before calling fit on\n"
"an estimator with normalize=False."))
        self.ennormalizeCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enprecomputeLabel.setText(_translate("Form", "precompute\n"
""))
        self.enprecomputeCheckBox.setToolTip(_translate("Form", "Whether to use a precomputed Gram matrix to speed up calculations.\n"
"The Gram matrix can also be passed as argument. For sparse input this\n"
"option is always True to preserve sparsity."))
        self.enprecomputeCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enmax_iterLabel.setText(_translate("Form", "max_iter\n"
""))
        self.enmax_iterSpinBox.setToolTip(("The maximum number of iterations"))
        self.enmax_iterSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.encopy_XLabel.setText(_translate("Form", "copy_X\n"
""))
        self.encopy_XCheckBox.setToolTip(("If True, X will be copied; else, it may be overwritten."))
        self.encopy_XCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.entolLabel.setText(_translate("Form", "tol\n"
""))
        self.entolDoubleSpinBox.setToolTip(("The tolerance for the optimization:"))
        self.entolDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enwarm_startLabel.setText(_translate("Form", "warm_start\n"
""))
        self.enwarm_startCheckBox.setToolTip(_translate("Form", "When set to True, reuse the solution of the previous call to fit as\n"
"initialization, otherwise, just erase the previous solution."))
        self.enwarm_startCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enpositiveLabel.setText(("positive"))
        self.enpositiveCheckBox.setToolTip(("When set to True, forces the coefficients to be positive."))
        self.enpositiveCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enselectionLabel.setText(("selection"))
        self.enselectionComboBox.setToolTip(_translate("Form", "If set to \'random\', a random coefficient is updated every iteration\n"
"rather than looping over features sequentially by default. This\n"
"(setting to \'random\') often leads to significantly faster convergence\n"
"especially when tol is higher than 1e-4."))
        self.enselectionComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.enselectionComboBox.setItemText(0, ("cyclic"))
        self.enselectionComboBox.setItemText(1, ("random"))
        self.CVCheckBox.setToolTip(("Cross Validate"))
        self.CVCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html"))
        self.CVCheckBox.setText(("CV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

