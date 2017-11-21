from PyQt5 import QtWidgets, QtCore
from sklearn.manifold.locally_linear import LocallyLinearEmbedding
from point_spectra_gui.ui.dimred_LLE import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, LocallyLinearEmbedding, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.neighbors_spin.setValue(5)
        self.nc_spin.setValue(2)
        self.regularization_spin.setValue(0.001)
    def function(self):

        params = {
            'n_components': self.nc_spin.value(),
            'n_neighbors' : self.neighbors_spin.value(),
            'reg' : self.regularization_spin.value()}
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
