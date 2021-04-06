from PyQt5 import QtWidgets, QtCore
from sklearn.linear_model import Lars
from sklearn.linear_model import LarsCV

from point_spectra_gui.ui.cv_LARS import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        lars = Lars()
        self.fit_intercept_listWidget.setCurrentItem(
            self.fit_intercept_listWidget.findItems(str(lars.fit_intercept), QtCore.Qt.MatchExactly)[0])
        self.normalize_list.setCurrentItem(
            self.normalize_list.findItems(str(lars.normalize), QtCore.Qt.MatchExactly)[0])
        self.n_nonzero_coefsLineEdit.setText(str(lars.n_nonzero_coefs))

    def run(self):
        fit_intercept_items = [i.text() == 'True' for i in self.fit_intercept_listWidget.selectedItems()]
        normalize_items = [i.text() == 'True' for i in self.normalize_list.selectedItems()]

        params = {
            'fit_intercept': fit_intercept_items,
            'verbose': [True],
            'normalize': normalize_items,
            'precompute': ['auto'],
            'n_nonzero_coefs': [int(i) for i in self.n_nonzero_coefsLineEdit.text().split(',')],
            'copy_X': [True],
            'fit_path': [False]}

        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
