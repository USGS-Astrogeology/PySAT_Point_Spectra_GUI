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
        self.neighbors_label = QtWidgets.QLabel(self.groupBox)
        self.neighbors_label.setObjectName("neighbors_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.neighbors_label)
        self.neighbors_spin = QtWidgets.QSpinBox(self.groupBox)
        self.neighbors_spin.setMaximum(1000000)
        self.neighbors_spin.setObjectName("neighbors_spin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.neighbors_spin)
        self.nc_label = QtWidgets.QLabel(self.groupBox)
        self.nc_label.setObjectName("nc_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nc_label)
        self.nc_spin = QtWidgets.QSpinBox(self.groupBox)
        self.nc_spin.setMaximum(10000)
        self.nc_spin.setObjectName("nc_spin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nc_spin)
        self.regularization_label = QtWidgets.QLabel(self.groupBox)
        self.regularization_label.setObjectName("regularization_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.regularization_label)
        self.regularization_spin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.regularization_spin.setDecimals(6)
        self.regularization_spin.setMinimum(0.0)
        self.regularization_spin.setMaximum(2000.0)
        self.regularization_spin.setSingleStep(0.001)
        self.regularization_spin.setProperty("value", 0.001)
        self.regularization_spin.setObjectName("regularization_spin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.regularization_spin)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.neighbors_label.setText(("# of neighbors"))
        self.nc_label.setText(("# of components"))
        self.regularization_label.setText(("Regularization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

