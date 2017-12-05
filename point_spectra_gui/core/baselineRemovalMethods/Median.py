from PyQt5 import QtWidgets
from libpysat.spectral.baseline_code.median import MedianFilter

from point_spectra_gui.ui.Median import Ui_Form
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
        br = MedianFilter()
        self.windowSizeSpinBox.setValue(br.window_)

    def function(self):
        methodParameters = {'window_': self.windowSizeSpinBox.value()}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
