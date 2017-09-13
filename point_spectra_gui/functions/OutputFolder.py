from PyQt5 import QtWidgets

from point_spectra_gui.ui.OutputFolder import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def on_outPutLocationButton_clicked(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
        self.folderNameLineEdit.setText(filename)
        if self.folderNameLineEdit.text() == "":
            self.folderNameLineEdit.setText("*/")

    def connectWidgets(self):
        pass

        self.pushButton.clicked.connect(lambda: self.on_outPutLocationButton_clicked())

    def function(self):
        params = self.getGuiParams()
        outpath = params['folderNameLineEdit']
        try:
            Basics.outpath = outpath
            print("Output path folder has been set to " + outpath)
        except Exception as e:
            print("Error: {}; using default outpath: {}".format(e, Basics.outpath))

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # noinspection PyArgumentList
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
