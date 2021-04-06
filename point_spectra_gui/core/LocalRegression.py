import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.util import Qtickle
from libpyhat.regression import regression
from point_spectra_gui.util.spectral_data import spectral_data
from point_spectra_gui.core.regressionMethods import *
from point_spectra_gui.ui.LocalRegression import Ui_Form
from point_spectra_gui.util.Modules import Modules
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LassoCV
from sklearn.model_selection import GroupKFold
from libpyhat.regression import local_regression

class LocalRegression(Ui_Form, Modules):
    count = -1

    def __init__(self):
        LocalRegression.count += 1
        self.curr_count = LocalRegression.count

    def delete(self):
        try:
            LocalRegression.count -= 1
            del self.models[self.modelkeys[-1]]
            del self.modelkeys[-1]
        except:
            pass

        LocalRegression.count -= 1
        self.modelkeys = self.modelkeys[:-1]

    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupLayout

    def make_regression_widget(self, alg, params=None):
        self.hideAll()
        #print(alg)
        try:
            self.alg[alg].setHidden(False)
        except:
            pass

    def connectWidgets(self):
        self.setComboBox(self.choosedata_train, self.datakeys)
        self.setComboBox(self.choosedata_predict, self.datakeys)
        self.changeComboListVars(self.yVariableList, self.yvar_choices())
        self.changeComboListVars(self.xVariableList, self.xvar_choices())
        self.xvar_choices()
        self.choosedata_train.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.yVariableList, self.yvar_choices()))
        self.choosedata_train.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.xVariableList, self.xvar_choices()))


    def run(self):
        method = self.chooseAlgorithmComboBox.currentText()
        xvars = [str(x.text()) for x in self.xVariableList.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.yVariableList.selectedItems()]
        fit_intercept = self.fit_intercept.isChecked()
        force_positive = self.forcepositive.isChecked()
        params = {'fit_intercept': self.fit_intercept.isChecked(),
                  'max_iter': 10000,
                  'positive': self.forcepositive.isChecked(),
                  'selection': 'random',
                  'l1_ratio': [.1, .5, .7, .9, .95, .99, 1]}
        localmodel = local_regression.LocalRegression(params, n_neighbors = self.n_neighbors_spin.value())
        traindata = self.data[self.choosedata_train.currentText()]
        predictdata = self.data[self.choosedata_predict.currentText()]
        x_train = np.array(traindata.df[xvars])
        y_train = np.array(traindata.df[yvars])
        x_predict = np.array(predictdata.df[xvars])
        predictions, coefs, intercepts = localmodel.fit_predict(x_train, y_train, x_predict)
        predictname = ('predict', 'Local LASSO - ' + self.choosedata_predict.currentText() + ' - Predict')
        self.data[self.choosedata_predict.currentText()].df[predictname] = predictions


        coefs = pd.DataFrame(coefs, columns = pd.MultiIndex.from_tuples(self.data[self.choosedata_predict.currentText()].df[xvars].columns.values))
        coefs[('meta', 'Intercept')] = intercepts
        try:
            self.data['Model Coefficients'] = spectral_data(pd.concat([self.data['Model Coefficients'].df, coefs]))
        except:
            self.data['Model Coefficients'] = spectral_data(coefs)
            self.datakeys.append('Model Coefficients')

    def yvar_choices(self):
        try:
            yvarchoices = self.data[self.choosedata_train.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def xvar_choices(self):
        try:
            xvarchoices = self.data[self.choosedata_train.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = LocalRegression()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
