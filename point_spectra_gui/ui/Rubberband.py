# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupbox)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.windowSizeLabel = QtWidgets.QLabel(self.groupbox)
        self.windowSizeLabel.setObjectName("windowSizeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.windowSizeLabel)
        self.windowSizeSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.windowSizeSpinBox.setObjectName("windowSizeSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.windowSizeSpinBox)
        self.numOfRangesLabel = QtWidgets.QLabel(self.groupbox)
        self.numOfRangesLabel.setObjectName("numOfRangesLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfRangesLabel)
        self.numOfRangesSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.numOfRangesSpinBox.setObjectName("numOfRangesSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfRangesSpinBox)
        self.verticalLayout.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.windowSizeLabel.setText(("Window Size"))
        self.numOfRangesLabel.setText(("Num of Ranges"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

