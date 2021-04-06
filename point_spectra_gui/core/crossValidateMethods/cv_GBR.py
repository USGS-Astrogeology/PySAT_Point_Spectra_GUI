from PyQt5 import QtWidgets, QtCore
from sklearn.ensemble import GradientBoostingRegressor

from point_spectra_gui.ui.cv_GBR import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, GradientBoostingRegressor, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        pass

    def run(self):
        loss_lookup ={'Least Squares':'ls', 'Least Absolute Deviation':'lad', 'Huber':'huber', 'Quantile':'quantile'}
        loss_funcs = [loss_lookup[i.text()] for i in self.lossfunclistWidget.selectedItems()]

        params = {
                    'loss': loss_funcs,
                    'learning_rate': [float(i) for i in self.learninglineEdit.text().split(',')],
                    'n_estimators': [int(i) for i in self.numEstlineEdit.text().split(',')],
                    'subsample': [float(i) for i in self.subsamplelineEdit.text().split(',')],
                    'min_samples_split': [int(i) for i in self.min_n_splitlineEdit.text().split(',')],
                    'min_samples_leaf': [int(i) for i in self.min_n_leaflineEdit.text().split(',')],
                    'max_depth': [int(i) for i in self.maxdepthlineEdit.text().split(',')],
                    'min_impurity_decrease': [float(i) for i in self.min_impuritylineEdit.text().split(',')],
                    'random_state': [0],
                    'alpha': [float(i) for i in self.AlphalineEdit.text().split(',')]}
        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
