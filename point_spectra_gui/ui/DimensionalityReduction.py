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
        self.formLayout.setObjectName("formLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseDataLabel)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseDataComboBox)
        self.chooseMethodLabel = QtWidgets.QLabel(self.formGroupBox)
        self.chooseMethodLabel.setObjectName("chooseMethodLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.chooseMethodLabel)
        self.chooseMethodComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseMethodComboBox.setObjectName("chooseMethodComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.chooseMethodComboBox)
        self.dim_reduction_vlayout = QtWidgets.QVBoxLayout()
        self.dim_reduction_vlayout.setObjectName("dim_reduction_vlayout")
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.dim_reduction_vlayout)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Dimensionality Reduction"))
        self.chooseDataLabel.setText(("Choose data:"))
        self.chooseMethodLabel.setText(("Choose method:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

