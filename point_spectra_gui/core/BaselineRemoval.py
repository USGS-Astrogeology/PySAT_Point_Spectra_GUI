from PyQt5 import QtWidgets
from Qtickle import Qtickle
from libpysat.spectral.spectral_data import spectral_data
from point_spectra_gui.core.baselineRemovalMethods import *
from point_spectra_gui.ui.BaselineRemoval import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics



class BaselineRemoval(Ui_Form, Basics):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Basics.setupUi(self, Form)
        self.baselineMethods()

    def get_widget(self):
        return self.formGroupBox

    def make_regression_widget(self, alg, params=None):
        self.hideAll()
        print(alg)
        for i in range(len(self.chooseAlgorithmList)):
            if alg == self.chooseAlgorithmList[i] and i > 0:
                self.alg[i - 1].setHidden(False)

    def connectWidgets(self):
        self.chooseAlgorithmList = ['Choose an algorithm',
                                    'AirPLS',
                                    'ALS',
                                    'Dietrich',
                                    'FABC',
                                    'KK',
                                    'Median',
                                    'Polyfit',
                                    'Rubberband',
                                    'CCAM',
                                    'Mario (Coming soon)',
                                    ]
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseAlgorithmComboBox, self.chooseAlgorithmList)
        self.chooseAlgorithmComboBox.currentIndexChanged.connect(
            lambda: self.make_regression_widget(self.chooseAlgorithmComboBox.currentText()))

    def getGuiParams(self):
        """
        Overriding Basics' getGuiParams, because I'll need to do a list of lists
        in order to obtain the regressionMethods' parameters
        """
        self.qt = Qtickle.Qtickle(self)
        s = []
        s.append(self.qt.guiSave())
        for items in self.alg:
            s.append(items.getGuiParams())
        return s

    def setGuiParams(self, dict):
        self.qt = Qtickle.Qtickle(self)
        self.qt.guiRestore(dict[0])
        for i in range(len(dict)):
            self.alg[i - 1].setGuiParams(dict[i])

    def function(self):
        method = self.chooseAlgorithmComboBox.currentText()
        datakey = self.chooseDataComboBox.currentText()

        if self.checkoptions(datakey, self.datakeys,'data set'):
            self.connectWidgets()
        else:
            methodParameters = self.getMethodParams(self.chooseAlgorithmComboBox.currentIndex())

            datakey_new = datakey + '-Baseline Removed-' + method + str(methodParameters)
            datakey_baseline = datakey + '-Baseline-' + method + str(methodParameters)
            self.datakeys.append(datakey_new)
            self.datakeys.append(datakey_baseline)
            self.data[datakey_new] = spectral_data(self.data[datakey].df.copy(deep=True))
            self.data[datakey_new].remove_baseline(method, segment=True, params=methodParameters)
            self.data[datakey_baseline] = spectral_data(self.data[datakey_new].df_baseline)

    def hideAll(self):
        for a in self.alg:
            a.setHidden(True)

    def getMethodParams(self, index):
        return self.alg[index - 1].function()

    def baselineMethods(self):
        self.alg = []
        list_forms = [
            AirPLS,
            ALS,
            Dietrich,
            FABC,
            KK,
            Median,
            Polyfit,
            Rubberband,
            CCAM,
            Mario,
        ]
        for items in list_forms:
            self.alg.append(items.Ui_Form())
            self.alg[-1].setupUi(self.Form)
            self.algorithmLayout.addWidget(self.alg[-1].get_widget())
            self.alg[-1].setHidden(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = BaselineRemoval()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
