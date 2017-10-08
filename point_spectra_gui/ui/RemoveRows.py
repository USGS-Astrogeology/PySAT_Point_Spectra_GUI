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
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.isLabel = QtWidgets.QLabel(self.groupBox)
        self.isLabel.setMaximumSize(QtCore.QSize(10, 16777215))
        self.isLabel.setObjectName("isLabel")
        self.gridLayout.addWidget(self.isLabel, 1, 2, 1, 1)
        self.removeRowsWhereLabel = QtWidgets.QLabel(self.groupBox)
        self.removeRowsWhereLabel.setObjectName("removeRowsWhereLabel")
        self.gridLayout.addWidget(self.removeRowsWhereLabel, 1, 0, 1, 1)
        self.valueComboBox = QtWidgets.QComboBox(self.groupBox)
        self.valueComboBox.setObjectName("valueComboBox")
        self.gridLayout.addWidget(self.valueComboBox, 1, 3, 1, 1)
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.colNameComboBox = QtWidgets.QComboBox(self.groupBox)
        self.colNameComboBox.setObjectName("colNameComboBox")
        self.gridLayout.addWidget(self.colNameComboBox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.chooseDataComboBox, self.colNameComboBox)
        Form.setTabOrder(self.colNameComboBox, self.valueComboBox)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Remove Rows"))
        self.isLabel.setText(("is "))
        self.removeRowsWhereLabel.setText(("Remove rows where"))
        self.chooseDataLabel.setText(("Choose Data:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

