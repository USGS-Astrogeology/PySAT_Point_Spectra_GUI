from PyQt5 import QtWidgets,QtCore
from sklearn.linear_model.coordinate_descent import Lasso
import numpy as np
from point_spectra_gui.ui.cv_Lasso import Ui_Form
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

        self.minalpha_spin.setValue(1.0)
        self.maxalpha_spin.setValue(1e3)
        self.nalphas_spin.setValue(10)

        self.fit_intercept_list.setCurrentItem(self.fit_intercept_list.findItems(str(self.fit_intercept),QtCore.Qt.MatchExactly)[0])
        self.maxNumOfIterationsLineEdit.setText(str(self.max_iter))
        self.toleranceLineEdit.setText(str(self.tol))
        self.forcePositive_list.setCurrentItem(self.forcePositive_list.findItems(str(self.positive),QtCore.Qt.MatchExactly)[0])

    def function(self):
        fit_intercept_items = [i.text() == 'True' for i in self.fit_intercept_list.selectedItems()]
        positive_items = [i.text() == 'True' for i in self.forcePositive_list.selectedItems()]
        alphas = np.logspace(np.log10(self.minalpha_spin.value()*1e10), np.log10(self.maxalpha_spin.value()*1e10),
                       num=self.nalphas_spin.value())
        params = {'alpha': alphas,
                  'fit_intercept': fit_intercept_items,
                  'max_iter': [int(i) for i in self.maxNumOfIterationsLineEdit.text().split(',')],
                  'tol': [float(i) for i in self.toleranceLineEdit.text().split(',')],
                  'positive': positive_items,
                  'selection': ['random']
                  }
        keyparams = params.pop('alpha')
        keyparams['alpha_min']=self.minalpha_spin.value()*1e10
        keyparams['alpha_max'] = self.maxalpha_spin.value() * 1e10
        keyparams['n_alpha'] = self.nalphas_spin.value()

        modelkey = str(keyparams)
        return params, modelkey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
