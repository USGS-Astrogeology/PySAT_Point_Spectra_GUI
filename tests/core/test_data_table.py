import pytest
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets

from point_spectra_gui.util.PandasModel import PandasModel as pm
from point_spectra_gui.core import DataTable

@pytest.fixture
def repeat_df(n):
    data =  np.repeat(np.arange(1, n + 1), (n)).reshape(n, -1)
    columns = np.arange(1, n + 1)
    df = pd.DataFrame(data, columns = columns)
    return pm(df)

def test_data_table(qtbot):
    form = QtWidgets.QWidget()
    guiDT = DataTable()
    guiDT.setupUi(form)

    guiDT.data = {'data_key': repeat_df(5)}

    guiDT.chooseDataComboBox.addItem('data_key')
    guiDT.chooseDataComboBox.setItemText(0, 'data_key')

    guiDT.on_refreshTable()

    assert type(guiDT.data['data_key']._data) == type(pd.DataFrame())

def test_data_table_bad_key(qtbot):
    with pytest.raises(KeyError):
        form = QtWidgets.QWidget()
        guiDT = DataTable()
        guiDT.setupUi(form)

        guiDT.chooseDataComboBox.addItem('data_key')
        guiDT.chooseDataComboBox.setItemText(0, 'data_key')

        guiDT.on_refreshTable()
        guiDT.data['data_key'] == KeyError
