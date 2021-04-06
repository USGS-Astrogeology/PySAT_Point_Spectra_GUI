from PyQt5 import QtWidgets
from sklearn.decomposition import PCA
from point_spectra_gui.ui.cluster_Spectral import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, PCA, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.n_clust_spin.setValue(8)
        self.n_runs_spin.setValue(10)
        self.gamma_dspin.setValue(1.0)
        self.n_neighbors_spin.setValue(10)
        self.coef0_spin.setValue(1)
        self.hide_for_kernel(self.affinity_comboBox.currentText())
        self.affinity_comboBox.currentIndexChanged.connect(
            lambda: self.hide_for_kernel(self.affinity_comboBox.currentText()))

    def hide_options(self, hide_list):
        self.gamma_dspin.setHidden(hide_list['gamma'])
        self.gamma_label.setHidden(hide_list['gamma'])
        self.n_neighbors_spin.setHidden(hide_list['n_neighbors'])
        self.n_neighbors_label.setHidden(hide_list['n_neighbors'])
        self.coef0_spin.setHidden(hide_list['coef0'])
        self.coef0_label.setHidden(hide_list['coef0'])
        self.degree_label.setHidden(hide_list['degree'])
        self.degree_spin.setHidden(hide_list['degree'])

    def hide_for_kernel(self, kernel):
        hide_list = {'gamma': True, 'n_neighbors': True, 'coef0': True, 'degree': True}
        if kernel == 'Radial Basis Function':
            hide_list['gamma'] = False
        if kernel == 'Nearest Neighbors':
            hide_list['n_neighbors'] = False
        if kernel == 'Sigmoid':
            hide_list['coef0'] = False
            hide_list['gamma'] = False
        if kernel == 'Polynomial':
            hide_list['degree'] = False
            hide_list['coef0'] = False
        self.hide_options(hide_list)

    def run(self):
        affinity = self.affinity_comboBox.currentText()
        if affinity == 'Radial Basis Function':
            kernel = 'rbf'
        if affinity == 'Nearest Neighbors':
            kernel = 'nearest_neighbors'
        if affinity == 'Sigmoid':
            kernel = 'sigmoid'
        if affinity == 'Polynomial':
            kernel = 'polynomial'
        if affinity == 'Linear':
            kernel = 'linear'
        if affinity == 'Cosine':
            kernel = 'cosine'

        params = {
            'n_clusters': self.n_clust_spin.value(),
            'n_init': self.n_runs_spin.value(),
            'affinity': kernel,
            'gamma': self.gamma_dspin.value(),
            'n_neighbors': self.n_neighbors_spin.value(),
            'degree': self.degree_spin.value(),
            'coef0': self.coef0_spin.value(),
            'n_jobs': -2} #use all but one cpu in parallel
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
