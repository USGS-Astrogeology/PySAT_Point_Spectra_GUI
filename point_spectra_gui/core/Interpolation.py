from PyQt5 import QtWidgets

from point_spectra_gui.ui.Interpolation import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Interpolation(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.interpolateDataComboBox, self.datakeys)
        self.setComboBox(self.referenceDataComboBox, self.datakeys)

    def function(self):
        datakey_to_interp = self.interpolateDataComboBox.currentText()
        datakey_ref = self.referenceDataComboBox.currentText()
        print(self.data[datakey_ref].df.columns.levels[0])
        try:
            self.data[datakey_to_interp].interp(self.data[datakey_ref].df['wvl'].columns)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Interpolation()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
