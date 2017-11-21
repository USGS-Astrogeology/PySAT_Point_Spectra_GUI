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
        self.nc_label = QtWidgets.QLabel(self.groupBox)
        self.nc_label.setObjectName("nc_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nc_label)
        self.nc_spin = QtWidgets.QSpinBox(self.groupBox)
        self.nc_spin.setObjectName("nc_spin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nc_spin)
        self.learning_label = QtWidgets.QLabel(self.groupBox)
        self.learning_label.setObjectName("learning_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.learning_label)
        self.learning_spin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.learning_spin.setMinimum(10.0)
        self.learning_spin.setMaximum(2000.0)
        self.learning_spin.setProperty("value", 200.0)
        self.learning_spin.setObjectName("learning_spin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.learning_spin)
        self.n_iter_label = QtWidgets.QLabel(self.groupBox)
        self.n_iter_label.setObjectName("n_iter_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.n_iter_label)
        self.n_iter_spin = QtWidgets.QSpinBox(self.groupBox)
        self.n_iter_spin.setMinimum(250)
        self.n_iter_spin.setMaximum(999999999)
        self.n_iter_spin.setProperty("value", 1000)
        self.n_iter_spin.setObjectName("n_iter_spin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.n_iter_spin)
        self.no_progress_label = QtWidgets.QLabel(self.groupBox)
        self.no_progress_label.setObjectName("no_progress_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.no_progress_label)
        self.no_progress_spin = QtWidgets.QSpinBox(self.groupBox)
        self.no_progress_spin.setMinimum(50)
        self.no_progress_spin.setMaximum(999999999)
        self.no_progress_spin.setSingleStep(50)
        self.no_progress_spin.setProperty("value", 300)
        self.no_progress_spin.setObjectName("no_progress_spin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.no_progress_spin)
        self.perplexity = QtWidgets.QLabel(self.groupBox)
        self.perplexity.setObjectName("perplexity")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.perplexity)
        self.perplexity_spin = QtWidgets.QSpinBox(self.groupBox)
        self.perplexity_spin.setMaximum(10000)
        self.perplexity_spin.setObjectName("perplexity_spin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.perplexity_spin)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.nc_label.setText(("# of components"))
        self.learning_label.setText(("Learning Rate"))
        self.n_iter_label.setText(("# of iterations"))
        self.no_progress_label.setText(("# with no progress"))
        self.perplexity.setText(("Perplexity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

