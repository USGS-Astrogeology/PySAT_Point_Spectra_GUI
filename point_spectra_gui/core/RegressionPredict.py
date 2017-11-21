from PyQt5 import QtWidgets

from point_spectra_gui.ui.RegressionPredict import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class RegressionPredict(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseModelComboBox, self.modelkeys)

    def function(self):
        datakey = self.chooseDataComboBox.currentText()
        modelkey = self.chooseModelComboBox.currentText()
        if (self.checkoptions(datakey, self.datakeys, 'data set') or
            self.checkoptions(modelkey, self.modelkeys, 'model')):
            self.connectWidgets()
        else:
            predictname = ('predict', modelkey + ' - ' + datakey + ' - Predict')
            prediction = self.models[modelkey].predict(self.data[datakey].df[self.model_xvars[modelkey]])
            self.data[datakey].df[predictname] = prediction

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RegressionPredict()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
