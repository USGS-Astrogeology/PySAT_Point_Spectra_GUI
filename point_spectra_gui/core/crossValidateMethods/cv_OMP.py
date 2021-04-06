from PyQt5 import QtWidgets, QtCore
from sklearn.linear_model import OrthogonalMatchingPursuit
from sklearn.linear_model import OrthogonalMatchingPursuitCV

from point_spectra_gui.ui.cv_OMP import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.fit_intercept_list.setCurrentItem(
            self.fit_intercept_list.findItems(str(self.fit_intercept), QtCore.Qt.MatchExactly)[0])
        self.normalize_list.setCurrentItem(
            self.normalize_list.findItems(str(self.normalize), QtCore.Qt.MatchExactly)[0])

    def run(self):
        fit_intercept_items = [i.text() == 'True' for i in self.fit_intercept_list.selectedItems()]
        normalize_items = [i.text() == 'True' for i in self.normalize_list.selectedItems()]

        params = {'n_nonzero_coefs': [int(i) for i in self.n_coefs_lineedit.text().split(',')],
                  'fit_intercept': fit_intercept_items,
                  'normalize': normalize_items,
                  'precompute': ['auto']}
        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
