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
    gui = DataTable()
    gui.setupUi(form)

    datakey = 'test'

    gui.data = {datakey: repeat_df(5)}

    gui.chooseDataComboBox.addItem(datakey)
    gui.chooseDataComboBox.setItemText(0, datakey)

    gui.on_refreshTable()

def test_data_table_bad_key(qtbot):
    with pytest.raises(KeyError):
        form = QtWidgets.QWidget()
        gui = DataTable()
        gui.setupUi(form)

        datakey = 'test'

        gui.chooseDataComboBox.addItem(datakey)
        gui.chooseDataComboBox.setItemText(0, datakey)

        gui.on_refreshTable()
        gui.data['data_key'] == KeyError
