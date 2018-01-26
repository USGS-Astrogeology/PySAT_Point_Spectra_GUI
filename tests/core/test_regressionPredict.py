import pytest
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets

from point_spectra_gui import core
from point_spectra_gui.core.CombineDataSets import CombineDataSets
from point_spectra_gui.util.PandasModel import PandasModel
from point_spectra_gui.core import regressionMethods as rm

from point_spectra_gui.core.RegressionPredict import RegressionPredict

@pytest.fixture
def predict_data():
    pass


@pytest.mark.parametrize('model', [
    rm.BayesianRidge,
    rm.ARD,
    rm.ElasticNet,
    rm.GP,
    rm.KRR,
    rm.Lasso,
    rm.OLS,
    rm.PLS,
    rm.Ridge,
])
def test_regresstion_predict(qtbot, repeat_df_len10, model):
    form = QtWidgets.QWidget()
    gui = RegressionPredict()
    gui.setupUi(form)

    datakey = 'test'
    modelkey = 'model'
    predictname = ('predict', modelkey + ' - ' + datakey + ' - Predict')

    gui.chooseDataComboBox.addItem(datakey)
    gui.chooseDataComboBox.setItemText(0, datakey)
    gui.chooseModelComboBox.addItem(modelkey)
    gui.chooseModelComboBox.setItemText(0, modelkey)

    gui.model_xvars[modelkey] = ['test1', 'test2']

    gui.data[datakey] = PandasModel(repeat_df_len10.copy(deep=True))
    gui.data[datakey]._data[modelkey] = np.arange(10)
    gui.data[datakey]._data['test1'] = np.arange(10)
    gui.data[datakey]._data['test2'] = np.arange(10)

    gui.models[modelkey] = model.Ui_Form()
    gui.models[modelkey].setupUi(form)
    gui.models[modelkey].run()
    gui.models[modelkey].fit(gui.data[datakey]._data[gui.model_xvars[modelkey]], repeat_df_len10.index)
    gui.run()
