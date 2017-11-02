import ast

from PyQt5 import QtWidgets,QtCore
from sklearn.linear_model.ridge import Ridge
from sklearn.linear_model.ridge import RidgeCV

from point_spectra_gui.ui.cv_Ridge import Ui_Form
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
        ridge = Ridge()

        self.alphaLineEdit.setText(str(ridge.alpha))
        self.fit_intercept_list.setCurrentItem(self.fit_intercept_list.findItems(str(ridge.fit_intercept),QtCore.Qt.MatchExactly)[0])
        self.normalize_list.setCurrentItem(self.normalize_list.findItems(str(ridge.normalize),QtCore.Qt.MatchExactly)[0])
        self.toleranceLineEdit.setText(str(ridge.tol))
        self.maxNumOfIterationslineEdit.setText(str(ridge.max_iter))


    def function(self):
        fit_intercept_items = [i.text() == 'True' for i in self.fit_intercept_list.selectedItems()]
        normalize_items = [i.text() == 'True' for i in self.normalize_list.selectedItems()]

        params = {'alpha': self.alphaLineEdit.text().split(','),
                  'copy_X': True,
                  'fit_intercept': fit_intercept_items,
                  'max_iter': self.maxNumOfIterationslineEdit.text().split(','),
                  'normalize': normalize_items,
                  'solver': 'auto',
                  'tol': self.toleranceLineEdit.text().split(','),
                  'random_state': None}
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
