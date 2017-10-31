import pandas as pd
from PyQt5 import QtWidgets
from libpysat.fileio import io_ccam_pds
from libpysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui.ReadChemCamData import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class ReadChemCamData(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.searchStringLineEdit.setText("*ccs*.csv")
        self.searchDirectorypushButton.clicked.connect(self.on_searchpathButton_clicked)
        self.metadatapushButton.clicked.connect(self.on_metadataButton_clicked)

    def on_searchpathButton_clicked(self):
        dirname = QtWidgets.QFileDialog.getExistingDirectory(parent=None, caption="Select Search Directory",
                                                             directory='.')
        self.searchDirectoryLineEdit.setText(dirname)
        if self.searchDirectoryLineEdit.text() == "":
            self.searchDirectoryLineEdit.setText("*/")

    def on_metadataButton_clicked(self):
        self.metadata_file, null = QtWidgets.QFileDialog.getOpenFileNames(parent=None,
                                                                          caption="Select metadata file(s)",
                                                                          directory='.')
        self.metadataFilesLineEdit.setText(str(self.metadata_file))
        if self.metadataFilesLineEdit.text() == "":
            self.metadataFilesLineEdit.setText("*/")

    def function(self):
        params = self.getGuiParams()
        searchdir = params['searchDirectoryLineEdit']
        searchstring = params['searchStringLineEdit']
        to_csv = params['outputFileNameLineEdit']
        try:
            lookupfile = params['metadataFilesLineEdit']
        except:
            lookupfile = None
        ave = bool(params['averagesradioButton'])
        progressbar = QtWidgets.QProgressDialog()
        io_ccam_pds.ccam_batch(searchdir, searchstring=searchstring, to_csv=Basics.outpath + '/' + to_csv,
                               lookupfile=lookupfile, ave=ave, progressbar=progressbar)
        self.do_get_data(Basics.outpath + '/' + to_csv, 'ChemCam')

    def do_get_data(self, filename, keyname):
        try:
            print('Loading data file: ' + str(filename))
            self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1]))
            self.datakeys.append(keyname)
            pass
        except Exception as e:
            print('Problem reading data: {}'.format(e))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    
    Form = QtWidgets.QWidget()
    ui = ReadChemCamData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
