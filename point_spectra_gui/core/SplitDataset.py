import numpy as np
from PyQt5 import QtWidgets
from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui.SplitDataset import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class SplitDataset(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        try:
            self.setComboBox(self.chooseDataComboBox, self.datakeys)
            self.setComboBox(self.splitOnUniqueValuesOfComboBox, self.get_choices())
        except:
            pass

    def function(self):
        datakey = self.chooseDataComboBox.currentText()
        colname = self.splitOnUniqueValuesOfComboBox.currentText()
        if (self.checkoptions(datakey, self.datakeys, 'data set') or
            self.checkoptions(colname,self.datakeys,'column')):
            self.connectWidgets()
        else:
            vars_level0 = self.data[datakey].df.columns.get_level_values(0)
            vars_level1 = self.data[datakey].df.columns.get_level_values(1)
            vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
            vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
            colname = (vars_level0[vars_level1.index(colname)], colname)

            coldata = np.array([str(i) for i in self.data[datakey].df[colname]])
            unique_values = np.unique(coldata)
            for i in unique_values:
                new_datakey = datakey + ' - ' + str(i)
                self.datakeys.append(new_datakey)
                self.data[new_datakey] = spectral_data(self.data[datakey].df.ix[coldata == i])

    def get_choices(self):
        try:
            self.vars_level0 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'wvl'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'wvl'])
            colnamechoices = self.vars_level1
            return colnamechoices
        except:
            try:
                colnamechoices = self.data[self.chooseDataComboBox.currentText()].columns.values
                colnamechoices = [i for i in colnamechoices if
                                  not 'Unnamed' in i]  # remove unnamed columns from choices
                return colnamechoices
            except:
                pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = SplitDataset()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
