import numpy as np
from PyQt5 import QtWidgets
from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui.RemoveRows import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class RemoveRows(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.colNameComboBox, self.get_colname_choices())
        self.setComboBox(self.valueComboBox, self.get_rowval_choices())
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.colNameComboBox, self.get_colname_choices()))
        self.colNameComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.valueComboBox, self.get_rowval_choices()))

    def function(self):
        datakey = self.chooseDataComboBox.currentText()
        colname = self.colNameComboBox.currentText()
        value = self.valueComboBox.currentText()
        value = value.split(' : ')[0]
        print(datakey, colname, value)
        print(self.data[datakey].df.shape)
        vars_level0 = self.data[datakey].df.columns.get_level_values(0)
        vars_level1 = self.data[datakey].df.columns.get_level_values(1)
        vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
        vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
        colname = (vars_level0[vars_level1.index(colname)], colname)

        if value == 'Null':
            self.data[datakey] = spectral_data(self.data[datakey].df.ix[-self.data[datakey].df[colname].isnull()])
        else:
            # find where the values in the specified column match the value to be removed
            coldata = np.array([str(i) for i in self.data[datakey].df[colname]])
            match = coldata == value
            # keep everything except where match is true
            self.data[datakey] = spectral_data(self.data[datakey].df.ix[~match])
        print(self.data[datakey].df.shape)

    def get_colname_choices(self):
        try:
            self.vars_level0 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = list(
                self.vars_level1[np.logical_and(self.vars_level0 != 'wvl', self.vars_level0 != 'masked')])
            self.vars_level0 = list(
                self.vars_level0[np.logical_and(self.vars_level0 != 'wvl', self.vars_level0 != 'masked')])

            colnamechoices = self.vars_level1

        except:
            try:
                colnamechoices = self.data[self.chooseDataComboBox.currentText()].columns.values
            except:
                colnamechoices = []
        colnamechoices = [i for i in colnamechoices if not 'Unnamed' in str(i)]  # remove unnamed columns from choices
        return colnamechoices

    def get_rowval_choices(self):
        try:
            colname = self.colNameComboBox.currentText()
            colname = (self.vars_level0[self.vars_level1.index(colname)], colname)
            choices = self.data[self.chooseDataComboBox.currentText()].df[colname]
            # choices = choices[~np.isnan(choices)]
            # nchoices2 = choices.size
            nchoice = []
            choices = [str(i) for i in choices]
            for choice in choices:
                if not choice + ' : ' + str(choices.count(choice)) in nchoice:
                    nchoice.append(choice + ' : ' + str(choices.count(choice)))
            choices = nchoice
        except:
            choices = ['-']
        return choices


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RemoveRows()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
