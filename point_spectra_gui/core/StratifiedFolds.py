from PyQt5 import QtWidgets

from point_spectra_gui.ui.StratifiedFolds import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class StratifiedFolds(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.nFoldsSpinBox.setValue(2)
        self.testFoldsSpinBox.setValue(2)
        self.setComboBox(self.chooseDataToStratifyComboBox, self.datakeys)
        try:  # Some instances where perhaps there is no data to load
            data = self.data[self.chooseDataToStratifyComboBox.currentText()].df['comp'].columns.values
            self.setComboBox(self.chooseVarComboBox, data)
        except:
            pass
        self.chooseDataToStratifyComboBox.activated[int].connect(self.strat_fold_change_vars)
        self.nFoldsSpinBox.valueChanged.connect(self.strat_fold_change_testfolds)

    def function(self):
        datakey = self.chooseDataToStratifyComboBox.currentText()
        nfolds = self.nFoldsSpinBox.value()
        try:
            testfold = int(self.testFoldsSpinBox.value())
        except:
            testfold = 1
        colname = ('comp', self.chooseVarComboBox.currentText())
        self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        self.data[datakey + '-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey + '-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys.append(datakey + '-Train')
        self.datakeys.append(datakey + '-Test')

        print(self.data.keys())
        print(self.data[datakey + '-Test'].df.index.shape)
        print(self.data[datakey + '-Train'].df.index.shape)

    def strat_fold_change_vars(self):
        self.chooseVarComboBox.clear()
        try:
            choices = self.data[self.chooseDataToStratifyComboBox.currentText()].df['comp'].columns.values
        except:
            choices = ['No composition columns!']

        self.chooseVarComboBox.addItems(choices)

    def strat_fold_change_testfolds(self):
        self.testFoldsSpinBox.clear()
        self.testFoldsSpinBox.setMaximum(self.nFoldsSpinBox.value())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = StratifiedFolds()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
