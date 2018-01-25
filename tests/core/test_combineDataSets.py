import pytest
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtWidgets

from point_spectra_gui import core
from point_spectra_gui.core.CombineDataSets import CombineDataSets

def test_combine_datasets(qtbot):
    form = QtWidgets.QWidget()
    guiCD = CombineDataSets()
    guiCD.setupUi(form)

    guiCD.dataSet1ComboBox.addItem('test1')
    guiCD.dataSet1ComboBox.setItemText(0, 'test1')

    guiCD.dataSet2ComboBox.addItem('test2')
    guiCD.dataSet2ComboBox.setItemText(0, 'test2')

    guiCD.outputToDataSetComboBox.addItem('data')
    guiCD.outputToDataSetComboBox.setItemText(0, 'data')

    guiCD.run()

    assert guiCD.data['data'] == 'test1test2'
