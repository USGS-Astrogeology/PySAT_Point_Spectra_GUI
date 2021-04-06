# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupLayout = QtWidgets.QGroupBox(Form)
        self.groupLayout.setObjectName("groupLayout")
        self.gridLayout = QtWidgets.QGridLayout(self.groupLayout)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.n_endmembers_label = QtWidgets.QLabel(self.groupLayout)
        self.n_endmembers_label.setObjectName("n_endmembers_label")
        self.horizontalLayout.addWidget(self.n_endmembers_label)
        self.n_endmembers_spinBox = QtWidgets.QSpinBox(self.groupLayout)
        self.n_endmembers_spinBox.setMinimum(1)
        self.n_endmembers_spinBox.setProperty("value", 4)
        self.n_endmembers_spinBox.setObjectName("n_endmembers_spinBox")
        self.horizontalLayout.addWidget(self.n_endmembers_spinBox)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupLayout)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.horizontalLayout_3.addWidget(self.chooseDataLabel)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupLayout)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.horizontalLayout_3.addWidget(self.chooseDataComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseAlgorithmLabel = QtWidgets.QLabel(self.groupLayout)
        self.chooseAlgorithmLabel.setObjectName("chooseAlgorithmLabel")
        self.horizontalLayout_2.addWidget(self.chooseAlgorithmLabel)
        self.chooseAlgorithmComboBox = QtWidgets.QComboBox(self.groupLayout)
        self.chooseAlgorithmComboBox.setObjectName("chooseAlgorithmComboBox")
        self.horizontalLayout_2.addWidget(self.chooseAlgorithmComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.xVariableLabel = QtWidgets.QLabel(self.groupLayout)
        self.xVariableLabel.setObjectName("xVariableLabel")
        self.gridLayout.addWidget(self.xVariableLabel, 1, 0, 1, 1)
        self.xVariableList = QtWidgets.QListWidget(self.groupLayout)
        self.xVariableList.setObjectName("xVariableList")
        item = QtWidgets.QListWidgetItem()
        self.xVariableList.addItem(item)
        self.gridLayout.addWidget(self.xVariableList, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupLayout.setTitle(("Endmember Identification"))
        self.n_endmembers_label.setText(("# of endmembers"))
        self.chooseDataLabel.setText(("Choose Data"))
        self.chooseAlgorithmLabel.setText(("Choose Algorithm"))
        self.xVariableLabel.setText(("X Variable"))
        __sortingEnabled = self.xVariableList.isSortingEnabled()
        self.xVariableList.setSortingEnabled(False)
        item = self.xVariableList.item(0)
        item.setText(("Choose X"))
        self.xVariableList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

