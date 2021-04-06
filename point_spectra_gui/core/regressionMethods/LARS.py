from PyQt5 import QtWidgets
from sklearn.linear_model import Lars


from point_spectra_gui.ui.LARS import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        # LARS/         # LARSCV

        lars = Lars()
        self.fit_interceptCheckBox.setChecked(lars.fit_intercept)
        self.normalizeCheckBox.setChecked(lars.normalize)
        self.n_nonzero_coefsSpinBox.setValue(lars.n_nonzero_coefs)


    def run(self):
        params = {
            'fit_intercept': self.fit_interceptCheckBox.isChecked(),
            'verbose': False,
            'normalize': self.normalizeCheckBox.isChecked(),
            'precompute': 'auto',
            'n_nonzero_coefs': self.n_nonzero_coefsSpinBox.value(),
            'copy_X': True,
            'fit_path': True
            }
        return params, self.getChangedValues(params, Lars())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
