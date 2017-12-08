import ast

from PyQt5 import QtWidgets
from sklearn.linear_model.ridge import Ridge
from sklearn.linear_model.ridge import RidgeCV

from point_spectra_gui.ui.Ridge import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Ridge, RidgeCV, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.Ridge.setVisible(False)
        ridgecv = RidgeCV()

        self.alphasLineEdit_cv.setText(str(ridgecv.alphas))
        self.fitInterceptCheckBox_cv.setChecked(ridgecv.fit_intercept)
        self.normalizeCheckBox_cv.setChecked(ridgecv.normalize)
        self.defaultComboItem(self.scoringComboBox_cv, ridgecv.scoring)
        self.defaultComboItem(self.gCVModeComboBox_cv, ridgecv.gcv_mode)
        self.storeCVValuesCheckBox_cv.setChecked(ridgecv.store_cv_values)

        ridge = Ridge()

        self.alphaDoubleSpinBox.setValue(ridge.alpha)
        self.fitInterceptCheckBox.setChecked(ridge.fit_intercept)
        self.normalizeCheckBox.setChecked(ridge.normalize)
        self.copyXCheckBox.setChecked(ridge.copy_X)
        self.defaultComboItem(self.solverComboBox, ridge.solver)
        self.toleranceDoubleSpinBox.setValue(ridge.tol)
        self.randomStateLineEdit.setText(str(ridge.random_state))

    def function(self):
        m_attrib = {'None': None}
        r_attrib = {'None': None}
        try:
            m_state = int(self.maxNumOfIterationslineEdit.text())
        except:
            m_state = m_attrib[self.maxNumOfIterationslineEdit.text()]
        try:
            r_state = int(self.randomStateLineEdit.text())
        except:
            r_state = r_attrib[self.randomStateLineEdit.text()]

        if self.crossValidateCheckBox.isChecked():
            params = {'alphas': ast.literal_eval(self.alphasLineEdit_cv.text()),
                      'fit_intercept': self.fitInterceptCheckBox_cv.isChecked(),
                      'normalize': self.normalizeCheckBox_cv.isChecked(),
                      'scoring': {'None': None}.get(self.scoringComboBox_cv.currentText()),
                      'gcv_mode': {'None': None}.get(self.gCVModeComboBox_cv.currentText()),
                      'store_cv_values': self.storeCVValuesCheckBox_cv.isChecked(),
                      'CV': self.crossValidateCheckBox.isChecked()}
            return params, self.getChangedValues(params, RidgeCV())

        else:
            params = {'alpha': self.alphaDoubleSpinBox.value(),
                      'copy_X': self.copyXCheckBox.isChecked(),
                      'fit_intercept': self.fitInterceptCheckBox.isChecked(),
                      'max_iter': m_state,
                      'normalize': self.normalizeCheckBox.isChecked(),
                      'solver': self.solverComboBox.currentText(),
                      'tol': self.toleranceDoubleSpinBox.value(),
                      'random_state': r_state,
                      'CV': self.crossValidateCheckBox.isChecked()}
            return params, self.getChangedValues(params, Ridge())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
