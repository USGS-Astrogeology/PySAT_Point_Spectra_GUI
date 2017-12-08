from PyQt5 import QtWidgets
from sklearn.svm.classes import SVR

from point_spectra_gui.ui.SVR import Ui_Form
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
        svr = SVR()
        svr.kernel = 'rbf'
        svr.degree = 3
        svr.gamma = 'auto'
        svr.coef0 = 0.0
        svr.tol = 1e-3
        svr.C = 1.0
        svr.epsilon = 0.1
        svr.shrinking = True
        svr.cache_size = 200
        svr.verbose = False
        svr.max_iter = -1

        self.cDoubleSpinBox.setValue(svr.C)
        self.epsilonDoubleSpinBox.setValue(svr.epsilon)
        self.defaultComboItem(self.kernelComboBox, svr.kernel)
        self.degreeSpinBox.setValue(svr.degree)
        self.defaultComboItem(self.gammaComboBox, svr.gamma)
        self.coeff0DoubleSpinBox.setValue(svr.coef0)
        self.shrinkingCheckBox.setChecked(svr.shrinking)
        self.toleranceDoubleSpinBox.setValue(svr.tol)
        self.cacheSizeSpinBox.setValue(svr.cache_size)
        self.verboseCheckBox.setChecked(svr.verbose)
        self.maxIterationsSpinBox.setValue(svr.max_iter)

    def function(self):
        gamma_index = self.gammaComboBox.currentIndex()
        kernel_index = self.kernelComboBox.currentIndex()
        params = {'C': self.cDoubleSpinBox.value(),
                  'epsilon': self.epsilonDoubleSpinBox.value(),
                  'kernel': self.kernelComboBox.itemText(kernel_index),
                  'degree': self.degreeSpinBox.value(),
                  'gamma': self.gammaComboBox.itemText(gamma_index),
                  'coef0': self.coeff0DoubleSpinBox.value(),
                  'shrinking': self.shrinkingCheckBox.isChecked(),
                  'tol': self.toleranceDoubleSpinBox.value(),
                  'cache_size': self.cacheSizeSpinBox.value(),
                  'verbose': self.verboseCheckBox.isChecked(),
                  'max_iter': int(self.maxIterationsSpinBox.value())}

        return params, self.getChangedValues(params, SVR())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
