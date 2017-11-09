from PyQt5 import QtWidgets, QtCore
from sklearn.decomposition import FastICA
from point_spectra_gui.ui.dimred_FastICA import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, FastICA, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.nc_spin.setValue(8)

    def function(self):

        params = {
            'n_components': self.nc_spin.value()}
        params_key = str(params)
        return params, params_key


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
