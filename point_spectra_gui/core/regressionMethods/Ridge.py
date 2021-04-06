import ast

from PyQt5 import QtWidgets
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeCV

from point_spectra_gui.ui.Ridge import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, Ridge, RidgeCV, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        ridge = Ridge()

        self.alphaDoubleSpinBox.setValue(ridge.alpha)
        self.fitInterceptCheckBox.setChecked(ridge.fit_intercept)
        self.normalizeCheckBox.setChecked(ridge.normalize)
        self.toleranceDoubleSpinBox.setValue(ridge.tol)

    def run(self):
        params = {'alpha': self.alphaDoubleSpinBox.value(),
                  'copy_X': True,
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'normalize': self.normalizeCheckBox.isChecked(),
                  'solver': 'auto',
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'random_state': 1
                  }
        return params, self.getChangedValues(params, Ridge())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
