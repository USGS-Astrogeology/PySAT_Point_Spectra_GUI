import numpy as np
from PyQt5 import QtWidgets, QtCore
from point_spectra_gui.ui.cv_Local import Ui_Form
from point_spectra_gui.util.Modules import Modules

class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.n_neighbors_lineEdit.setText('250')
        self.fit_intercept_list.setCurrentItem(
            self.fit_intercept_list.findItems('True', QtCore.Qt.MatchExactly)[0])
        self.forcePositive_list.setCurrentItem(
            self.forcePositive_list.findItems('False', QtCore.Qt.MatchExactly)[0])

    def run(self):
        method = self.choose_alg_comboBox.currentText()
        fit_intercept_items = [i.text() == 'True' for i in self.fit_intercept_list.selectedItems()]
        positive_items = [i.text() == 'True' for i in self.forcePositive_list.selectedItems()]
        n_neighbors = [int(i) for i in self.n_neighbors_lineEdit.text().split(',')]


        if method== 'Elastic Net':
            params = {'n_neighbors':n_neighbors,
                      'fit_intercept': fit_intercept_items,
                      'max_iter': 10000,
                      'positive': positive_items,
                      'selection': 'random',
                      'l1_ratio': [.1, .5, .7, .9, .95, .99, 1]}
        else:
            params = {}

        # keyparams = {}
        # keyparams['method'] = 'Local '+method
        # keyparams['n_neighbors'] = n_neighbors
        #
        # modelkey = str(keyparams)
        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
