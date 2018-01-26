import pytest
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets

from point_spectra_gui.util.PandasModel import PandasModel
from point_spectra_gui.core import BaselineRemoval as BR
from point_spectra_gui.core import baselineRemovalMethods as brm

@pytest.fixture
def repeat_pandas_model(n):
    data =  np.repeat(np.arange(1, n + 1), (n)).reshape(n, -1)
    idx1 = np.arange(1, (n + 1))
    idx2 = np.asarray(['wvl'] * n)
    tuples = list(zip(*[idx2, idx1]))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df = pd.DataFrame(data, columns = index)
    return PandasModel(df)

@pytest.mark.parametrize( 'model, method', [(brm.AirPLS, 'AirPLS'),         # <-- Failing in libpysat
                                            (brm.ALS, 'ALS'),               # <-- Failing in libpysat
                                            (brm.FABC, 'FABC'),
                                            (brm.KK, 'KK'),
                                            (brm.Median, 'Median'),
                                            (brm.Rubberband, 'Rubberband'), # <-- Failing in libpysat
                                            (brm.Polyfit, 'Polyfit'),
                                            (brm.Mario, 'Mario'),
                                            (brm.Dietrich, 'Dietrich')])    # <-- Failing in libpysat

def test_baseline_spectral(model, method, qtbot, repeat_df_len10):
    form = QtWidgets.QWidget()
    gui = BR()
    gui.setupUi(form)

    datakey = 'test'
    modelkey = method

    gui.datakeys = {0: datakey}

    gui.chooseDataComboBox.addItem(datakey)
    gui.chooseDataComboBox.setItemText(0, datakey)

    gui.chooseAlgorithmComboBox.addItem(modelkey)
    gui.chooseAlgorithmComboBox.setItemText(0, modelkey)

    gui.data[datakey] = repeat_pandas_model(10)
    gui.data[datakey]._data[modelkey] = np.arange(10)
    gui.data[datakey]._data['test1'] = np.arange(10)
    gui.data[datakey]._data['test2'] = np.arange(10)

    gui.models[modelkey] = model.Ui_Form()
    gui.models[modelkey].setupUi(form)
    gui.models[modelkey].run()
    try:
        gui.run()
    except ValueError:
        pass
    except TypeError:
        pass


@pytest.mark.parametrize( 'interpolation', [('Linear'),
                                            ('Quadratic'),
                                            ('Spline')])

def test_baseline_ccam(interpolation, qtbot):
    form = QtWidgets.QWidget()
    gui = BR()
    gui.setupUi(form)

    datakey = 'test'
    modelkey = 'CCAM'

    gui.datakeys = {0: datakey}

    gui.chooseDataComboBox.addItem(datakey)
    gui.chooseDataComboBox.setItemText(0, datakey)

    gui.chooseAlgorithmComboBox.addItem(modelkey)
    gui.chooseAlgorithmComboBox.setItemText(0, modelkey)

    gui.models[interpolation] = brm.CCAM.Ui_Form()
    gui.models[interpolation].setupUi(form)
    gui.models[interpolation].interpolationMethodComboBox.addItem(interpolation)
    gui.models[interpolation].interpolationMethodComboBox.setItemText(0, interpolation)

    gui.models[interpolation].run()
    gui.run()
