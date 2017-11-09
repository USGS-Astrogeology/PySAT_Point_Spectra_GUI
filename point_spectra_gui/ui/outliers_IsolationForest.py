# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 104)
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
        self.n_est_label = QtWidgets.QLabel(self.groupBox)
        self.n_est_label.setObjectName("n_est_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.n_est_label)
        self.n_est_spin = QtWidgets.QSpinBox(self.groupBox)
        self.n_est_spin.setObjectName("n_est_spin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.n_est_spin)
        self.prop_outliers_label = QtWidgets.QLabel(self.groupBox)
        self.prop_outliers_label.setToolTip("")
        self.prop_outliers_label.setObjectName("prop_outliers_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.prop_outliers_label)
        self.prop_outliers_spin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.prop_outliers_spin.setDecimals(4)
        self.prop_outliers_spin.setMaximum(0.5)
        self.prop_outliers_spin.setObjectName("prop_outliers_spin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prop_outliers_spin)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.n_est_label.setText(("# of estimators"))
        self.prop_outliers_label.setText(("Proportion of outliers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

