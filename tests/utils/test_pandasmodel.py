import pytest
import numpy as np
import pandas as pd

from PyQt5 import QtCore

from point_spectra_gui.util import PandasModel as pm

# PyQt is being difficult about imports
Horizontal = QtCore.Qt.Horizontal
Vertical = QtCore.Qt.Vertical
DisplayRole = QtCore.Qt.DisplayRole

@pytest.fixture
def repeat_pandas_model(n):
    data =  np.repeat(np.arange(1, n + 1), (n)).reshape(n,-1)
    columns = np.arange(1, n+1)
    df = pd.DataFrame(data, columns = columns)
    return pm.PandasModel(df)

@pytest.mark.parametrize( 'model, expected', [
    (repeat_pandas_model(5), 5),
    (repeat_pandas_model(6), 6),
    (repeat_pandas_model(20), 20)
])
def test_row_count(model, expected):
    assert model.rowCount() == expected


@pytest.mark.parametrize( 'model, expected', [
    (repeat_pandas_model(5), 5),
    (repeat_pandas_model(6), 6),
    (repeat_pandas_model(20), 20)
])
def test_row_count(model, expected):
    assert model.columnCount() == expected


@pytest.mark.parametrize('model, val, orientation, expected', [
    (repeat_pandas_model(6), 5, Horizontal, 6),
    (repeat_pandas_model(20), 10, Horizontal, 11),
    (repeat_pandas_model(6), 5, Vertical, 5),
    (repeat_pandas_model(20), 10, Vertical, 10),
    (repeat_pandas_model(20), 10, None, None)
])
def test_header_data(model, val, orientation, expected):
    assert model.headerData(val, orientation, DisplayRole) == expected
