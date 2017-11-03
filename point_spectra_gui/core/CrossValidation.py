import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from pysat.regression import cv
from pysat.spectral.spectral_data import spectral_data

from Qtickle import Qtickle
from point_spectra_gui.core.crossValidateMethods import *
from point_spectra_gui.ui.CrossValidation import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class CrossValidation(Ui_Form, Basics):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Basics.setupUi(self, Form)
        self.regressionMethods()

    def get_widget(self):
        return self.groupLayout

    def make_regression_widget(self, alg, params=None):
        self.hideAll()
        print(alg)
        for i in range(len(self.algorithm_list) - 1):
            if alg == self.algorithm_list[i] and i > 0:
                self.alg[i - 1].setHidden(False)

    def connectWidgets(self):
        self.algorithm_list = ['Choose an algorithm',
                               'ARD',
                               'BRR',
                               'Elastic Net',
                               'GP',
                               #'KRR',  This needs more work since it requires parameters for the kernel passed as an object
                               'LARS',
                               'LASSO',
                               'LASSO LARS',
                               'OLS',
                               'OMP',
                               'PLS',
                               'Ridge',
                               'SVR']


        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseAlgorithmComboBox, self.algorithm_list)
        self.yMaxDoubleSpinBox.setMaximum(999999)
        self.yMinDoubleSpinBox.setMaximum(999999)
        self.yMaxDoubleSpinBox.setValue(100)
        self.changeComboListVars(self.yVariableList, self.yvar_choices())
        self.changeComboListVars(self.xVariableList, self.xvar_choices())
        self.xvar_choices()
        self.chooseAlgorithmComboBox.currentIndexChanged.connect(
            lambda: self.make_regression_widget(self.chooseAlgorithmComboBox.currentText()))
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.yVariableList, self.yvar_choices()))
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.xVariableList, self.xvar_choices()))

    def getGuiParams(self):
        """
        Overriding Basics' getGuiParams, because I'll need to do a list of lists
        in order to obtain the regressionMethods' parameters
        """
        self.qt = Qtickle.Qtickle(self)
        s = []
        s.append(self.qt.guiSave())
        for items in self.alg:
            s.append(items.getGuiParams())
        return s

    def setGuiParams(self, dict):
        self.qt = Qtickle.Qtickle(self)
        self.qt.guiRestore(dict[0])
        for i in range(len(dict)):
            self.alg[i - 1].setGuiParams(dict[i])

    def function(self):
        method = self.chooseAlgorithmComboBox.currentText()
        datakey = self.chooseDataComboBox.currentText()
        xvars = [str(x.text()) for x in self.xVariableList.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.yVariableList.selectedItems()]
        yrange = [self.yMinDoubleSpinBox.value(), self.yMaxDoubleSpinBox.value()]
        params, modelkey = self.getMethodParams(self.chooseAlgorithmComboBox.currentIndex())

        y = np.array(self.data[datakey].df[yvars])
        match = np.squeeze((y > yrange[0]) & (y < yrange[1]))
        data_for_cv = spectral_data(self.data[datakey].df.ix[match])
        # Warning: Params passing through cv.cv(params) needs to be in lists
        # Example: {'n_components': [4], 'scale': [False]}
        cv_obj = cv.cv(params)
        self.data[datakey].df, self.cv_results, cvmodels, cvmodelkeys = cv_obj.do_cv(data_for_cv.df, xcols=xvars, ycol=yvars,
                                                              yrange=yrange, method=method)
        for n, key in enumerate(cvmodelkeys):
            self.modelkeys.append(key)
            self.models[key] = cvmodels[n]
            if method != 'GP':
                coef = np.squeeze(cvmodels[n].model.coef_)
                coef = pd.DataFrame(coef)
                coef.index = pd.MultiIndex.from_tuples(self.data[datakey].df[xvars].columns.values)
                coef = coef.T
                coef[('meta', 'Model')] = key
                try:
                    coef[('meta','Intercept')] = cvmodels[n].model.intercept_
                except:
                    pass
                try:
                    self.data['Model Coefficients'] = spectral_data(pd.concat([self.data['Model Coefficients'].df, coef]))
                except:
                    self.data['Model Coefficients'] = spectral_data(coef)
                    self.datakeys.append('Model Coefficients')

        self.datakeys.append('CV Results ' + modelkey)
        self.data['CV Results ' + modelkey] = self.cv_results

    def yvar_choices(self):
        try:
            yvarchoices = self.data[self.chooseDataComboBox.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def xvar_choices(self):
        try:
            xvarchoices = self.data[self.chooseDataComboBox.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices

    def hideAll(self):
        for a in self.alg:
            a.setHidden(True)

    def getMethodParams(self, index):
        return self.alg[index - 1].function()

    def regressionMethods(self):
        self.alg = []
        list_forms = [cv_ARD,
                      cv_BayesianRidge,
                      cv_ElasticNet,
                      cv_GP,
        #              cv_KRR,
                      cv_LARS,
                      cv_Lasso,
                      cv_LassoLARS,
                      cv_OLS,
                      cv_OMP,
                      cv_PLS,
                      cv_Ridge,
                      cv_SVR
                      ]
        for items in list_forms:
            self.alg.append(items.Ui_Form())
            self.alg[-1].setupUi(self.Form)
            self.algorithmLayout.addWidget(self.alg[-1].get_widget())
            self.alg[-1].setHidden(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = CrossValidation()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
