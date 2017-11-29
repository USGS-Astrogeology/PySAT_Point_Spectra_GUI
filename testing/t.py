import sys
import warnings

from point_spectra_gui import core

try:
    import qtmodern.styles

    q = True
except:
    q = False
    warnings.warn("You're missing the qtmodern package."
                  "to install it use pip install qtmodern")

from PyQt5 import QtWidgets

from point_spectra_gui.core.MainWindow import MainWindow


class Ui_MainWindow(MainWindow):
    def connectWidgets(self):
        """
        Connect all the widgets associated with the MainWindow UI
        :return:
        """
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
