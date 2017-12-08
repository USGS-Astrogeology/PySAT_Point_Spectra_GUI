from PyQt5 import QtWidgets
from sklearn.linear_model.base import LinearRegression

from point_spectra_gui.ui.OLS import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, LinearRegression, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.fitInterceptCheckBox.setChecked(self.fit_intercept)

    def function(self):
        params = {'fit_intercept': self.fitInterceptCheckBox.isChecked()}
        return params, self.getChangedValues(params, LinearRegression())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
