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
        self.fitInterceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.precomputeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.precomputeLabel.setObjectName("precomputeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.precomputeLabel)
        self.precomputeComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.precomputeComboBox.setObjectName("precomputeComboBox")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.precomputeComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.precomputeComboBox)
        self.cVLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cVLabel.setObjectName("cVLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cVLabel)
        self.cVCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.cVCheckBox.setObjectName("cVCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cVCheckBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        self.fitInterceptCheckBox.setToolTip(("whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations (e.g. data is expected to be already centered)."))
        self.fitInterceptCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html"))
        self.normalizeLabel.setText(("Normalize"))
        self.normalizeCheckBox.setToolTip(("This parameter is ignored when fit_intercept is set to False. If True, the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm. If you wish to standardize, please use sklearn.preprocessing.StandardScaler before calling fit on an estimator with normalize=False."))
        self.normalizeCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html"))
        self.precomputeLabel.setText(("Precompute"))
        self.precomputeComboBox.setToolTip(("Whether to use a precomputed Gram and Xy matrix to speed up calculations. Improves performance when n_targets or n_samples is very large. Note that if you already have such matrices, you can pass them directly to the fit method."))
        self.precomputeComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html"))
        self.precomputeComboBox.setItemText(0, ("auto"))
        self.precomputeComboBox.setItemText(1, ("True"))
        self.precomputeComboBox.setItemText(2, ("False"))
        self.cVLabel.setText(("CV"))
        self.cVCheckBox.setToolTip(("Cross Validate"))
        self.cVCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

