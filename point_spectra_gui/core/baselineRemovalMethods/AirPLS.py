from PyQt5 import QtWidgets
from libpysat.spectral.baseline_code.airpls import AirPLS

from point_spectra_gui.ui.AirPLS import Ui_Form
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
        airPLS = AirPLS()
        self.smoothnessSpinBox.setValue(airPLS.smoothness_)
        self.convergenceThresholdDoubleSpinBox.setValue(airPLS.conv_thresh_)
        self.maxNumOfIterationsSpinBox.setValue(airPLS.max_iters_)

    def function(self):
        methodParameters = {'smoothness_': float(self.smoothnessSpinBox.value()),
                            'conv_thresh_': int(self.convergenceThresholdDoubleSpinBox.value()),
                            'max_iters_': float(self.maxNumOfIterationsSpinBox.value())}

        return methodParameters, self.getChangedValues(methodParameters, AirPLS())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
