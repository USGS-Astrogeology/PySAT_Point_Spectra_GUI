from PyQt5 import QtWidgets
from pysat.spectral.baseline_code.polyfit import PolyFit

from point_spectra_gui.ui.Polyfit import Ui_Form
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
        br = PolyFit()
        self.orderSpinBox.setValue(br.poly_order_)
        self.numOfStandardDeviationsSpinBox.setValue(br.stdv_)

    def function(self):
        methodParameters = {'poly_order_': int(self.orderSpinBox.value()),
                            'stdv_': int(self.numOfStandardDeviationsSpinBox.value()),
                            'max_iter_': int(self.maxNumOfIterationsSpinBox.value())}
        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
