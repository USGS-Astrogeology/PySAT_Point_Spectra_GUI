from PyQt5 import QtWidgets

from point_spectra_gui.ui.DimensionalityReduction import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class DimensionalityReduction(Ui_Form, Basics):
    _methods = [
        'PCA',
        'FastICA'#,
        #'ICA-JADE',
    ]

    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseMethodComboBox, ['Choose a method'] + self._methods)
        self.chooseMethodComboBox.currentIndexChanged.connect(
            lambda: self.method_ComboBox_IndexChanged(self.chooseMethodComboBox.currentText()))

    def function(self):
        col = 'wvl'
        self.dim_reds = {}
        self.dim_red_keys = []
        load_fit = None
        dim_red_key = None
        datakey = self.chooseDataComboBox.currentText()
        method = self.chooseMethodComboBox.currentText()
        params = []
        method_kws = {}
        try:
            if method == 'PCA':
                method_kws = {'n_components': self.dim_red_widget.pca_nc_spinbox.value()}

            if method == 'FastICA':
                method_kws = {'n_components': self.dim_red_widget.ica_nc_spinbox.value()}

            if method == 'ICA-JADE':
                method_kws = {'n_components': self.dim_red_widget.ica_jade_nc_spinbox.value()}

        except Exception as e:
            print(e)

        try:
            if method == 'PCA' or method == 'FastICA':
                self.dim_reds[dim_red_key] = self.data[datakey].dim_red(
                    col, method, params, method_kws, load_fit=load_fit)
            elif method == 'ICA-JADE':
                self.dim_reds[dim_red_key] = self.data[datakey].ica_jade(col)
            self.dim_red_keys.append(dim_red_key)

        except Exception as e:
            print(e)

    def method_ComboBox_IndexChanged(self, method):
        print(method)
        try:
            self.dim_red_widget.deleteLater()
        except:
            pass
        self.dim_red_widget = QtWidgets.QWidget()
        if method == 'PCA':
            self.dim_red_widget.pca_hlayout = QtWidgets.QHBoxLayout(self.dim_red_widget)
            self.dim_red_widget.pca_nc_label = QtWidgets.QLabel(self.dim_red_widget)
            self.dim_red_widget.pca_nc_label.setText('# of components:')
            self.dim_red_widget.pca_nc_label.setObjectName("self.pca_nc_label")
            self.dim_red_widget.pca_hlayout.addWidget(self.dim_red_widget.pca_nc_label)
            self.dim_red_widget.pca_nc_spinbox = QtWidgets.QSpinBox(self.dim_red_widget)

            self.dim_red_widget.pca_nc_spinbox.setObjectName("self.pca_nc_spinbox")
            self.dim_red_widget.pca_hlayout.addWidget(self.dim_red_widget.pca_nc_spinbox)
            self.dim_red_widget.pca_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                   QtWidgets.QSizePolicy.Minimum)
            self.dim_red_widget.pca_hlayout.addItem(self.dim_red_widget.pca_spacer)
            self.dim_red_widget.pca_nc_spinbox.setValue(2)

        if method == 'FastICA':
            self.dim_red_widget.ica_hlayout = QtWidgets.QHBoxLayout(self.dim_red_widget)
            self.dim_red_widget.ica_nc_label = QtWidgets.QLabel(self.dim_red_widget)
            self.dim_red_widget.ica_nc_label.setText('# of components:')
            self.dim_red_widget.ica_nc_label.setObjectName("self.ica_nc_label")
            self.dim_red_widget.ica_hlayout.addWidget(self.dim_red_widget.ica_nc_label)
            self.dim_red_widget.ica_nc_spinbox = QtWidgets.QSpinBox(self.dim_red_widget)
            self.dim_red_widget.ica_nc_spinbox.setObjectName("self.ica_nc_spinbox")
            self.dim_red_widget.ica_hlayout.addWidget(self.dim_red_widget.ica_nc_spinbox)
            self.dim_red_widget.ica_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                   QtWidgets.QSizePolicy.Minimum)
            self.dim_red_widget.ica_hlayout.addItem(self.dim_red_widget.ica_spacer)
            self.dim_red_widget.ica_nc_spinbox.setValue(2)

        if method == 'ICA-JADE':
            self.dim_red_widget.ica_jade_hlayout = QtWidgets.QHBoxLayout(self.dim_red_widget)
            self.dim_red_widget.ica_jade_nc_label = QtWidgets.QLabel(self.dim_red_widget)
            self.dim_red_widget.ica_jade_nc_label.setText('# of components:')
            self.dim_red_widget.ica_jade_nc_label.setObjectName("self.ica_jade_nc_label")
            self.dim_red_widget.ica_jade_hlayout.addWidget(self.dim_red_widget.ica_jade_nc_label)
            self.dim_red_widget.ica_jade_nc_spinbox = QtWidgets.QSpinBox(self.dim_red_widget)
            self.dim_red_widget.ica_jade_nc_spinbox.setObjectName("self.ica_jade_nc_spinbox")
            self.dim_red_widget.ica_jade_hlayout.addWidget(self.dim_red_widget.ica_jade_nc_spinbox)
            self.dim_red_widget.ica_jade_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                        QtWidgets.QSizePolicy.Minimum)
            self.dim_red_widget.ica_jade_hlayout.addItem(self.dim_red_widget.ica_jade_spacer)
            self.dim_red_widget.ica_jade_nc_spinbox.setValue(2)

            self.dim_red_widget.setObjectName("dim_red_widget")
        self.dim_reduction_vlayout.addWidget(self.dim_red_widget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = DimensionalityReduction()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
