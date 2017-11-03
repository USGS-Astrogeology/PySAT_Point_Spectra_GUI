from PyQt5 import QtWidgets, QtCore
from sklearn.svm.classes import SVR

from point_spectra_gui.ui.cv_SVR import Ui_Form
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

        self.cLineEdit.setText(str(svr.C))
        self.epsilonLineEdit.setText(str(svr.epsilon))
        self.kernel_list.setCurrentItem(self.kernel_list.findItems('Radial Basis Function',QtCore.Qt.MatchExactly)[0])
        self.degreeLineEdit.setText(str(svr.degree))
        self.coeff0LineEdit.setText(str(svr.coef0))
        self.shrinking_list.setCurrentItem(self.shrinking_list.findItems(str(svr.shrinking),QtCore.Qt.MatchExactly)[0])
        self.toleranceLineEdit.setText(str(svr.tol))
        self.maxIterationsLineEdit.setText(str(svr.max_iter))

    def function(self):
        kernels = [str(i.text()) for i in self.kernel_list.selectedItems()]
        shrinking_items = [i.text() == 'True' for i in self.shrinking_list.selectedItems()]
        params = {'C': [float(i) for i in self.cLineEdit.text().split(',')],
                  'epsilon': [float(i) for i in self.epsilonLineEdit.text().split(',')],
                  'kernel': kernels,
                  'degree': [int(i) for i in self.degreeLineEdit.text().split(',')],
                  'gamma': ['auto'],
                  'coef0': [float(i) for i in self.coeff0LineEdit.text().split(',')],
                  'shrinking': shrinking_items,
                  'tol': [float(i) for i in self.toleranceLineEdit.text().split(',')],
                  'cache_size': [200],
                  'verbose': [True],
                  'max_iter': [int(i) for i in self.maxIterationsLineEdit.text().split(',')]}
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
