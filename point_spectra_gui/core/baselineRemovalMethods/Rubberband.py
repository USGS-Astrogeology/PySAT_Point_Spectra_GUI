from PyQt5 import QtWidgets
from pysat.spectral.baseline_code.rubberband import Rubberband

from point_spectra_gui.ui.Rubberband import Ui_Form
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
        br = Rubberband()
        self.windowSizeSpinBox.setValue(br.num_iters_)
        self.numOfRangesSpinBox.setValue(br.num_ranges_)


    def function(self):
        methodParameters = {'num_iters': int(self.windowSizeSpinBox.value()),
                            'num_ranges': int(self.numOfRangesSpinBox.value())}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
