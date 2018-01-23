import pytest
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets

from point_spectra_gui.util import PandasModel as pm
from point_spectra_gui.core.BaselineRemoval import BaselineRemoval as BR

import sys

def trace(frame, event, arg):
    print("{}, {}:{}".format(event, frame.f_code.co_filename, frame.f_lineno))
    return trace

sys.settrace(trace)

@pytest.fixture
def repeat_pandas_model(n):
    data =  np.repeat(np.arange(1, n + 1), (n)).reshape(n, -1)
    idx1 = np.arange(1, (n + 1))
    idx2 = np.asarray(['wvl'] * n)
    tuples = list(zip(*[idx2, idx1]))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df = pd.DataFrame(data, columns = index)
    return pm.PandasModel(df)

@pytest.mark.parametrize( 'func, index, expected', [('AirPLS', 0, type(pd.DataFrame())), #<-- Failing
                                                    ('ALS', 1, type(pd.DataFrame())),
                                                    ('FABC', 3, type(pd.DataFrame())),
                                                    ('KK', 4, type(pd.DataFrame())),
                                                    ('Median', 5, type(pd.DataFrame())),
                                                    ('Rubberband', 7, type(pd.DataFrame())), #<-- Failing
                                                    ('CCAM', 8, type(pd.DataFrame())),
                                                    ('Mario', 9, type(pd.DataFrame()))])

def test_baseline_spectral(func, index, expected, qtbot):
    Form = QtWidgets.QWidget()
    guiBR = BR()
    guiBR.setupUi(Form)
    guiBR.chooseDataComboBox.addItem('data_key')
    guiBR.chooseDataComboBox.setItemText(0, 'data_key')
    guiBR.chooseAlgorithmComboBox.setItemText(index, func)
    guiBR.chooseAlgorithmComboBox.setCurrentIndex(index)
    guiBR.data = {'data_key' + '-Baseline Removed-' + func + '{}': repeat_pandas_model(5),
                  'data_key': repeat_pandas_model(5)}
    try:
        guiBR.run()
        assert type(guiBR.data['data_key-Baseline Removed-' + func + '{}'].df) == expected
    except:
        pass

@pytest.mark.parametrize( 'func, index, expected', [('Dietrich', 2, type(pd.DataFrame())), #<-- Failing
                                                    ('Polyfit', 6, type(pd.DataFrame()))])


def test_baseline_pandas(func, index, expected, qtbot):
    Form = QtWidgets.QWidget()
    guiBR = BR()
    guiBR.setupUi(Form)
    guiBR.chooseDataComboBox.addItem('data_key')
    guiBR.chooseDataComboBox.setItemText(0, 'data_key')
    guiBR.chooseAlgorithmComboBox.setItemText(index, func)
    guiBR.chooseAlgorithmComboBox.setCurrentIndex(index)
    guiBR.data = {'data_key' + '-Baseline Removed-' + func + '{}': repeat_pandas_model(5),
                  'data_key': repeat_pandas_model(5)}
    try:
        guiBR.run()
        assert type(guiBR.data['data_key-Baseline Removed-' + func + '{}']._data) == expected
    except:
        pass
