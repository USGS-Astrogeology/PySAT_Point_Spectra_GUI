from PyQt5 import QtWidgets

from point_spectra_gui.ui.Dietrich import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics
from libpysat.spectral.baseline_code.dietrich import Dietrich

class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupbox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        br = Dietrich()
        self.halfWindowSpinBox.setValue(br.half_window_)
        self.numOfErosionsSpinBox.setValue(br.num_erosions_)

    def function(self):
        methodParameters = {'half_window_': self.halfWindowSpinBox.value(),
                            'num_erosions_': self.numOfErosionsSpinBox.value()}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
