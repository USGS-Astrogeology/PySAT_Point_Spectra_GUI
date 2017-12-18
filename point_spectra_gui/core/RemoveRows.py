import numpy as np
from PyQt5 import QtWidgets
from libpysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui.RemoveRows import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics

class remove_operation:
    def __init__(self, colname, operator, value, logic = None, hidden = None):
        self.colname = colname
        self.operator = operator
        self.value = value
        self.logic = logic
        self.hidden = hidden
        if hidden is not None:
            self.hidden.setHidden(True)
            self.hidden.stateChanged.connect(self.Hidden)

    def Hidden(self):
        if self.hidden.isChecked():
            self.colname.setHidden(True)
            self.operator.setHidden(True)
            self.value.setHidden(True)
            try:
                self.logic.setHidden(True)
            except:
                pass

        else:
            self.colname.setHidden(False)
            self.operator.setHidden(False)
            self.value.setHidden(False)
            try:
                self.logic.setHidden(False)
            except:
                pass

    def GetValues(self):
        try:
            return {'column':self.colname.currentText(), 'operator':self.operator.currentText(),
                    'value':self.value.currentText().split(' : ')[0], 'logic':self.logic.currentText()}
        except:
            return {'column': self.colname.currentText(), 'operator': self.operator.currentText(),
                    'value': self.value.currentText().split(' : ')[0]}


class RemoveRows(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.setup_remove_operations()
        Basics.setupUi(self, Form)

    def setup_remove_operations(self):
        self.operations = [remove_operation(self.colName_1, self.operator_1, self.value_1, logic = self.logic_1),
                           remove_operation(self.colName_2, self.operator_2, self.value_2, logic=self.logic_2, hidden=self.hidden_2),
                           remove_operation(self.colName_3, self.operator_3, self.value_3, logic=self.logic_3, hidden=self.hidden_3),
                           remove_operation(self.colName_4, self.operator_4, self.value_4, logic=self.logic_4, hidden=self.hidden_4),
                           remove_operation(self.colName_5, self.operator_5, self.value_5, hidden=self.hidden_5)]
        for i in self.operations:
            try:
                i.hidden.setChecked(True)
            except:
                pass
            i.colname.currentIndexChanged.connect(lambda: self.update_vals())


    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseData, self.datakeys)
        self.chooseData.currentIndexChanged.connect(lambda: self.update_cols())
        self.update_cols()
        self.connect_logic()


    def update_cols(self):
        for i in self.operations:
            self.setComboBox(i.colname, self.get_colname_choices())
            self.update_vals()

    def update_vals(self):
        for i in self.operations:
            self.setComboBox(i.value, self.get_rowval_choices(i.colname.currentText()))

    def connect_logic(self):
        for i in self.operations:
            try:
                i.logic.currentIndexChanged.connect(lambda: self.hide_operations())
            except:
                pass


    def hide_operations(self):
        for i in range(len(self.operations)-1):
            try:
                if self.operations[i].logic.currentText() == 'and':
                    self.operations[i+1].hidden.setChecked(False)
                else:
                    self.operations[i+1].hidden.setChecked(True)

                if self.operations[i+1].logic.currentText() == 'and':
                    self.operations[i].logic.setEnabled(False)
                else:
                    self.operations[i].logic.setEnabled(True)

            except:
                pass
    def function(self):
        match_vectors = []
        logic_list = []
        datakey = self.chooseData.currentText()
        for i in self.operations:
            values_tmp = i.GetValues()
            if i.hidden == None:
                match_vectors.append(self.evaluate_operation(datakey, values_tmp))
                logic_list.append(values_tmp['logic'])
            else:
                if i.hidden.isChecked() == False:
                    match_vectors.append(self.evaluate_operation(datakey, values_tmp))
                    logic_list.append(values_tmp['logic'])


        match_combined = np.all(match_vectors, axis=0)
        print(self.data[datakey].df.shape)
        self.data[datakey] = spectral_data(self.data[datakey].df.ix[~match_combined])

        print(self.data[datakey].df.shape)

        pass




    def evaluate_operation(self, datakey, operation_values):
        colname = operation_values['column']
        value = operation_values['value']
        operator = operation_values['operator']

        vars_level0 = self.data[datakey].df.columns.get_level_values(0)
        vars_level1 = self.data[datakey].df.columns.get_level_values(1)
        vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
        vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
        colname = (vars_level0[vars_level1.index(colname)], colname)
        coldata = np.array([str(i) for i in self.data[datakey].df[colname]])\

        #
        # if value == 'Null':
        #     self.data[datakey] = spectral_data(self.data[datakey].df.ix[-self.data[datakey].df[colname].isnull()])
        # else:
        #     # find where the values in the specified column match the value to be removed

        if operator == '=':
            match = coldata == value
        if operator == '>':
            match = coldata > value
        if operator == '<':
            match = coldata < value
        if operator == '<=':
            match = coldata <= value
        if operator == '>=':
            match = coldata >= value

        return match
        #     # keep everything except where match is true
        #     self.data[datakey] = spectral_data(self.data[datakey].df.ix[~match])
        # print(self.data[datakey].df.shape)

    def get_colname_choices(self):
        try:
            self.vars_level0 = self.data[self.chooseData.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.data[self.chooseData.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = list(
                self.vars_level1[np.logical_and(self.vars_level0 != 'wvl', self.vars_level0 != 'masked')])
            self.vars_level0 = list(
                self.vars_level0[np.logical_and(self.vars_level0 != 'wvl', self.vars_level0 != 'masked')])

            colnamechoices = self.vars_level1

        except:
            try:
                colnamechoices = self.data[self.chooseData.currentText()].columns.values
            except:
                colnamechoices = []
        colnamechoices = [i for i in colnamechoices if not 'Unnamed' in str(i)]  # remove unnamed columns from choices
        return colnamechoices

    def get_rowval_choices(self, colname):
        try:
            colname = (self.vars_level0[self.vars_level1.index(colname)], colname)
            choices = self.data[self.chooseData.currentText()].df[colname]
            # choices = choices[~np.isnan(choices)]
            # nchoices2 = choices.size
            nchoice = []
            choices = np.sort(choices)
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
