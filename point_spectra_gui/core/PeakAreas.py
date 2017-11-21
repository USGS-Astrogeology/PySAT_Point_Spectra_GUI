import numpy as np
from PyQt5 import QtWidgets

from point_spectra_gui.ui.PeakAreas import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class PeakAreas(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.peakMinimaLineEdit.setText("None (calculate from average spectrum)")
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.peakMinimaLineEdit))

    def function(self):
        datakey = self.chooseDataComboBox.currentText()
        if self.checkoptions(datakey, self.datakeys, 'data set'):
            self.connectWidgets()
        else:

            peaks_mins_file = self.peakMinimaLineEdit.text()
            if peaks_mins_file == "None (calculate from average spectrum)":
                peaks_mins_file = None

            try:
                peaks, mins = self.data[datakey].peak_area(peaks_mins_file=peaks_mins_file)
                print("Peak Areas Calculated")

                np.savetxt(self.outpath + '/peaks.csv', peaks, delimiter=',')
                np.savetxt(self.outpath + '/mins.csv', mins, delimiter=',')

            except Exception as e:
                print(e)

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open peaks and minima File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("None (calculate from average spectrum)")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = PeakAreas()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
