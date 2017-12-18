from PyQt5 import QtWidgets
from sklearn.linear_model.least_angle import LassoLars, LassoLarsCV, LassoLarsIC

from point_spectra_gui.ui.LassoLARS import Ui_Form
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
        # LassoLARS
        ll = LassoLars()
        self.alpha_text.setText(str(ll.alpha))
        self.fit_interceptCheckBox.setChecked(ll.fit_intercept)
        self.verboseCheckBox.setChecked(ll.verbose)
        self.normalizeCheckBox.setChecked(ll.normalize)
        self.setComboBox(self.precomputeComboBox, ['True', 'False', 'auto', 'array-like'])
        self.defaultComboItem(self.precomputeComboBox, ll.precompute)
        self.max_iterSpinBox.setValue(ll.max_iter)
        self.copy_XCheckBox.setChecked(ll.copy_X)
        self.fit_pathCheckBox.setChecked(ll.fit_path)
        self.positiveCheckBox.setChecked(ll.positive)

        # LassoLarsCV
        llcv = LassoLarsCV()
        self.max_n_alphasSpinBox.setValue(llcv.max_n_alphas)
        self.n_jobsSpinBox.setValue(llcv.n_jobs)

        # LassoLarsIC
        llic = LassoLarsIC()
        self.cvSpinBox.setValue(3)
        self.setComboBox(self.criterionComboBox, ['aic', 'bic'])
        self.defaultComboItem(self.criterionComboBox, llic.criterion)

    def function(self):
        model = self.modelComboBox.currentIndex()
        if model == 0:
            params = {
                'alpha': self.alpha_text.value(),
                'fit_intercept': self.fit_interceptCheckBox.isChecked(),
                'verbose': self.fit_interceptCheckBox.isChecked(),
                'normalize': self.normalizeCheckBox.isChecked(),
                'precompute': self.precomputeComboBox.currentText(),
                'max_iter': self.max_iterSpinBox.value(),
                'copy_X': self.copy_XCheckBox.isChecked(),
                'fit_path': self.fit_pathCheckBox.isChecked(),
                'positive': self.positiveCheckBox.isChecked(),
                'model': model
            }
            return params, self.getChangedValues(params, LassoLars())

        elif model == 1:
            params = {
                'fit_intercept': self.fit_interceptCheckBox.isChecked(),
                'verbose': self.fit_interceptCheckBox.isChecked(),
                'max_iter': self.max_iterSpinBox.value(),
                'normalize': self.normalizeCheckBox.isChecked(),
                'precompute': self.precomputeComboBox.currentText(),
                'cv': self.cvSpinBox.value(),
                'max_n_alphas': self.max_n_alphasSpinBox.value(),
                'n_jobs': self.n_jobsSpinBox.value(),
                'copy_X': self.copy_XCheckBox.isChecked(),
                'positive': self.positiveCheckBox.isChecked(),
                'model': model
            }
            return params, self.getChangedValues(params, LassoLarsCV())

        elif model == 2:
            params = {
                'criterion': self.criterionComboBox.currentText(),
                'fit_intercept': self.fit_interceptCheckBox.isChecked(),
                'verbose': self.fit_interceptCheckBox.isChecked(),
                'normalize': self.normalizeCheckBox.isChecked(),
                'precompute': self.precomputeComboBox.currentText(),
                'max_iter': self.max_iterSpinBox.value(),
                'copy_X': self.copy_XCheckBox.isChecked(),
                'positive': self.positiveCheckBox.isChecked(),
                'model': model
            }
            return params, self.getChangedValues(params, LassoLarsIC())
        else:
            params = {}
            print("Error")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
