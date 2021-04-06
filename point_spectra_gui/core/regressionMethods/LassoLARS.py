from PyQt5 import QtWidgets
from sklearn.linear_model import LassoLars

from point_spectra_gui.ui.LassoLARS import Ui_Form
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
        # LassoLARS
        ll = LassoLars()
        self.alpha_text.setText(str(ll.alpha))
        self.fit_interceptCheckBox.setChecked(ll.fit_intercept)
        self.normalizeCheckBox.setChecked(ll.normalize)
        self.max_iterSpinBox.setValue(ll.max_iter)
        self.positiveCheckBox.setChecked(ll.positive)

    def run(self):
            params = {
                'alpha': self.alpha_text.text(),
                'fit_intercept': self.fit_interceptCheckBox.isChecked(),
                'verbose': False,
                'normalize': self.normalizeCheckBox.isChecked(),
                'precompute': True,
                'max_iter': self.max_iterSpinBox.value(),
                'copy_X': True,
                'fit_path': True,
                'positive': self.positiveCheckBox.isChecked()
            }
            params_check=dict(params)
            return params, self.getChangedValues(params_check, LassoLars())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
