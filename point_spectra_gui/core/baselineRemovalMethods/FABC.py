from PyQt5 import QtWidgets
from libpysat.spectral.baseline_code.fabc import FABC

from point_spectra_gui.ui.FABC import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupbox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        br = FABC()
        self.smoothnessDoubleSpinBox.setValue(br.dilation_)
        self.dilationSpinBox.setValue(br.smoothness_)

    def function(self):
        methodParameters = {'dilation_': float(self.smoothnessDoubleSpinBox.value()),
                            'smoothness_': int(self.dilationSpinBox.value())}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
