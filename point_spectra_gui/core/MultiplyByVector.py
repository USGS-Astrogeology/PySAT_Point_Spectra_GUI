from PyQt5 import QtWidgets

from point_spectra_gui.ui.MultiplyByVector import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class MultiplyByVector(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.vectorFileLineEdit))

    def function(self):
        datakey = self.chooseDataComboBox.currentText()

        if self.checkoptions(datakey, self.datakeys, 'data set'):
            self.connectWidgets()
        else:
            vectorfile = self.vectorFileLineEdit.text()

            try:
                self.data[datakey].multiply_vector(vectorfile)
            except Exception as e:
                print(e)

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Vector Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = MultiplyByVector()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
