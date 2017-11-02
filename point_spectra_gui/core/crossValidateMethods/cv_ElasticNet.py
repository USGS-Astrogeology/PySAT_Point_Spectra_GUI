from PyQt5 import QtWidgets,QtCore
from sklearn.linear_model import ElasticNet

from point_spectra_gui.ui.cv_ElasticNet import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, ElasticNet, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        en = ElasticNet()

        self.enalphaLineEdit.setText(str(en.alpha))
        self.enl1_ratioLineEdit.setText(str(en.l1_ratio))
        self.enfit_intercept_list.setCurrentItem(self.enfit_intercept_list.findItems(str(en.fit_intercept),QtCore.Qt.MatchExactly)[0])
        self.ennormalize_list.setCurrentItem(self.ennormalize_list.findItems(str(en.normalize),QtCore.Qt.MatchExactly)[0])
        #self.enprecomputeCheckBox.setChecked(en.precompute)
        self.enmax_iterLineEdit.setText(str(en.max_iter))
        #self.encopy_XCheckBox.setChecked(en.copy_X)
        self.entolLineEdit.setText(str(en.tol))
        self.enwarm_start_list.setCurrentItem(self.enwarm_start_list.findItems(str(en.warm_start),QtCore.Qt.MatchExactly)[0])
        self.enpositive_list.setCurrentItem(self.enpositive_list.findItems(str(en.positive),QtCore.Qt.MatchExactly)[0])
        #self.setComboBox(self.enselectionComboBox, ['cyclic', 'random'])
        #self.defaultComboItem(self.enselectionComboBox, en.selection)


    def function(self):
        fit_intercept_items = [i.text() == 'True' for i in self.enfit_intercept_list.selectedItems()]
        normalize_items = [i.text() == 'True' for i in self.ennormalize_list.selectedItems()]
        positive_items = [i.text() == 'True' for i in self.enpositive_list.selectedItems()]

        params = {
            'alpha': self.enalphaLineEdit.text().split(','),
            'l1_ratio': self.enl1_ratioLineEdit.text().split(','),
            'fit_intercept': fit_intercept_items,
            'normalize': normalize_items,
            'precompute': True,
            'max_iter': self.enmax_iterLineEdit.text().split(','),
            'copy_X': True,
            'tol': self.entolLineEdit.text().split(','),
            'warm_start': True,
            'positive': positive_items,
            'selection': 'random'}

        modelkey = str(params)
        return params, modelkey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
