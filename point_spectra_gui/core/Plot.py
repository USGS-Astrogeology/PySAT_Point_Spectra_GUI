from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter
import numpy as np
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype

from point_spectra_gui.ui.Plot import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.plots import make_plot

class Plot(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.newfig_checkBox.setHidden(True)
        self.colorcode_checkBox.setHidden(True)
        completer = QCompleter()
        self.newfig_lineEdit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.get_data(model)

        choices2 = ['None']
        datakey_choices = self.datakeys
        for choice in datakey_choices:
            choices2.append(choice)
        datakey_choices = choices2
        fig_choices = self.figname
        fig_choices2 = ['New Figure']
        for choice in fig_choices:
            fig_choices2.append(choice)
        fig_choices = fig_choices2
        none_choice = ['None']

        self.setComboBox(self.chooseDataComboBox, datakey_choices)
        self.setComboBox(self.figname_comboBox, fig_choices)
        self.setComboBox(self.chooseYVariableComboBox, self.get_choices())
        self.setComboBox(self.chooseXVariableComboBox, self.get_choices())
        self.setComboBox(self.comboBoxcolorvar, self.get_choices())

        self.plotFilenamePushButton.clicked.connect(self.plotFilenamePushButton_clicked)

        self.figname_comboBox.activated[int].connect(
            lambda: self.newfig_check())
        self.newfig_checkBox.stateChanged.connect(
            lambda:self.fig_options())
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.changeComboListVars(self.chooseXVariableComboBox, self.get_choices()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.changeComboListVars(self.chooseYVariableComboBox, self.get_choices()))
        self.chooseDataComboBox.activated[int].connect(
             lambda: self.changeComboListVars(self.comboBoxcolorvar, self.get_choices()))
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
        self.comboBoxcolorvar.activated[int].connect(self.color_check)
        self.colorcode_checkBox.stateChanged.connect(self.disable_colors)
        self.chooseXVariableComboBox.activated[int].connect(self.set_xTitle)
        self.chooseYVariableComboBox.activated[int].connect(self.set_yTitle)

    def set_xTitle(self):
        self.xTitleLineEdit.setText(self.chooseXVariableComboBox.currentText())

    def set_yTitle(self):
        self.yTitleLineEdit.setText(self.chooseYVariableComboBox.currentText())

    def newfig_check(self):
        if self.figname_comboBox.currentText() == 'New Figure':
            self.newfig_checkBox.setChecked(True)
        else:
            self.newfig_checkBox.setChecked(False)

    def fig_options(self):
        if self.newfig_checkBox.isChecked():
            self.xMinLabel.setHidden(False)
            self.xMinDoubleSpinBox.setHidden(False)
            self.xMaxLabel.setHidden(False)
            self.xMaxDoubleSpinBox.setHidden(False)
            self.xTitleLabel.setHidden(False)
            self.xTitleLineEdit.setHidden(False)
            self.yMaxLabel.setHidden(False)
            self.yMaxDoubleSpinBox.setHidden(False)
            self.yMinDoubleSpinBox.setHidden(False)
            self.yMinLabel.setHidden(False)
            self.yTitleLabel.setHidden(False)
            self.yTitleLineEdit.setHidden(False)
            self.plotTitleLabel.setHidden(False)
            self.plotTitleLineEdit.setHidden(False)
            self.newfig_lineEdit.setHidden(False)
            self.newfig_label.setHidden(False)
        else:
            self.xMinLabel.setHidden(True)
            self.xMinDoubleSpinBox.setHidden(True)
            self.xMaxLabel.setHidden(True)
            self.xMaxDoubleSpinBox.setHidden(True)
            self.xTitleLabel.setHidden(True)
            self.xTitleLineEdit.setHidden(True)
            self.yMinLabel.setHidden(True)
            self.yMinDoubleSpinBox.setHidden(True)
            self.yMaxLabel.setHidden(True)
            self.yMaxDoubleSpinBox.setHidden(True)
            self.yTitleLabel.setHidden(True)
            self.yTitleLineEdit.setHidden(True)
            self.plotTitleLabel.setHidden(True)
            self.plotTitleLineEdit.setHidden(True)
            self.newfig_lineEdit.setHidden(True)
            self.newfig_label.setHidden(True)

    def color_check(self):
        if self.comboBoxcolorvar.currentText() == 'None':
            self.colorcode_checkBox.setChecked(False)
        else:
            self.colorcode_checkBox.setChecked(True)

    def disable_colors(self):
          if self.colorcode_checkBox.isChecked():
              self.colorComboBox.setHidden(True)
              self.colorLabel.setHidden(True)
              self.legendLineEdit.setHidden(True)
              self.legendLabel.setHidden(True)
              self.lineComboBox.setHidden(True)
              self.lineLabel.setHidden(True)
              self.alphaLabel.setHidden(True)
              self.alphaDoubleSpinBox.setHidden(True)
          else:
              self.colorComboBox.setHidden(False)
              self.colorLabel.setHidden(False)
              self.legendLineEdit.setHidden(False)
              self.legendLabel.setHidden(False)
              self.lineComboBox.setHidden(False)
              self.lineLabel.setHidden(False)
              self.alphaLabel.setHidden(False)
              self.alphaDoubleSpinBox.setHidden(False)


    def run(self):
        cmap = 'viridis'
        datakey = self.chooseDataComboBox.currentText()
        xvar = self.chooseXVariableComboBox.currentText()
        yvar = self.chooseYVariableComboBox.currentText()
        colorvar = self.comboBoxcolorvar.currentText()

        if colorvar != 'None':
            for top_col_val in list(self.data[datakey].df.columns.levels[0]):
                try:
                    colorval = self.data[datakey].df[(top_col_val,colorvar)]
                except:
                    pass

        else:
            colorval = None

        if self.figname_comboBox.currentText() == 'New Figure':
            figname = self.newfig_lineEdit.text()
        else:
            figname = self.figname_comboBox.currentText()

        loadfig = None
        if not figname in self.figname:
            self.figname.append(figname)
        if figname in self.figs:
            loadfig = self.figs[figname]

        title = self.plotTitleLineEdit.text()
        xrange = self.xMinDoubleSpinBox.value(), self.xMaxDoubleSpinBox.value()
        yrange = self.yMinDoubleSpinBox.value(), self.yMaxDoubleSpinBox.value()
        xtitle = self.xTitleLineEdit.text()
        ytitle = self.yTitleLineEdit.text()
        lbl = self.legendLineEdit.text()
        one_to_one = self.oneToOneCheckBox.isChecked()
        color = self.colorComboBox.currentText()

        alpha = self.alphaDoubleSpinBox.value()/100.0
        annot_mask = None
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



        figpath = self.plotFilenameLineEdit.text()
        figpath, figfile = '/'.join(figpath.split('/')[:-1]), figpath.split('/')[-1]
        if self.plotFilenameLineEdit.text() == "" or self.plotFilenameLineEdit.text() == "*.png":
            figpath, figfile = self.outpath, figname
        self.figs[figname] = make_plot(x, y, figpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                       ytitle=ytitle, title=title,
                                       lbl=lbl, one_to_one=one_to_one, dpi=dpi, colorvar=colorvar, colorval=colorval,
                                       annot_mask=annot_mask, cmap=cmap, color = color,
                                       colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)

    def get_data_levels(self):
        self.vars_level0 = []
        self.vars_level1 = []

        vars_level0 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(0)
        vars_level1 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(1)
        exclude_list = ['wvl','masked','peak_area']
        for i in exclude_list:
            vars_level1 = vars_level1[vars_level0 != i]
            vars_level0 = vars_level0[vars_level0 != i]

        #remove unnamed columns
        try:
            unnamed_flag0 = []
            for i in vars_level0:
                flag_val = 'Unnamed' not in str(i)
                unnamed_flag0.append(flag_val)
            unnamed_flag1 = []
            for i in vars_level1:
                flag_val = 'Unnamed' not in str(i)
                unnamed_flag1.append(flag_val)

            #at some point, need to make this more elegant
            unnamed_flag = np.logical_and(unnamed_flag0, unnamed_flag1).tolist()
            vars_level0 = np.array(vars_level0)[unnamed_flag].tolist()
            vars_level1 = np.array(vars_level1)[unnamed_flag].tolist()

        except:
            pass

        #keep only columns that are numerical
        for i in list(range(len(vars_level0))):
            if is_numeric_dtype(self.data[self.chooseDataComboBox.currentText()].df[vars_level0[i], vars_level1[i]]):
                self.vars_level0.append(vars_level0[i])
                self.vars_level1.append(vars_level1[i])
            else:
                print(vars_level0[i] + ',' + vars_level1[i] + ' is non-numeric. Excluding.')


    def get_choices(self):
        try:
            self.get_data_levels()
            choices = self.vars_level1

        except:
            try:
                choices = self.data[self.chooseDataComboBox.currentText()].columns.values
            except:
                choices = ['No valid choices']
        choices2 = ['None']
        for choice in choices:
            choices2.append(choice)
        return choices2

    def get_data(self, model):
        model.setStringList(self.figname)

    def get_minmax(self, objmin, objmax, var):
        try:
            self.get_data_levels()
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

    def plotFilenamePushButton_clicked(self):
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
