# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(332, 96)
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
        self.fitInterceptLabel = QtWidgets.QLabel(self.groupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fit_intercept_list = QtWidgets.QListWidget(self.groupBox)
        self.fit_intercept_list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fit_intercept_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.fit_intercept_list.setObjectName("fit_intercept_list")
        item = QtWidgets.QListWidgetItem()
        self.fit_intercept_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.fit_intercept_list.addItem(item)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fit_intercept_list)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        __sortingEnabled = self.fit_intercept_list.isSortingEnabled()
        self.fit_intercept_list.setSortingEnabled(False)
        item = self.fit_intercept_list.item(0)
        item.setText(("True"))
        item = self.fit_intercept_list.item(1)
        item.setText(("False"))
        self.fit_intercept_list.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

