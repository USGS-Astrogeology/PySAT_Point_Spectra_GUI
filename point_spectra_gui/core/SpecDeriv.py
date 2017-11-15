from PyQt5 import QtWidgets

from point_spectra_gui.ui.SpecDeriv import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class SpecDeriv(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataToDerivComboBox, self.datakeys)

    def function(self):
        datakey = self.chooseDataToDerivComboBox.currentText()
        if self.checkoptions(datakey, self.datakeys, 'data set'):
            self.connectWidgets()
        else:
            new_datakey = datakey + ' - Derivative'
            self.datakeys.append(new_datakey)
            self.data[new_datakey]=self.data[datakey].deriv()
            print("Derivative Applied")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = SpecDeriv()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
