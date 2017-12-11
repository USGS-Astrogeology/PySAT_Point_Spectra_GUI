from PyQt5 import QtWidgets,QtCore
from sklearn.gaussian_process.gaussian_process import GaussianProcess

from point_spectra_gui.ui.cv_GP import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, GaussianProcess, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        self.checkMinAndMax()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.DimRedList.setCurrentItem(self.DimRedList.findItems('PCA',QtCore.Qt.MatchExactly)[0])
        self.regression_list.setCurrentItem(self.regression_list.findItems('Linear',QtCore.Qt.MatchExactly)[0])
        self.CorrelationList.setCurrentItem(self.CorrelationList.findItems('Squared Exponential',QtCore.Qt.MatchExactly)[0])
        self.theta0LineEdit.setText(str(self.theta0))
        self.ThetaL.setText(str(self.thetaL))
        self.ThetaU.setText(str(self.thetaU))
        self.randomStartLineEdit.setText(str(self.random_start))
        self.normalize_list.setCurrentItem(self.normalize_list.findItems(str(self.normalize),QtCore.Qt.MatchExactly)[0])

    def function(self):
        normalize_items = [i.text() == 'True' for i in self.normalize_list.selectedItems()]
        regr_items = [str(i.text().lower()) for i in self.regression_list.selectedItems()]
        corr_items = [str(i.text().lower().replace(' ','_')) for i in self.CorrelationList.selectedItems()]
        dim_red_items = [str(i.text()) for i in self.DimRedList.selectedItems()]
        params = {
            'reduce_dim': dim_red_items,
            'n_components': [int(i) for i in self.numOfComponenetsLineEdit.text().split(',')],
            'regr': regr_items,
            'corr': corr_items,
            'storage_mode': ['light'],
            'verbose': [True],
            'theta0': [float(i) for i in self.theta0LineEdit.text().split(',')],
            #where are the bounds on Theta? need to check this
            'normalize': [normalize_items],
            'optimizer': ['fmin_cobyla'],
            'random_start': [int(i) for i in self.randomStartLineEdit.text().split(',')],
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
