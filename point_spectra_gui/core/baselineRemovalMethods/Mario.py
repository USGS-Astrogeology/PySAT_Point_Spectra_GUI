from PyQt5 import QtWidgets
from libpysat.spectral.baseline_code.mario import Mario

from point_spectra_gui.ui.Mario import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupbox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        br = Mario()
        # This algorithm doesn't work for now, but let the user get a sneak peek of it.
        self.get_widget().setDisabled(True)
        self.polynomialOrderSpinBox.setValue(br.poly_order_)
        self.toleranceDoubleSpinBox.setValue(br.tol_)

    def function(self):
        maxNIDSpinBox = self.maximumNumOfIterationsDoubleSpinBox.value()
        if maxNIDSpinBox == 0:
            maxNIDSpinBox = None
        methodParameters = {'poly_order_': self.polynomialOrderSpinBox.value(),
                            'max_iters_': maxNIDSpinBox,
                            'tol_': self.toleranceDoubleSpinBox.value()}
        return methodParameters, self.getChangedValues(methodParameters, Mario())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
