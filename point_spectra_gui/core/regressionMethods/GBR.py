from PyQt5 import QtWidgets
from point_spectra_gui.ui.GBR import Ui_Form
from point_spectra_gui.util.Modules import Modules
from sklearn.ensemble import GradientBoostingRegressor


class Ui_Form(Ui_Form, GradientBoostingRegressor, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        pass
        # self.numOfIterationsSpinBox.setValue(self.n_iter)
        # self.toleranceDoubleSpinBox.setValue(self.tol)
        # self.alpha1DoubleSpinBox.setValue(self.alpha_1)
        # self.alpha2DoubleSpinBox.setValue(self.alpha_2)
        # self.lambdaDoubleSpinBox.setValue(self.lambda_1)
        # self.lambdaDoubleSpinBox.setValue(self.lambda_2)
        # self.computerScoreCheckBox.setChecked(self.compute_score)
        # self.fitInterceptCheckBox.setChecked(self.fit_intercept)
        # self.normalizeCheckBox.setChecked(self.normalize)

    def run(self):
        loss = self.lossComboBox.currentText()
        if loss == 'Least Squares':
            loss = 'ls'
        if loss == 'Least Absolute Deviation':
            loss = 'lad'
        if loss == 'Huber':
            loss = 'huber'
        if loss == 'Quantile':
            loss = 'quantile'

        params = {'loss': loss,
                  'learning_rate': self.learningDoubleSpinBox.value(),
                  'n_estimators': self.numEstSpinBox.value(),
                  'subsample': self.subsampleDoubleSpinBox.value(),
                  'criterion': 'friedman_mse',
                  'min_samples_split': self.min_n_splitSpinBox.value(),
                  'min_samples_leaf': self.min_n_leafSpinBox.value(),
                  'min_weight_fraction_leaf': self.min_fractionDoubleSpinBox.value(),
                  'max_depth': self.max_depthSpinBox.value(),
                  'min_impurity_decrease': self.min_imp_decDoubleSpinBox.value(),
                  'random_state': 1,
                  'alpha': self.alphaDoubleSpinBox.value()
                  }
        return params, self.getChangedValues(params, GradientBoostingRegressor())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
