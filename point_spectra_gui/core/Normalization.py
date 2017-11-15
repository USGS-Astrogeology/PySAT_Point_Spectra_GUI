from PyQt5 import QtWidgets

from point_spectra_gui.ui.Normalization import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Normalization(Ui_Form, Basics):
    def setupUi(self, Form, restore=False):
        if restore:
            self.restored = True
        super().setupUi(Form)
        self.setup_norm_ranges()
        self.index = 1
        self.hide_settings()
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def setup_norm_ranges(self):
        self.ranges = [{'labels': [self.minimumWavelengthLabel, self.maximumWavelengthLabel],
                        'spins': [self.minimumWavelengthSpinBox, self.maximumWavelengthSpinBox]},
                       {'labels': [self.minimumWavelengthLabel_2, self.maximumWavelengthLabel_2],
                        'spins': [self.minimumWavelengthSpinBox_2, self.maximumWavelengthSpinBox_2]},
                       {'labels': [self.minimumWavelengthLabel_3, self.maximumWavelengthLabel_3],
                        'spins': [self.minimumWavelengthSpinBox_3, self.maximumWavelengthSpinBox_3]},
                       {'labels': [self.minimumWavelengthLabel_4, self.maximumWavelengthLabel_4],
                        'spins': [self.minimumWavelengthSpinBox_4, self.maximumWavelengthSpinBox_4]},
                       {'labels': [self.minimumWavelengthLabel_5, self.maximumWavelengthLabel_5],
                        'spins': [self.minimumWavelengthSpinBox_5, self.maximumWavelengthSpinBox_5]},
                       {'labels': [self.minimumWavelengthLabel_6, self.maximumWavelengthLabel_6],
                        'spins': [self.minimumWavelengthSpinBox_6, self.maximumWavelengthSpinBox_6]},
                       {'labels': [self.minimumWavelengthLabel_7, self.maximumWavelengthLabel_7],
                        'spins': [self.minimumWavelengthSpinBox_7, self.maximumWavelengthSpinBox_7]},
                       {'labels': [self.minimumWavelengthLabel_8, self.maximumWavelengthLabel_8],
                        'spins': [self.minimumWavelengthSpinBox_8, self.maximumWavelengthSpinBox_8]},
                       {'labels': [self.minimumWavelengthLabel_9, self.maximumWavelengthLabel_9],
                        'spins': [self.minimumWavelengthSpinBox_9, self.maximumWavelengthSpinBox_9]},
                       {'labels': [self.minimumWavelengthLabel_10, self.maximumWavelengthLabel_10],
                        'spins': [self.minimumWavelengthSpinBox_10, self.maximumWavelengthSpinBox_10]},
                       {'labels': [self.minimumWavelengthLabel_11, self.maximumWavelengthLabel_11],
                        'spins': [self.minimumWavelengthSpinBox_11, self.maximumWavelengthSpinBox_11]},
                       {'labels': [self.minimumWavelengthLabel_12, self.maximumWavelengthLabel_12],
                        'spins': [self.minimumWavelengthSpinBox_12, self.maximumWavelengthSpinBox_12]},
                       {'labels': [self.minimumWavelengthLabel_13, self.maximumWavelengthLabel_13],
                        'spins': [self.minimumWavelengthSpinBox_13, self.maximumWavelengthSpinBox_13]},
                       {'labels': [self.minimumWavelengthLabel_14, self.maximumWavelengthLabel_14],
                        'spins': [self.minimumWavelengthSpinBox_14, self.maximumWavelengthSpinBox_14]},
                       {'labels': [self.minimumWavelengthLabel_15, self.maximumWavelengthLabel_15],
                        'spins': [self.minimumWavelengthSpinBox_15, self.maximumWavelengthSpinBox_15]}]

    def checkForNewMax(self):
        for i in range(len(self.ranges) - 1):
            self.ranges[i]['spins'][0].valueChanged.connect(self.ranges[i]['spins'][1].setMinimum)
            self.ranges[i]['spins'][1].valueChanged.connect(self.ranges[i + 1]['spins'][0].setMinimum)
            self.ranges[i + 1]['spins'][1].setMinimum(self.ranges[i + 1]['spins'][0].value())

    def setMaximumValue(self, value):
        for range in self.ranges:
            range['spins'][0].setMaximum(value)
            range['spins'][1].setMaximum(value)

    def hide_settings(self):
        for i in range(self.index, len(self.ranges)):
            if self.ranges[i]['spins'][0].value() == self.ranges[i]['spins'][1].value():
                self.ranges[i]['spins'][0].setHidden(True)
                self.ranges[i]['spins'][1].setHidden(True)
                self.ranges[i]['labels'][0].setHidden(True)
                self.ranges[i]['labels'][1].setHidden(True)
            else:
                self.ranges[i]['spins'][0].setHidden(False)
                self.ranges[i]['spins'][1].setHidden(False)
                self.ranges[i]['labels'][0].setHidden(False)
                self.ranges[i]['labels'][1].setHidden(False)

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)
        self.chooseDataComboBox.currentIndexChanged.connect(
            lambda: self.changeComboListVars(self.varToNormalizeListWidget, self.xvar_choices()))
        self.changeComboListVars(self.varToNormalizeListWidget, self.xvar_choices())
        self.setMaximumValue(999999999)
        self.qt.isGuiChanged(self.checkForNewMax)
        self.qt.isGuiChanged(self.hide_settings)
        self.add_range_button.clicked.connect(lambda: self.on_addRange_pushed())
        self.delete_range_button.clicked.connect(lambda: self.on_deleteRange_pushed())

    def on_addRange_pushed(self):
        if self.index < len(self.ranges):
            self.ranges[self.index]['spins'][1].setValue(self.ranges[self.index]['spins'][1].value() + 1)
            self.checkForNewMax()
            self.index += 1
        else:
            print("Cannot add more ranges!")

    def on_deleteRange_pushed(self):
        if self.index > 1:
            self.index -= 1
            self.ranges[self.index]['spins'][0].setValue(self.ranges[self.index - 1]['spins'][1].value())
            self.ranges[self.index]['spins'][1].setValue(self.ranges[self.index - 1]['spins'][1].value())
            self.checkForNewMax()
        else:
            print("Cannot delete any more ranges!")

    def function(self):
        # self.connectWidgets()
        datakey = self.chooseDataComboBox.currentText()

        if self.checkoptions(datakey, self.datakeys, 'data set'):
            self.connectWidgets()
        else:
            range_vals = []
            for i in range(len(self.ranges)):
                range_min = self.ranges[i]['spins'][0].value()
                range_max = self.ranges[i]['spins'][1].value()
                if range_min != range_max:
                    range_vals.append([range_min, range_max])
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
