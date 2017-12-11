from PyQt5 import QtWidgets, QtCore
from sklearn.linear_model.least_angle import LassoLars, LassoLarsCV, LassoLarsIC
import numpy as np
from point_spectra_gui.ui.cv_LassoLARS import Ui_Form
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
        self.minalpha_spin.setValue(0.0000001)
        self.maxalpha_spin.setValue(0.01)
        self.nalpha_spin.setValue(100)
        self.fit_intercept_list.setCurrentItem(self.fit_intercept_list.findItems(str(ll.fit_intercept),QtCore.Qt.MatchExactly)[0])
        self.normalize_list.setCurrentItem(self.normalize_list.findItems(str(ll.normalize),QtCore.Qt.MatchExactly)[0])
        self.max_iterLineEdit.setText(str(ll.max_iter))
        self.force_positive_list.setCurrentItem(self.force_positive_list.findItems(str(ll.positive),QtCore.Qt.MatchExactly)[0])


    def function(self):
        fit_intercept_items = [i.text() == 'True' for i in self.fit_intercept_list.selectedItems()]
        normalize_items = [i.text() == 'True' for i in self.normalize_list.selectedItems()]
        positive_items = [i.text() == 'True' for i in self.force_positive_list.selectedItems()]
        alphas = np.logspace(np.log10(self.minalpha_spin.value() * 1e10), np.log10(self.maxalpha_spin.value() * 1e10),
                             num=self.nalpha_spin.value())
        params = {
            'alpha': alphas,
            'fit_intercept': fit_intercept_items,
            'verbose': [True],
            'normalize': normalize_items,
            'precompute': ['auto'],
            'max_iter': [int(i) for i in self.max_iterLineEdit.text().split(',')],
            'copy_X': [True],
            'fit_path': [False],
            'positive': positive_items
        }


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
