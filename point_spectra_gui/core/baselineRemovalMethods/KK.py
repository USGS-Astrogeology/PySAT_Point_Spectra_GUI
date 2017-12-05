from PyQt5 import QtWidgets
from libpysat.spectral.baseline_code.kajfosz_kwiatek import KajfoszKwiatek as KK

from point_spectra_gui.ui.KK import Ui_Form
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
        br = KK()
        self.topWidthSpinBox.setValue(br.top_width_)
        self.bottomWidthSpinBox.setValue(br.bottom_width_)
        self.tangentCheckBox.setChecked(br.tangent_)
        self.exponentSpinBox.setValue(br.exponent_)

    def function(self):
        methodParameters = {'top_width_': self.topWidthSpinBox.value(),
                            'bottom_width_': self.bottomWidthSpinBox.value(),
                            'tangent_': self.tangentCheckBox.isChecked(),
                            'exponent_': self.exponentSpinBox.value()}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
