from PyQt5 import QtWidgets
from libpysat.plotting.plots import pca_ica_plot

from point_spectra_gui.ui.Plot_ICA_PCA import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Plot_ICA_PCA(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        alg_choices = ['Choose a method', 'PCA', 'FastICA', 'JADE-ICA']
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.chooseMethodComboBox, alg_choices)
        self.colorchoices_change_vars(self.colorCodedVariableComboBox)
        self.pushButton.clicked.connect(self.on_plotFilenamePushButton_clicked)
        self.chooseMethodComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.chooseXVariableComboBox, self.xychoices()))
        self.chooseMethodComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.chooseYVariableComboBox, self.xychoices()))

    def function(self):
        cmap = 'viridis'
        datakey = self.chooseDataComboBox.currentText()
        method = self.chooseMethodComboBox.currentText()
        x_component = self.chooseXVariableComboBox.currentText()
        y_component = self.chooseYVariableComboBox.currentText()
        if self.colorCodedVariableComboBox.currentText() != 'None':
            colorvar = self.colorCodedVariableComboBox.currentText()
        else:
            colorvar = None
        filename = self.plotFilenameLineEdit.text()
        figpath, figfile = '/'.join(filename.split('/')[:-1]), filename.split('/')[-1]
        pca_ica_plot(self.data[datakey], x_component, y_component, colorvar=colorvar, cmap=cmap, method=method,
                     figpath=figpath, figfile=figfile)

    def xychoices(self):
        try:
            choices = self.data[self.chooseDataComboBox.currentText()].df[
                self.chooseMethodComboBox.currentText()].columns.values
        except Exception as e:
            print(e)
            choices = ['-']
        return choices

    def on_plotFilenamePushButton_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save Plot", self.outpath, "(*.png)")
        self.plotFilenameLineEdit.setText(filename)
        if self.plotFilenameLineEdit.text() == "":
            self.plotFilenameLineEdit.setText("*.png")

    def colorchoices_change_vars(self, obj):
        obj.clear()
        choices = ['None']
        try:
            self.vars_level0 = self.data[
                self.chooseDataComboBox.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.data[
                self.chooseDataComboBox.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = self.vars_level1[self.vars_level0 != 'wvl']
            self.vars_level0 = self.vars_level0[self.vars_level0 != 'wvl']
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'masked'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'masked'])
            try:
                self.vars_level0 = [i for i in self.vars_level0 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except Exception as e:
                print(e)
                pass
            try:
                self.vars_level1 = [i for i in self.vars_level1 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except Exception as e:
                print(e)
                pass
            for i in self.vars_level1:
                choices.append(str(i))

        except Exception as e:
            print(e)
            try:
                choices.append(self.data[self.chooseDataComboBox.currentText()].columns.values)
            except Exception as e:
                print(e)
                pass
        for i in choices:
            obj.addItem(str(i))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Plot_ICA_PCA()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
