import os.path
import sys
import time
import warnings

from point_spectra_gui import core

try:
    import qtmodern.styles

    q = True
except:
    q = False
    warnings.warn("You're missing the qtmodern package."
                  "to install it use pip install qtmodern")

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSettings

from point_spectra_gui.core.MainWindow import Ui_MainWindow


class Ui_MainWindow(Ui_MainWindow):
    def connectWidgets(self):
        """
        Connect all the widgets associated with the MainWindow UI
        :return:
        """
        # TODO figure out how to get this code into `MainWindow.py`
        self.addWidget(core.ReadChemCamData.ReadChemCamData)
        self.addWidget(core.BaselineRemoval.BaselineRemoval)
        self.addWidget(core.CrossValidation.CrossValidation)
        self.addWidget(core.DimensionalityReduction.DimensionalityReduction)
        self.addWidget(core.Interpolation.Interpolation)
        self.addWidget(core.LoadData.LoadData)
        self.addWidget(core.WriteToCSV.WriteToCSV)
        self.addWidget(core.RenameData.RenameData)
        self.addWidget(core.MaskData.MaskData)
        self.addWidget(core.MultiplyByVector.MultiplyByVector)
        self.addWidget(core.Normalization.Normalization)
        self.addWidget(core.OutputFolder.OutputFolder)
        self.addWidget(core.PeakAreas.PeakAreas)
        self.addWidget(core.Plot.Plot)
        self.addWidget(core.Plot_ICA_PCA.Plot_ICA_PCA)
        self.addWidget(core.PlotSpectra.PlotSpectra)
        self.addWidget(core.RegressionTrain.RegressionTrain)
        self.addWidget(core.RegressionPredict.RegressionPredict)
        self.addWidget(core.RemoveRows.RemoveRows)
        self.addWidget(core.SplitDataset.SplitDataset)
        self.addWidget(core.StratifiedFolds.StratifiedFolds)
        self.addWidget(core.SubmodelPredict.SubmodelPredict)


def get_splash(app):
    """
    Get the splash screen for the application
    But check to see if the image even exists
    :param app:
    :return:
    """
    dirs = ['../images/', '/point_spectra_gui/images', './point_spectra_gui/images']
    for dir in dirs:
        if os.path.exists(dir + 'splash.png'):
            splash_pix = QPixmap(dir + 'splash.png')  # default
            app_icon = QtGui.QIcon(dir + 'icon.png')
            app.setWindowIcon(app_icon)
            splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
            splash.setMask(splash_pix.mask())
            splash.show()
            time.sleep(0.5)
            app.processEvents()
            return 0


def setDarkmode(app):
    settings = QSettings('USGS', 'PPSG')
    p = settings.value('theme') == 'qtmodern'
    if q and p:
        qtmodern.styles.dark(app)


def main():
    app = QtWidgets.QApplication(sys.argv)
    get_splash(app)
    setDarkmode(app)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
