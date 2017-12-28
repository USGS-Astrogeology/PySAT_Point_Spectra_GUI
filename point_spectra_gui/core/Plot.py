import numpy as np
from PyQt5 import QtWidgets
from point_spectra_gui.util.plots import make_plot

from point_spectra_gui.ui.Plot import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Plot(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.setComboBox(self.figureNameComboBox, self.figname)
        self.changeComboListVars(self.chooseXVariableComboBox, self.get_choices())
        self.changeComboListVars(self.chooseYVariableComboBox, self.get_choices())
        self.colorComboBox.addItem("Red")
        self.colorComboBox.addItem("Green")
        self.colorComboBox.addItem("Blue")
        self.colorComboBox.addItem("Cyan")
        self.colorComboBox.addItem("Yellow")
        self.colorComboBox.addItem("Magenta")
        self.colorComboBox.addItem("Black")
        self.lineComboBox.addItem("No Line")
        self.lineComboBox.addItem("Line")
        self.lineComboBox.addItem("Dashed Line")
        self.lineComboBox.addItem("Dotted Line")
        self.markerComboBox.addItem("Circles")
        self.markerComboBox.addItem("Squares")
        self.markerComboBox.addItem("Diamonds")
        self.markerComboBox.addItem("Triangle Up")
        self.markerComboBox.addItem("Triangle Down")
        self.markerComboBox.addItem("Triangle Left")
        self.markerComboBox.addItem("Triangle Right")
        self.markerComboBox.addItem("None")
        self.alphaDoubleSpinBox.setValue(0.25)
        self.alphaDoubleSpinBox.setSingleStep(0.25)
        self.alphaDoubleSpinBox.setMaximum(1)
        self.xMinDoubleSpinBox.setMaximum(110)
        self.xMaxDoubleSpinBox.setMaximum(110)
        self.yMinDoubleSpinBox.setMaximum(110)
        self.yMaxDoubleSpinBox.setMaximum(110)
        self.plotFilenamePushButton.clicked.connect(self.on_plotFilenamePushButton_clicked)

        self.figureNameComboBox.activated[int].connect(
            lambda: self.figureNameLineEdit.setText(self.figureNameComboBox.currentText()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.changeComboListVars(self.chooseXVariableComboBox, self.get_choices()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.changeComboListVars(self.chooseYVariableComboBox, self.get_choices()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.get_minmax(self.xMinDoubleSpinBox, self.xMaxDoubleSpinBox,
                                    self.chooseXVariableComboBox.currentText()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.get_minmax(self.yMinDoubleSpinBox, self.yMaxDoubleSpinBox,
                                    self.chooseYVariableComboBox.currentText()))
        self.chooseXVariableComboBox.activated[int].connect(
            lambda: self.get_minmax(self.xMinDoubleSpinBox, self.xMaxDoubleSpinBox,
                                    self.chooseXVariableComboBox.currentText()))
        self.chooseYVariableComboBox.activated[int].connect(
            lambda: self.get_minmax(self.yMinDoubleSpinBox, self.yMaxDoubleSpinBox,
                                    self.chooseYVariableComboBox.currentText()))

    def function(self):

        datakey = self.chooseDataComboBox.currentText()
        xvar = self.chooseXVariableComboBox.currentText()
        yvar = self.chooseYVariableComboBox.currentText()

        figname = self.figureNameLineEdit.text()
        title = self.plotTitleLineEdit.text()
        xrange = self.xMinDoubleSpinBox.value(), self.xMaxDoubleSpinBox.value()
        yrange = self.yMinDoubleSpinBox.value(), self.yMaxDoubleSpinBox.value()
        xtitle = self.xTitleLineEdit.text()
        ytitle = self.yTitleLineEdit.text()
        lbl = self.legendLineEdit.text()
        one_to_one = self.oneToOneCheckBox.isChecked()

        color = self.colorComboBox.currentText()
        alpha = self.alphaDoubleSpinBox.value()
        annot_mask = None
        cmap = None
        colortitle = ''
        dpi = 1000

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

        marker = self.markerComboBox.currentText()
        if marker == 'Circles':
            marker = 'o'
        if marker == 'Squares':
            marker = 's'
        if marker == 'Diamonds':
            marker = 'D'
        if marker == 'Triangle Up':
            marker = '^'
        if marker == 'Triangle Down':
            marker = 'v'
        if marker == 'Triangle Right':
            marker = '>'
        if marker == 'Triangle Left':
            marker = '<'

        linestyle = self.lineComboBox.currentText()
        if linestyle == 'No Line':
            linestyle = 'None'
        if linestyle == 'Line':
            linestyle = '-'
        if linestyle == 'Dashed Line':
            linestyle = '--'
        if linestyle == 'Dotted Line':
            linestyle = ':'

        try:
            if self.data[datakey].df.columns.nlevels == 2:
                vars_level0 = self.data[datakey].df.columns.get_level_values(0)
                vars_level1 = self.data[datakey].df.columns.get_level_values(1)
                vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
                vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
                xvar = (vars_level0[vars_level1.index(xvar)], xvar)
                yvar = (vars_level0[vars_level1.index(yvar)], yvar)
        except AttributeError:  # df attribute doesn't exist.
            pass

        try:
            x = self.data[datakey].df[xvar]
            y = self.data[datakey].df[yvar]
        except:
            x = self.data[datakey]['cv'][xvar]
            y = self.data[datakey]['cv'][yvar]
        loadfig = None
        if not figname in self.figname:
            self.figname.append(figname)
        if figname in self.figs:
            loadfig = self.figs[figname]

        figpath = self.plotFilenameLineEdit.text()
        figpath, figfile = '/'.join(figpath.split('/')[:-1]), figpath.split('/')[-1]
        if self.plotFilenameLineEdit.text() == "" or self.plotFilenameLineEdit.text() == "*.png":
            figpath, figfile = self.outpath, figname
        self.figs[figname] = make_plot(x, y, figpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                       ytitle=ytitle, title=title,
                                       lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                       annot_mask=annot_mask, cmap=cmap,
                                       colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)

    def get_choices(self):
        try:
            self.vars_level0 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(0)
            self.vars_level1 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(1)
            self.vars_level1 = self.vars_level1[self.vars_level0 != 'wvl']
            self.vars_level0 = self.vars_level0[self.vars_level0 != 'wvl']
            self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'masked'])
            self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'masked'])
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
        return choices

    def get_minmax(self, objmin, objmax, var):
        try:
            varind = self.vars_level1.index(var)
            vartuple = (self.vars_level0[varind], self.vars_level1[varind])
            vardata = self.data[self.chooseDataComboBox.currentText()].df[vartuple]
        except:
            try:
                vardata = self.data[self.chooseDataComboBox.currentText()]['cv'][var]
            except:
                vardata = [0, 0]
        try:
            varmin = float(np.min(vardata))
            varmax = float(np.max(vardata))
            objmin.setValue(varmin)
            objmax.setValue(varmax)
        except:
            objmin.setValue(0)
            objmax.setValue(1)

    def on_plotFilenamePushButton_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save Plot", self.outpath, "(*.png)")
        self.plotFilenameLineEdit.setText(filename)
        if self.plotFilenameLineEdit.text() == "":
            self.plotFilenameLineEdit.setText("*.png")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Plot()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
