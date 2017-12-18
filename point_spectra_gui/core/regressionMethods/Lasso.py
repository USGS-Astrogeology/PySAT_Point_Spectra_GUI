from PyQt5 import QtWidgets
from sklearn.linear_model.coordinate_descent import Lasso

from point_spectra_gui.ui.Lasso import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Lasso, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.alpha_text.setText(str(self.alpha))
        self.fitInterceptCheckBox.setChecked(self.fit_intercept)
        self.maxNumOfIterationsSpinBox.setValue(self.max_iter)
        self.toleranceDoubleSpinBox.setValue(self.tol)
        self.forcePositiveCoefficientsCheckBox.setChecked(self.positive)

    def function(self):
        params = {'alpha': float(self.alpha_text.text()),
                  'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                  'max_iter': int(self.maxNumOfIterationsSpinBox.value()),
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'positive': self.forcePositiveCoefficientsCheckBox.isChecked(),
                  'selection': 'random'}
#                  'CV': self.optimizeWCrossValidaitonCheckBox.isChecked()}
        return params, self.getChangedValues(params, Lasso())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
