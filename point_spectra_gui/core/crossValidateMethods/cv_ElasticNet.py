from PyQt5 import QtWidgets
from sklearn.linear_model import ElasticNet
from sklearn.linear_model.coordinate_descent import ElasticNetCV

from point_spectra_gui.ui.ElasticNet import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, ElasticNet, ElasticNetCV, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.elasticNetCVGroupBox.setHidden(True)
        en = ElasticNet()
        encv = ElasticNetCV()

        self.enalphaDoubleSpinBox.setValue(en.alpha)
        self.enl1_ratioDoubleSpinBox.setValue(en.l1_ratio)
        self.enfit_interceptCheckBox.setChecked(en.fit_intercept)
        self.ennormalizeCheckBox.setChecked(en.normalize)
        self.enprecomputeCheckBox.setChecked(en.precompute)
        self.enmax_iterSpinBox.setValue(en.max_iter)
        self.encopy_XCheckBox.setChecked(en.copy_X)
        self.entolDoubleSpinBox.setValue(en.tol)
        self.enwarm_startCheckBox.setChecked(en.warm_start)
        self.enpositiveCheckBox.setChecked(en.positive)
        self.setComboBox(self.enselectionComboBox, ['cyclic', 'random'])
        self.defaultComboItem(self.enselectionComboBox, en.selection)

        self.l1_ratioDoubleSpinBox.setValue(encv.l1_ratio)
        self.epsDoubleSpinBox.setValue(encv.eps)
        self.n_alphasSpinBox.setValue(encv.n_alphas)
        self.alphasLineEdit.setText('None')
        self.fit_interceptCheckBox.setChecked(encv.fit_intercept)
        self.normalizeCheckBox.setChecked(encv.normalize)
        self.setComboBox(self.precomputeComboBox, ['True', 'False', 'auto', 'array-like'])
        self.defaultComboItem(self.precomputeComboBox, encv.precompute)
        self.max_iterSpinBox.setValue(encv.max_iter)
        self.tolDoubleSpinBox.setValue(encv.tol)
        self.cVSpinBox.setValue(3)
        self.copy_XCheckBox.setChecked(encv.copy_X)
        self.verboseCheckBox.setChecked(encv.verbose)
        self.n_jobsSpinBox.setValue(encv.n_jobs)
        self.positiveCheckBox.setChecked(encv.positive)
        self.setComboBox(self.selectionComboBox, ['cyclic', 'random'])
        self.defaultComboItem(self.selectionComboBox, encv.selection)

    def function(self):
        p_attrib = {'False': False, 'True': True, 'Array-like': 'array-like'}
        r_attrib = {'None': None}
        # TODO Add back the random state later.
        # try:
        #     r_state = int(self.randomStateLineEdit.text())
        # except:
        #     r_state = r_attrib[self.randomStateLineEdit.text()]

        index = self.precomputeComboBox.currentIndex()
        precomputeComboBox = self.precomputeComboBox.itemText(index)

        if self.CVCheckBox.isChecked():
            params = {
                'l1_ratio': self.l1_ratioDoubleSpinBox.value(),
                'eps': self.epsDoubleSpinBox.value(),
                'n_alphas': self.n_alphasSpinBox.value(),
                'alphas': {'None': None}.get(self.alphasLineEdit.text()),
                'fit_intercept': self.fit_interceptCheckBox.isChecked(),
                'normalize': self.normalizeCheckBox.isChecked(),
                'precompute': self.precomputeComboBox.currentText(),
                'max_iter': self.max_iterSpinBox.value(),
                'tol': self.max_iterSpinBox.value(),
                'cv': self.cVSpinBox.value(),
                'copy_X': self.copy_XCheckBox.isChecked(),
                'verbose': self.verboseCheckBox.isChecked(),
                'n_jobs': self.n_jobsSpinBox.value(),
                'positive': self.positiveCheckBox.isChecked(),
                'selection': self.selectionComboBox.currentText(),
                'CV': self.CVCheckBox.isChecked()}
        else:
            params = {
                'alpha': self.enalphaDoubleSpinBox.value(),
                'l1_ratio': self.enl1_ratioDoubleSpinBox.value(),
                'fit_intercept': self.enfit_interceptCheckBox.isChecked(),
                'normalize': self.ennormalizeCheckBox.isChecked(),
                'precompute': self.enprecomputeCheckBox.isChecked(),
                'max_iter': self.enmax_iterSpinBox.value(),
                'copy_X': self.encopy_XCheckBox.isChecked(),
                'tol': self.entolDoubleSpinBox.value(),
                'warm_start': self.enwarm_startCheckBox.isChecked(),
                'positive': self.enpositiveCheckBox.isChecked(),
                'selection': self.selectionComboBox.currentText(),
                'CV': self.CVCheckBox.isChecked()}

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
