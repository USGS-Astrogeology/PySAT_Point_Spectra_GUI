from PyQt5 import QtWidgets

from point_spectra_gui.ui.MaskData import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class MaskData(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.maskFileLineEdit))

    def function(self):
        datakey = self.chooseDataComboBox.currentText()
        if self.checkoptions(datakey, self.datakeys, 'data set'):
            self.connectWidgets()
        else:
            maskfile = self.maskFileLineEdit.text()
            self.data[datakey].mask(maskfile, maskvar='wvl')
            print("Mask applied")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = MaskData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
