from PyQt5 import QtWidgets

from point_spectra_gui.ui.RenameData import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class RenameData(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.renameDataComboBox, self.datakeys)

    def function(self):
        self.datakeys.append(self.toDataLineEdit.text())
        self.data[self.toDataLineEdit.text()] = self.data[self.renameDataComboBox.currentText()]
        for i in range(len(self.datakeys) - 1):
            if self.datakeys[i] == self.renameDataComboBox.currentText():
                del self.datakeys[i]


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RenameData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
