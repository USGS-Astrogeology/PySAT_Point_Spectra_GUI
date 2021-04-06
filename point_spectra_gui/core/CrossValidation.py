import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.util import Qtickle
from libpyhat.regression import cv
from point_spectra_gui.util.spectral_data import spectral_data
from point_spectra_gui.core.crossValidateMethods import *
from point_spectra_gui.ui.RegressionCV import Ui_Form
from point_spectra_gui.util.Modules import Modules
from sklearn.model_selection import ParameterGrid, LeaveOneGroupOut

class CrossValidation(Ui_Form, Modules):


    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Modules.setupUi(self, Form)
        self.regressionMethods()

    def get_widget(self):
        return self.formGroupBox

    def make_regression_widget(self, alg, params=None):
        self.hideAll()
        print(alg)
        try:
            self.alg[alg].setHidden(False)
        except:
            pass

    def connectWidgets(self):

        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.changeComboListVars(self.yVariableList, self.yvar_choices())
        self.changeComboListVars(self.xVariableList, self.xvar_choices())
        self.xvar_choices()
        self.ARDcheckbox.stateChanged.connect(
            lambda: self.toggle_regression_widget('ARD', self.ARDcheckbox.isChecked()))
        self.BRRcheckbox.stateChanged.connect(
            lambda: self.toggle_regression_widget('BRR',
                                                  self.BRRcheckbox.isChecked()))
        self.ENetcheckbox.stateChanged.connect(
            lambda: self.toggle_regression_widget('Elastic Net',
                                                  self.ENetcheckbox.isChecked()))
        # self.GPcheckBox.stateChanged.connect(
        #     lambda: self.toggle_regression_widget('GP - Gaussian Processes',
        #                                           self.GPcheckBox.isChecked()))
        #self.GPcheckBox.setDisabled(True)
        self.LARScheckbox.stateChanged.connect(
            lambda: self.toggle_regression_widget('LARS', self.LARScheckbox.isChecked()))
        self.LASSOcheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('LASSO', self.LASSOcheckBox.isChecked()))
        self.OLScheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('OLS', self.OLScheckBox.isChecked()))
        self.OMPcheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('OMP', self.OMPcheckBox.isChecked()))
        self.PLScheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('PLS', self.PLScheckBox.isChecked()))
        self.RidgecheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('Ridge', self.RidgecheckBox.isChecked()))
        self.SVRcheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('SVR', self.SVRcheckBox.isChecked()))
        self.LocalcheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('Local Regression', self.LocalcheckBox.isChecked()))
        self.GBRcheckBox.stateChanged.connect(
            lambda: self.toggle_regression_widget('GBR', self.GBRcheckBox.isChecked()))
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.yVariableList, self.yvar_choices()))
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.xVariableList, self.xvar_choices()))

        self.yVariableList.currentItemChanged.connect(self.set_yRange)

    def set_yRange(self):
        try:
            yvar = ('comp', self.yVariableList.currentItem().text())
            ymax = self.data[self.chooseDataComboBox.currentText()].df[yvar].max()
            ymin = self.data[self.chooseDataComboBox.currentText()].df[yvar].min()
            self.yMaxDoubleSpinBox.setValue(ymax)
            self.yMinDoubleSpinBox.setValue(ymin)
        except:
            print('Failed to update Y range. Selected data may be non-numeric!')

    def getGuiParams(self):
        """
        Overriding Modules' getGuiParams, because I'll need to do a list of lists
        in order to obtain the regressionMethods' parameters
        """
        self.qt = Qtickle.Qtickle(self)
        s = []
        s.append(self.qt.guiSave())
        for items in self.alg:
            s.append(self.alg[items][0].getGuiParams())
        return s


    def setGuiParams(self, dict):
        self.qt = Qtickle.Qtickle(self)
        self.qt.guiRestore(dict[0])
        keys = list(self.alg.keys())
        for i in range(len(dict)):
            self.alg[keys[i - 1]][0].setGuiParams(dict[i])

    def selectiveSetGuiParams(self, dict):
        """
        Override Modules' selective Restore function

        Setup Qtickle
        selectively restore the UI, the data to do that will be in the 0th element of the dictionary
        We will then iterate through the rest of the dictionary
        Will now restore the parameters for the algorithms in the list, Each of the algs have their own selectiveSetGuiParams

        :param dict:
        :return:
        """
        self.qt = Qtickle.Qtickle(self)
        self.qt.selectiveGuiRestore(dict[0])
        keys = list(self.alg.keys())
        for i in range(len(dict)):
            self.alg[keys[i - 1]].selectiveSetGuiParams(dict[i])


    def run(self):
        self.cv_results_combined = None #clear previous results in case of re-run

        if 'Model Coefficients' in self.datakeys:
            pass
        else:
            Modules.data_count += 1
            self.coef_index = Modules.data_count
            self.list_amend(self.datakeys, self.coef_index, 'Model Coefficients')

        Modules.data_count += 1
        self.results_index = Modules.data_count

        paramgrids = {}
        if self.ARDcheckbox.isChecked():
            paramgrids['ARD']=list(ParameterGrid(self.alg['ARD'][0].run()))
        if self.BRRcheckbox.isChecked():
            paramgrids['BRR']=list(ParameterGrid(self.alg['BRR'][0].run()))
        if self.ENetcheckbox.isChecked():
            enet_params=self.alg['Elastic Net'][0].run()
            params = enet_params[0]
            params['alpha'] = enet_params[1]
            paramgrids['Elastic Net']=list(ParameterGrid(params))
        # if self.GPcheckBox.isChecked():
        #     paramgrids.append(list(ParameterGrid(self.alg['GP - Gaussian Processes'][0].run())))
        if self.LARScheckbox.isChecked():
            paramgrids['LARS']=list(ParameterGrid(self.alg['LARS'][0].run()))
        if self.LASSOcheckBox.isChecked():
            lasso_params=self.alg['LASSO'][0].run()
            params = lasso_params[0]
            params['alpha'] = lasso_params[1]
            paramgrids['LASSO'] = list(ParameterGrid(params))
            #paramgrids['LASSO']={'alphas':lasso_params[1],'params':list(ParameterGrid(lasso_params[0]))}

        if self.OLScheckBox.isChecked():
            paramgrids['OLS']=list(ParameterGrid(self.alg['OLS'][0].run()))
        if self.OMPcheckBox.isChecked():
            paramgrids['OMP']=list(ParameterGrid(self.alg['OMP'][0].run()))
        if self.PLScheckBox.isChecked():
            paramgrids['PLS']=list(ParameterGrid(self.alg['PLS'][0].run()))
        if self.RidgecheckBox.isChecked():
            paramgrids['Ridge']=list(ParameterGrid(self.alg['Ridge'][0].run()))
        if self.SVRcheckBox.isChecked():
            paramgrids['SVR']=list(ParameterGrid(self.alg['SVR'][0].run()))
        if self.LocalcheckBox.isChecked():
            paramgrids['Local Regression']=list(ParameterGrid(self.alg['Local Regression'][0].run()))
        if self.GBRcheckBox.isChecked():
            paramgrids['GBR'] = list(ParameterGrid(self.alg['GBR'][0].run()))

        datakey = self.chooseDataComboBox.currentText()
        xvars = [str(x.text()) for x in self.xVariableList.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.yVariableList.selectedItems()]
        yrange = [self.yMinDoubleSpinBox.value(), self.yMaxDoubleSpinBox.value()]
        y = np.array(self.data[datakey].df[yvars])
        match = np.squeeze((y > yrange[0]) & (y < yrange[1]))
        data_for_cv = spectral_data(self.data[datakey].df.loc[match])


        for key in paramgrids.keys():
            print('===== Cross validating '+key+' =====')
            method=key
            #if the method supports it, separate out alpha from the other parameters and prepare for calculating path
            path_methods =  []#['Elastic Net', 'LASSO']#, 'Ridge']
            if method in path_methods:
                calc_path = True
                alphas = paramgrids[key]['alphas']
                paramgrid = paramgrids[key]['params']
            else:
                alphas = None
                calc_path = False
                paramgrid = paramgrids[key]

            cv_obj = cv.cv(paramgrid)

            data_for_cv_out, cv_results, cvmodels, cvmodelkeys, cvpredictkeys = cv_obj.do_cv(data_for_cv.df, xcols=xvars,
                                                                                         ycol=yvars, yrange=yrange, method=method,
                                                                                         alphas = alphas, calc_path = calc_path)

            try:
                cv_results[('cv','Data_file')] = self.datafiles[datakey]
            except:
                pass
            cv_results[('cv','ymin')] = yrange[0]
            cv_results[('cv','ymax')] = yrange[1]
            cv_results[('cv','ycol')] = yvars[0][1]

            data_for_cv = spectral_data(data_for_cv_out)

            self.cv_results_combined = pd.concat((self.cv_results_combined,cv_results))

            for key in cvpredictkeys:
                self.list_amend(self.predictkeys, len(self.predictkeys), key)

            for n, key in enumerate(cvmodelkeys):
                Modules.model_count += 1
                self.list_amend(self.modelkeys, Modules.model_count, key)
                self.models[key] = cvmodels[n]
                self.model_xvars[key] = xvars
                self.model_yvars[key] = yvars
                if method != 'GP':
                    try:
                        coef = np.squeeze(cvmodels[n].model.coef_)
                        coef = pd.DataFrame(coef)
                        coef.index = pd.MultiIndex.from_tuples(self.data[datakey].df[xvars].columns.values)
                        coef = coef.T
                        coef[('meta', 'Model')] = key
                        try:
                            coef[('meta', 'Intercept')] = cvmodels[n].model.intercept_
                        except:
                            pass
                        try:
                            self.data['Model Coefficients'] = spectral_data(
                                pd.concat([self.data['Model Coefficients'].df, coef]))
                        except:
                            self.data['Model Coefficients'] = spectral_data(coef)
                    except:
                        pass

        number = 1
        cvid = str('CV Results - ' + yvars[0][1])
        while cvid in self.datakeys:
            number += 1
            cvid = str('CV Results - ' + yvars[0][1]) + ' - ' + str(number)

        self.list_amend(self.datakeys,self.results_index,cvid)
        self.data[cvid] = spectral_data(self.cv_results_combined)

        Modules.data_count += 1
        new_datakey = datakey + '-' +str(yvars)+' '+ str(yrange)+'-CV Predictions'
        self.list_amend(self.datakeys, Modules.data_count, new_datakey)
        self.data[new_datakey] = spectral_data(data_for_cv_out)


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

    def toggle_regression_widget(self, alg, state):
        if state:
            self.alg[alg][0].setHidden(False)
        else:
            self.alg[alg][0].setHidden(True)

    def hideAll(self):
        for a in self.alg:
            self.alg[a].setHidden(True)

    def regressionMethods(self):
        self.alg = {'ARD': [cv_ARD.Ui_Form(),self.ARDLayout],
                    'BRR': [cv_BayesianRidge.Ui_Form(),self.BRRlayout],
                    'Elastic Net': [cv_ElasticNet.Ui_Form(),self.ENetlayout],
                    #'GP - Gaussian Processes': [cv_GP.Ui_Form(),self.GPlayout],
                    'LARS': [cv_LARS.Ui_Form(),self.LARSlayout],
                    'LASSO': [cv_Lasso.Ui_Form(),self.LASSOlayout],
                    'OLS': [cv_OLS.Ui_Form(),self.OLSLayout],
                    'OMP': [cv_OMP.Ui_Form(),self.OMPlayout],
                    'PLS': [cv_PLS.Ui_Form(),self.PLSLayout],
                    'Ridge': [cv_Ridge.Ui_Form(),self.Ridgelayout],
                    'SVR': [cv_SVR.Ui_Form(),self.SVRlayout],
                    'Local Regression': [cv_Local.Ui_Form(),self.Locallayout],
                    'GBR': [cv_GBR.Ui_Form(),self.GBRlayout]
                    }

        for key in self.alg.keys():
            self.alg[key][0].setupUi(self.Form)
            self.alg[key][1].addWidget(self.alg[key][0].get_widget())
            self.alg[key][0].setHidden(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = CrossValidation()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
