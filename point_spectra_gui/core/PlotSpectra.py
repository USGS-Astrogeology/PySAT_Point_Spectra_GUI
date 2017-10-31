import numpy as np
from PyQt5 import QtWidgets
from libpysat.plotting.plots import make_plot

from point_spectra_gui.ui.PlotSpectra import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class PlotSpectra(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.colorComboBox.addItem("Red")
        self.colorComboBox.addItem("Green")
        self.colorComboBox.addItem("Blue")
        self.colorComboBox.addItem("Cyan")
        self.colorComboBox.addItem("Yellow")
        self.colorComboBox.addItem("Magenta")
        self.colorComboBox.addItem("Black")
        self.lineComboBox.addItem("Line")
        self.lineComboBox.addItem("Dashed Line")
        self.lineComboBox.addItem("Dotted Line")
        self.lineComboBox.addItem("Points (No Line)")
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.lineWidthDoubleSpinBox.setRange(0, 10)
        self.lineWidthDoubleSpinBox.setValue(0.5)
        self.lineWidthDoubleSpinBox.setSingleStep(0.05)
        self.alphaDoubleSpinBox.setRange(0, 1)
        self.alphaDoubleSpinBox.setValue(1.0)
        self.alphaDoubleSpinBox.setSingleStep(0.1)
        self.maxDoubleSpinBox.setMaximum(99999)
        self.maxDoubleSpinBox.setMinimum(0)
        self.minDoubleSpinBox.setMaximum(99999)
        self.minDoubleSpinBox.setMinimum(0)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        try:
            self.setComboBox(self.chooseDataComboBox, self.datakeys)
            self.setListWidget(self.xVariableListWidget, self.xvar_choices())
            self.plot_spect_change_vars(self.chooseColumnComboBox)
            self.plot_spect_update_list(self.chooseRowsListWidget)
        except Exception as e:
            print("Could not process lists: {}".format(e))

        self.chooseDataComboBox.activated[int].connect(lambda: self.plot_spect_change_vars(self.chooseColumnComboBox))
        self.chooseColumnComboBox.activated[int].connect(lambda: self.plot_spect_update_list(self.chooseRowsListWidget))
        self.chooseDataComboBox.activated[int].connect(lambda: self.plot_spect_update_list(self.chooseRowsListWidget))
        try:
            self.xVariableListWidget.itemSelectionChanged.connect(
                lambda: self.set_spect_minmax(self.minDoubleSpinBox, self.maxDoubleSpinBox,
                                              self.xVariableListWidget.selectedItems()[0].text()))
        except:
            pass

    def function(self):
        yrange = None
        xtitle = 'Wavelength (nm)'
        ytitle = None
        lbl = None
        one_to_one = False
        dpi = 1000
        annot_mask = None
        cmap = None
        colortitle = ''
        marker = None

        datakey = self.chooseDataComboBox.currentText()
        try:
            xcol = self.xVariableListWidget.selectedItems()[0].text()
        except:
            xcol = 'wvl'
        col = self.chooseColumnComboBox.currentText()
        try:
            row = self.chooseRowsListWidget.selectedItems()[0].text()
        except:
            row = 'None Selected'
        figname = self.figureNameLineEdit.text()
        title = self.plotTitleLineEdit.text()
        figfile = self.plotFilenameLineEdit.text()
        figpath, figfile = '/'.join(figfile.split('/')[:-1]), figfile.split('/')[-1]
        color = self.colorComboBox.currentText()
        alpha = self.alphaDoubleSpinBox.value()
        linewidth = self.lineWidthDoubleSpinBox.value()

        if color == 'Red':
            color = [1, 0, 0, alpha]
        elif color == 'Green':
            color = [0, 1, 0, alpha]
        elif color == 'Blue':
            color = [0, 0, 1, alpha]
        elif color == 'Cyan':
            color = [0, 1, 1, alpha]
        elif color == 'Yellow':
            color = [1, 1, 0, alpha]
        elif color == 'Magenta':
            color = [1, 0, 1, alpha]
        elif color == 'Black':
            color = [0, 0, 0, alpha]
        else:
            color = [0, 0, 0, alpha]

        line = self.lineComboBox.currentText()
        if line == 'Points (No Line)':
            linestyle = 'None'
        elif line == 'Line':
            linestyle = '-'
        elif line == 'Dashed Line':
            linestyle = '--'
        elif line == 'Dotted Line':
            linestyle = ':'
        else:
            linestyle = '-'

        xmin = self.minDoubleSpinBox.value()
        xmax = self.maxDoubleSpinBox.value()
        xrange = [xmin, xmax]
        self.data[datakey].enumerate_duplicates(col)
        data = self.data[datakey].df

        y = np.squeeze(np.array(data.loc[data[('meta', col)].isin([row])][xcol].T))
        x = np.array(data[xcol].columns.values)
        if linestyle == 'None':
            marker = 'o'
        try:
            loadfig = self.figs[figname]
        except:
            loadfig = None

        self.figs[figname] = make_plot(x, y, figpath=figpath, figfile=figfile, xrange=xrange, yrange=yrange,
                                       xtitle=xtitle,
                                       ytitle=ytitle, title=title,
                                       lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                       annot_mask=annot_mask, cmap=cmap,
                                       colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle,
                                       linewidth=linewidth)

    def xvar_choices(self):
        try:
            try:
                xvarchoices = self.data[self.chooseDataComboBox.currentText()].df.columns.levels[0].values
            except:
                xvarchoices = self.data[self.chooseDataComboBox.currentText()].columns.values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices

    def plot_spect_change_vars(self, obj):
        obj.clear()
        try:
            self.vars_level0 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = self.vars_level1[self.vars_level0 == 'meta']
            self.vars_level0 = self.vars_level0[self.vars_level0 != 'meta']

            try:
                self.vars_level0 = [i for i in self.vars_level0 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except:
                pass
            try:
                self.vars_level1 = [i for i in self.vars_level1 if
                                    'Unnamed' not in str(i)]  # remove unnamed columns from choices
            except:
                pass
            choices = self.vars_level1

        except:
            try:
                choices = self.data[self.chooseDataComboBox.currentText()].columns.values
            except:
                choices = ['No valid choices']
        for i in choices:
            obj.addItem(str(i))

    def plot_spect_update_list(self, obj):
        try:
            obj.clear()
            self.data[self.chooseDataComboBox.currentText()].enumerate_duplicates(
                self.chooseColumnComboBox.currentText())
            rowchoices = self.data[self.chooseDataComboBox.currentText()].df[
                ('meta', self.chooseColumnComboBox.currentText())]
            for i in rowchoices:
                obj.addItem(i)
        except:
            pass

    def set_spect_minmax(self, objmin, objmax, var):
        try:
            vars = self.data[self.chooseDataComboBox.currentText()].df[var].columns.values
            objmin.setValue(min(vars))
            objmax.setValue(max(vars))
        except Exception as e:
            print(e)

    def on_pushButton_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save Plot", self.outpath, "(*.png)")
        self.plotFilenameLineEdit.setText(filename)
        if self.plotFilenameLineEdit.text() == "":
            self.plotFilenameLineEdit.setText("*.png")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = PlotSpectra()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
