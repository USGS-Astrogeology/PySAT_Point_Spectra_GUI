from PyQt5 import QtWidgets
from sklearn.linear_model.least_angle import Lars
from sklearn.linear_model.least_angle import LarsCV

from point_spectra_gui.ui.LARS import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
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
        larscv = LarsCV()
        self.fit_interceptCheckBox.setChecked(lars.fit_intercept)
        self.verboseCheckBox.setChecked(lars.verbose)
        self.normalizeCheckBox.setChecked(lars.normalize)
        self.setComboBox(self.precomputeComboBox, ['True', 'False', 'auto', 'array-like'])
        self.defaultComboItem(self.precomputeComboBox, lars.precompute)
        self.n_nonzero_coefsSpinBox.setValue(lars.n_nonzero_coefs)
        self.copy_XCheckBox.setChecked(lars.copy_X)
        self.fit_pathCheckBox.setChecked(lars.fit_path)
        self.positiveCheckBox.setChecked(lars.positive)
        self.max_iterSpinBox.setValue(larscv.max_iter)
        self.max_n_alphasSpinBox.setValue(larscv.max_n_alphas)
        self.n_jobsSpinBox.setValue(larscv.n_jobs)

    def function(self):
        if self.cVCheckBox.isChecked():
            params = {
                'fit_intercept': self.fit_interceptCheckBox.isChecked(),
                'positive': self.positiveCheckBox.isChecked(),
                'max_iter': self.max_iterSpinBox.value(),
                'verbose': self.verboseCheckBox.isChecked(),
                'normalize': self.normalizeCheckBox.isChecked(),
                'precompute': self.precomputeComboBox.currentText(),
                'copy_X': self.copy_XCheckBox.isChecked(),
                'cv': self.cvSpinBox.value(),
                'max_n_alphas': self.max_n_alphasSpinBox.value(),
                'n_jobs': self.n_jobsSpinBox.value(),
                'CV': self.cVCheckBox.isChecked(),
            }
        else:
            params = {
                'fit_intercept': self.fit_interceptCheckBox.isChecked(),
                'verbose': self.verboseCheckBox.isChecked(),
                'normalize': self.normalizeCheckBox.isChecked(),
                'precompute': {'True': True, 'False': False, 'auto': 'auto', 'array-like': 'array-like'}.get(
                    self.precomputeComboBox.currentText()),
                'n_nonzero_coefs': self.n_nonzero_coefsSpinBox.value(),
                'copy_X': self.copy_XCheckBox.isChecked(),
                'fit_path': self.fit_pathCheckBox.isChecked(),
                'positive': self.positiveCheckBox.isChecked(),
                'CV': self.cVCheckBox.isChecked(),
            }

        modelkey = str(params)
        return params, modelkey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
