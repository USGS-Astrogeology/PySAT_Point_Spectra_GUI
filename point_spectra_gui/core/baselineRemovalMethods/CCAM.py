from PyQt5 import QtWidgets
from libpysat.spectral.baseline_code.ccam_remove_continuum import ccam_br

from point_spectra_gui.ui.CCAM import Ui_Form
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
        CCAM = ccam_br()
        self.lowestWaveletScaleSpinBox.setValue(CCAM.lvmin_)
        self.largestWaveletScaleSpinBox.setValue(CCAM.lv_)

    def function(self):
        methodParameters = {'lv_': self.largestWaveletScaleSpinBox.value(),
                            'lvmin_': self.lowestWaveletScaleSpinBox.value()}

        int_flag = self.interpolationMethodComboBox.currentText()
        if int_flag == 'Linear':
            methodParameters.update({'int_flag_': 0})
        elif int_flag == 'Quadratic':
            methodParameters.update({'int_flag_': 1})
        elif int_flag == 'Spline':
            methodParameters.update({'int_flag_': 2})

        return methodParameters


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
