import pandas as pd
from PyQt5 import QtWidgets
from point_spectra_gui.util.spectral_data import spectral_data
from point_spectra_gui.ui.LoadData import Ui_loadData
from point_spectra_gui.util.Modules import Modules
import os.path

class LoadData(Ui_loadData, Modules):
    """
    Loads the data into the UI.
    The data needs to be a *.csv in order for this application to work
    """

    # def delete(self):
    #     Modules.data_count -= 1

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.newFilePushButton.clicked.connect(lambda: self.getDataButton_clicked(self.fileNameLineEdit))

    def getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", self.outpath, "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def run(self, filename = None, keyname = None):
        Modules.data_count += 1
        self.count = Modules.data_count
        if filename == None:
            filename = self.fileNameLineEdit.text()
        if keyname == None:
            keyname = self.dataSetNameLineEdit.text()

        #if the datakey exists, add a number to it to make it unique
        number = 1
        while keyname in self.datakeys:
            number += 1
            keyname = keyname + ' - ' + str(number)

        print('Loading data file: ' + str(filename))
        data = pd.read_csv(filename, header=[0, 1], verbose=False)

        #remove duplicate wvl values
        data_wvl = data['wvl']
        data_no_wvl = data.drop(columns='wvl')

        good_wvls = []
        for i in data_wvl.columns:
            try:
                i = float(i)
                good_wvls.append(True)
            except:
                print("Removing column "+str(i))
                good_wvls.append(False)

        data_wvl = data_wvl.iloc[:,good_wvls]
        data_wvl.columns = pd.MultiIndex.from_tuples([('wvl',float(i)) for i in data_wvl.columns])
        data = pd.merge(data_no_wvl,data_wvl,left_index=True,right_index=True)
        self.data[keyname] = spectral_data(data)
        self.list_amend(self.datakeys, self.count, keyname)
        self.datafiles[keyname] = os.path.basename(filename)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = LoadData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
