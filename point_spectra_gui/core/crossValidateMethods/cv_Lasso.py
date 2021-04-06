import numpy as np
from PyQt5 import QtWidgets, QtCore
from sklearn.linear_model import Lasso

from point_spectra_gui.ui.cv_Lasso import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, Lasso, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.nalphas_spin.setValue(100)

        self.fit_intercept_list.setCurrentItem(
            self.fit_intercept_list.findItems(str(self.fit_intercept), QtCore.Qt.MatchExactly)[0])
        self.maxNumOfIterationsLineEdit.setText(str(self.max_iter))
        self.toleranceLineEdit.setText(str(self.tol))
        self.forcePositive_list.setCurrentItem(
            self.forcePositive_list.findItems(str(self.positive), QtCore.Qt.MatchExactly)[0])

    def run(self):
        fit_intercept_items = [i.text() == 'True' for i in self.fit_intercept_list.selectedItems()]
        positive_items = [i.text() == 'True' for i in self.forcePositive_list.selectedItems()]
        alphas = np.logspace(np.log10(float(self.min_alpha_line_edit.text())), np.log10(float(self.max_alpha_line_edit.text())),
                             num=self.nalphas_spin.value())
        params = {
                  'fit_intercept': fit_intercept_items,
                  'max_iter': [int(i) for i in self.maxNumOfIterationsLineEdit.text().split(',')],
                  'tol': [float(i) for i in self.toleranceLineEdit.text().split(',')],
                  'precompute': [True],
                  'copy_X': [True],
                  'positive': positive_items,
                  'selection': ['random']
                  }
        # keyparams = {}  # params.pop('alpha')
        # keyparams['alpha_min'] = self.minalpha_spin.value()
        # keyparams['alpha_max'] = self.maxalpha_spin.value()
        # keyparams['n_alpha'] = self.nalphas_spin.value()
        #
        # modelkey = str(keyparams)
        return params, list(alphas)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
