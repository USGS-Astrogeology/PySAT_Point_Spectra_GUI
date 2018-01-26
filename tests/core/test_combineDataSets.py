import pytest
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets

from point_spectra_gui import core
from point_spectra_gui.core.CombineDataSets import CombineDataSets

def test_combine_datasets(qtbot, repeat_df_len10):
    form = QtWidgets.QWidget()
    gui = CombineDataSets()
    gui.setupUi(form)

    key1 = 'test1'
    key2 = 'test2'
    outkey = 'data'

    gui.data[key1] = repeat_df_len10
    gui.data[key2] = pd.DataFrame()

    gui.dataSet1ComboBox.addItem(key1)
    gui.dataSet1ComboBox.setItemText(0, key1)
    gui.dataSet2ComboBox.addItem(key2)
    gui.dataSet2ComboBox.setItemText(0, key2)
    gui.outputToDataSetTextBox.appendPlainText(outkey)

    gui.run()

    print(gui.dataSet1ComboBox.currentText(),gui.dataSet2ComboBox.currentText())
    print(gui.data)

    assert gui.data['data'].equals(pd.concat([gui.data[key1], gui.data[key2]]))
