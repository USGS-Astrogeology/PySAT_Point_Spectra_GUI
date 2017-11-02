# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 153)
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
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.fit_intercept_list = QtWidgets.QListWidget(self.formGroupBox)
        self.fit_intercept_list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fit_intercept_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.fit_intercept_list.setObjectName("fit_intercept_list")
        item = QtWidgets.QListWidgetItem()
        self.fit_intercept_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.fit_intercept_list.addItem(item)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fit_intercept_list)
        self.normalize_list = QtWidgets.QListWidget(self.formGroupBox)
        self.normalize_list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.normalize_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.normalize_list.setObjectName("normalize_list")
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.normalize_list)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        self.normalizeLabel.setText(("Normalize"))
        __sortingEnabled = self.fit_intercept_list.isSortingEnabled()
        self.fit_intercept_list.setSortingEnabled(False)
        item = self.fit_intercept_list.item(0)
        item.setText(("True"))
        item = self.fit_intercept_list.item(1)
        item.setText(("False"))
        self.fit_intercept_list.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.normalize_list.isSortingEnabled()
        self.normalize_list.setSortingEnabled(False)
        item = self.normalize_list.item(0)
        item.setText(("True"))
        item = self.normalize_list.item(1)
        item.setText(("False"))
        self.normalize_list.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

