import numpy as np
from PyQt5 import QtWidgets

from point_spectra_gui.ui.Normalization import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class norm_range:
    def __init__(self, minLabel, minSpin, maxLabel, maxSpin, hidden):
        self.minLabel = minLabel
        self.minSpin = minSpin
        self.maxLabel = maxLabel
        self.maxSpin = maxSpin
        self.hidden = hidden
        self.hidden.setHidden(True)
        self.hidden.stateChanged.connect(self.Hidden)
        self.setLimits(0.0, 9999999.0)

    def Hidden(self):
        if self.hidden.isChecked():
            self.minLabel.setHidden(True)
            self.minSpin.setHidden(True)
            self.maxLabel.setHidden(True)
            self.maxSpin.setHidden(True)
        else:
            self.minLabel.setHidden(False)
            self.minSpin.setHidden(False)
            self.maxLabel.setHidden(False)
            self.maxSpin.setHidden(False)

    def getValues(self):
        return self.minSpin.value(), self.maxSpin.value()

    def setLimits(self, min, max):
        self.minSpin.setMinimum(min)
        self.maxSpin.setMinimum(min)
        self.minSpin.setMaximum(max)
        self.maxSpin.setMaximum(max)

    def setValue(self, int_):
        self.minSpin.setValue(int_)
        self.maxSpin.setValue(int_)


class Normalization(Ui_Form, Basics):
    def setupUi(self, Form, restore=False):
        if restore:
            self.restored = True
        super().setupUi(Form)
        self.setup_norm_ranges()
        self.index.setHidden(True)
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def setup_norm_ranges(self):
        self.ranges = [norm_range(self.minWvlLabel, self.minWvlSpin, self.maxWvlLabel, self.maxWvlSpin,
                                  self.hidden_1),
                       norm_range(self.minWvlLabel_2, self.minWvlSpin_2, self.maxWvlLabel_2, self.maxWvlSpin_2,
                                  self.hidden_2),
                       norm_range(self.minWvlLabel_3, self.minWvlSpin_3, self.maxWvlLabel_3, self.maxWvlSpin_3,
                                  self.hidden_3),
                       norm_range(self.minWvlLabel_4, self.minWvlSpin_4, self.maxWvlLabel_4, self.maxWvlSpin_4,
                                  self.hidden_4),
                       norm_range(self.minWvlLabel_5, self.minWvlSpin_5, self.maxWvlLabel_5, self.maxWvlSpin_5,
                                  self.hidden_5),
                       norm_range(self.minWvlLabel_6, self.minWvlSpin_6, self.maxWvlLabel_6, self.maxWvlSpin_6,
                                  self.hidden_6),
                       norm_range(self.minWvlLabel_7, self.minWvlSpin_7, self.maxWvlLabel_7, self.maxWvlSpin_7,
                                  self.hidden_7),
                       norm_range(self.minWvlLabel_8, self.minWvlSpin_8, self.maxWvlLabel_8, self.maxWvlSpin_8,
                                  self.hidden_8),
                       norm_range(self.minWvlLabel_9, self.minWvlSpin_9, self.maxWvlLabel_9, self.maxWvlSpin_9,
                                  self.hidden_9),
                       norm_range(self.minWvlLabel_10, self.minWvlSpin_10, self.maxWvlLabel_10, self.maxWvlSpin_10,
                                  self.hidden_10),
                       norm_range(self.minWvlLabel_11, self.minWvlSpin_11, self.maxWvlLabel_11, self.maxWvlSpin_11,
                                  self.hidden_11),
                       norm_range(self.minWvlLabel_12, self.minWvlSpin_12, self.maxWvlLabel_12, self.maxWvlSpin_12,
                                  self.hidden_12),
                       norm_range(self.minWvlLabel_13, self.minWvlSpin_13, self.maxWvlLabel_13, self.maxWvlSpin_13,
                                  self.hidden_13),
                       norm_range(self.minWvlLabel_14, self.minWvlSpin_14, self.maxWvlLabel_14, self.maxWvlSpin_14,
                                  self.hidden_14),
                       norm_range(self.minWvlLabel_15, self.minWvlSpin_15, self.maxWvlLabel_15, self.maxWvlSpin_15,
                                  self.hidden_15)]
        self.spin_list = []
        for i in self.ranges:
            self.spin_list.append(i.minSpin)
            self.spin_list.append(i.maxSpin)
            i.hidden.setChecked(True)
        self.ranges[0].hidden.setChecked(False)

    def setDataLimits(self):
        # if the data exists, get the min and max of the data and use as the limits for the ranges
        datamin = 0.0
        datamax = 9999999.0
        try:
            data = self.data[self.chooseDataComboBox.currentText()]
            tempmin = np.min(data.df[self.varToNormalizeListWidget.currentItem().text()].columns.values)
            tempmax = np.max(data.df[self.varToNormalizeListWidget.currentItem().text()].columns.values)
            if type(tempmin) is not str:
                datamin = tempmin
            if type(tempmax) is not str:
                datamax = tempmax
        except:
            pass

        for i in range(len(self.ranges)):
            self.ranges[i].setLimits(datamin, datamax)
        try:
            if type(tempmin) is not str:
                self.setDataRanges()
        except:
            pass

    def setDataRanges(self):
        x = self.data[self.chooseDataComboBox.currentText()].df[
            self.varToNormalizeListWidget.currentItem().text()].columns.values
        # borrowed this from baseline removal code, which in turn borrowed from matplotlib's boxplot outlier detection.
        d = np.diff(x)
        q1, q3 = np.percentile(d, (25, 75))
        cutoff = q3 + 1.5 * (q3 - q1)
        inds, = np.where(d > cutoff)
        xvals = (x[inds] + x[inds + 1]) / 2.0  # set values to the middle of the gaps
        xvals = np.append(xvals, np.max(x))
        self.index.setValue(len(xvals))
        print('index set to ' + str(self.index.value()))
        for i, val in enumerate(xvals):
            self.ranges[i].maxSpin.setValue(val)
            self.ranges[i].hidden.setChecked(False)

    def updateVal(self):
        # step through the spinboxes and make sure that each successive box value is
        # greater than or equal to the one before it
        for i in range(1, len(self.spin_list)):
            if self.spin_list[i].value() < self.spin_list[i - 1].value():
                self.spin_list[i].setValue(self.spin_list[i - 1].value())

    def connectWidgets(self):
        # populate combobox with dataset names
        self.setComboBox(self.chooseDataComboBox, self.datakeys)

        # update list of variables to normalize when data set selection is changed
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.varToNormalizeListWidget, self.xvar_choices()))
        self.changeComboListVars(self.varToNormalizeListWidget, self.xvar_choices())

        # when the variable to normalize is changed, update the min max and default norm ranges
        self.varToNormalizeListWidget.itemSelectionChanged.connect(self.setDataLimits)

        # when anything in the gui is changed, run update val to make sure values are increasing
        self.qt.isGuiChanged(self.updateVal)

        # connect the add and delete ranges buttons
        self.add_range_button.clicked.connect(lambda: self.on_addRange_pushed())
        self.delete_range_button.clicked.connect(lambda: self.on_deleteRange_pushed())

    def on_addRange_pushed(self):
        if self.index.value() < len(self.ranges):
            self.ranges[self.index.value()].hidden.setChecked(False)
            self.index.setValue(self.index.value() + 1)
            print('Index is now: ' + str(self.index.value()))
        else:
            print("Cannot add more ranges!")

    def on_deleteRange_pushed(self):
        if self.index.value() > 1:
            self.index.setValue(self.index.value() - 1)
            self.ranges[self.index.value()].hidden.setChecked(True)
            print('Index is now: ' + str(self.index.value()))
        else:
            print("Cannot delete any more ranges!")

    def function(self):
        datakey = self.chooseDataComboBox.currentText()
        if self.checkoptions(datakey, self.datakeys, 'data set'):
            self.connectWidgets()
        else:
            range_vals = []
            for i in self.ranges:
                range_min, range_max = i.getValues()
                if range_min != range_max:
                    range_vals.append([range_min, range_max])
                    pass
            try:
                col_var = self.varToNormalizeListWidget.currentItem().text()
            except:
                print("Did you remember to select a variable?")
            print("{}".format(range_vals))
            try:
                self.data[datakey].norm(range_vals, col_var)
                print("Normalization has been applied to the ranges: " + str(range_vals))
            except Exception as e:
                print("There was a problem: ", e)

    def xvar_choices(self):
        try:
            try:
                xvarchoices = self.data[self.chooseDataComboBox.currentText()].df.columns.levels[
                    0].values
            except:
                xvarchoices = self.data[self.chooseDataComboBox.currentText()].columns.values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Normalization()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
