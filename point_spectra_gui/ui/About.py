# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appNameLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.appNameLabel.setObjectName("appNameLabel")
        self.verticalLayout.addWidget(self.appNameLabel)
        self.versionLabel = QtWidgets.QLabel(Form)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout.addWidget(self.versionLabel)
        self.poweredByLabel = QtWidgets.QLabel(Form)
        self.poweredByLabel.setObjectName("poweredByLabel")
        self.verticalLayout.addWidget(self.poweredByLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.appNameLabel.setText(("PySAT Point Spectra Gui"))
        self.versionLabel.setText(("Version "))
        self.poweredByLabel.setText(("Powered by Qt for Python"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

