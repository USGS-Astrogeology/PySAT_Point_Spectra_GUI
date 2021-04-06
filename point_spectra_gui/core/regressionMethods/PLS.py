from PyQt5 import QtWidgets
from sklearn.cross_decomposition import PLSRegression

from point_spectra_gui.ui.PLS import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, PLSRegression, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.numOfComponentsLineEdit.setText(str(self.n_components))

    def run(self):
        nc = self.numOfComponentsLineEdit.text().split(',')
        nc = [int(i) for i in nc]
        params = {'n_components': nc[0],
                  'scale': False}
        modelkey = '(nc=' + str(params['n_components']) + ')'
        return params, modelkey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
