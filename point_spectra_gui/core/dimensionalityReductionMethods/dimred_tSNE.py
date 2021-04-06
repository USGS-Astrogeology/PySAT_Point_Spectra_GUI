from PyQt5 import QtWidgets
from sklearn.manifold import TSNE
from point_spectra_gui.ui.dimred_tSNE import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, TSNE, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.nc_spin.setValue(self.n_components)
        self.learning_spin.setValue(self.learning_rate)
        self.n_iter_spin.setValue(self.n_iter)
        self.no_progress_spin.setValue(300)
        self.perplexity_spin.setValue(50)

    def run(self):
        params = {
            'n_components': self.nc_spin.value(),
            'learning_rate': self.learning_spin.value(),
            'n_iter': self.n_iter_spin.value(),
            'n_iter_without_progress': self.no_progress_spin.value(),
            'perplexity': self.perplexity_spin.value(),
            'init': 'pca'
        }

        params_key = str(params)
        return params, params_key


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
