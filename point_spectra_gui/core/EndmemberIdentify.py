from PyQt5 import QtWidgets

from point_spectra_gui.ui.EndmemberID import Ui_Form
from point_spectra_gui.util.Modules import Modules

class EndmemberIdentify(Ui_Form, Modules):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupLayout

    def connectWidgets(self, setup=False):
        self.algorithm_list = ['Choose an algorithm',
                               'PPI',
                               'N-FINDR',
                               'ATGP',
                               'FIPPI'
                               ]
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseAlgorithmComboBox, self.algorithm_list)
        self.changeComboListVars(self.xVariableList, self.xvar_choices())
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.xVariableList, self.xvar_choices()))

    def run(self):
        method = self.chooseAlgorithmComboBox.currentText()
        datakey = self.chooseDataComboBox.currentText()
        xvars = [str(x.text()) for x in self.xVariableList.selectedItems()]
        n_endmembers = self.n_endmembers_spinBox.value()
        self.data[datakey].endmember_identify(xvars, method, n_endmembers)

    def xvar_choices(self):
        try:
            xvarchoices = self.data[self.chooseDataComboBox.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = EndmemberIdentify()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())