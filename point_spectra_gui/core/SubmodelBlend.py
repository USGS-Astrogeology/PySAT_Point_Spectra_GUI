from PyQt5 import QtWidgets
from libpysat.regression import sm

from point_spectra_gui.ui.SubmodelBlend import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class subWidgets:
    def __init__(self, predictionComboBox, minLabel, minSpinBox, maxLabel, maxSpinBox):
        self.predictionComboBox = predictionComboBox
        self.minLabel = minLabel
        self.minSpinBox = minSpinBox
        self.maxLabel = maxLabel
        self.maxSpinBox = maxSpinBox

    def get_predictionComboBox(self):
        return self.predictionComboBox

    def get_minSpinBox(self):
        return self.minSpinBox

    def get_maxSpinBox(self):
        return self.maxSpinBox

    def setHidden(self, bool):
        self.predictionComboBox.setHidden(bool)
        self.minLabel.setHidden(bool)
        self.minSpinBox.setHidden(bool)
        self.maxLabel.setHidden(bool)
        self.maxSpinBox.setHidden(bool)

    def getValues(self):
        return [self.predictionComboBox.currentText(), [float(self.minSpinBox.value()), float(self.maxSpinBox.value())]]

    def setValue(self, int_):
        self.minSpinBox.setValue(int_)
        self.maxSpinBox.setValue(int_)

    def spinBox(self, int_):
        if int_ == 0:
            return self.minSpinBox
        elif int_ == 1:
            return self.maxSpinBox
        else:
            return "Not a valid number"


class SubmodelBlend(Ui_Form, Basics):
    def __init__(self):
        super().__init__()
        self.subwidgets = []
        self.index = 0


    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        Basics.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def set_index(self):
        self.index = self.index_spin.value()
        self.setHidden(self.subwidgets)

    def connectWidgets(self):
        self.index_spin.valueChanged.connect(self.set_index)
        self.index_spin.setHidden(True)
        self.setComboBox(self.chooseDatacomboBox,self.datakeys)
        self.get_Predictions()
        self.chooseDatacomboBox.currentIndexChanged.connect(self.get_Predictions)
        self.setupWidgets()
        self.setHidden(self.subwidgets)
        try:
            self.setComboBox(self.referencePredictionComboBox, self.predictnames)
            self.setComboBox(self.lowPredictionComboBox, self.predictnames)
            self.setComboBox(self.highPredictionComboBox, self.predictnames)
            self.setComboBox(self.optimizeSubRangesComboBox, self.data[self.chooseDatacomboBox.currentText()].df['comp'].columns.values)

        except:
            pass
        self.addSubPushButton.clicked.connect(self.on_addSubmodel_pushed)
        self.deleteSubPushButton.clicked.connect(self.on_deleteSubmodel_pushed)
        self.optimizeSubRangesLabel.setHidden(True)
        self.optimizeSubRangesComboBox.setHidden(True)


    def setHidden(self, list):
        for i in range(0, len(list)):
            if i < self.index:
                list[i].setHidden(False)
            else:
                list[i].setHidden(True)

    def get_Predictions(self):
        try:
            self.predictnames = self.data[self.chooseDatacomboBox.currentText()].df['predict'].columns.values
        except:
            pass

    def function(self):
        blendranges = []
        submodel_blend_names = []
        submodel_predictions = []
        datakey = self.chooseDatacomboBox.currentText()
        refcol = ('comp',self.optimizeSubRangesComboBox.currentText())

        #start with the low model
        blendranges.append([-9999, float(self.lowPredictionMaxSpinBox.value())])
        submodel_blend_names.append(self.lowPredictionComboBox.currentText())
        submodel_predictions.append(self.data[datakey].df[('predict',self.lowPredictionComboBox.currentText())])

        #append the intermediate submodels
        for i in range(0, self.index):
            temp_vals = self.subwidgets[i].getValues()
            blendranges.append(temp_vals[1])
            submodel_blend_names.append(temp_vals[0])
            submodel_predictions.append(self.data[datakey].df[('predict', temp_vals[0])])

        #append the high model
        blendranges.append([float(self.highPredictionMinSpinBox.value()), 9999])
        submodel_blend_names.append(self.highPredictionComboBox.currentText())
        submodel_predictions.append(self.data[datakey].df[('predict', self.highPredictionComboBox.currentText())])

        #append the reference model as a catch-all
        blendranges.append([-9999,9999])
        submodel_blend_names.append(self.referencePredictionComboBox.currentText())
        submodel_predictions.append(self.data[datakey].df[('predict', self.referencePredictionComboBox.currentText())])

        if self.optimizeSubRangesCheckBox.isChecked():
            truevals = self.data[datakey].df[refcol]
        else:
            truevals = None

        sm_obj = sm.sm(blendranges)
        # optimize blending if reference data is provided
        if truevals is not None:
            predictions_blended = sm_obj.do_blend(submodel_predictions, truevals=truevals)
        else:
        # otherwise just blend the predictions together
            predictions_blended = sm_obj.do_blend(submodel_predictions)

        # save the blended predictions
        self.data[datakey].df[('predict', 'Blended-Predict '+str(sm_obj.blendranges))] = predictions_blended

    def on_addSubmodel_pushed(self):
        if self.index < len(self.subwidgets):
            self.subwidgets[self.index].setHidden(False)
            self.setComboBox(self.subwidgets[self.index].get_predictionComboBox(), self.predictnames)
            self.index += 1
            self.index_spin.setValue(self.index)
        else:
            print("Cannot add more submodels")

    def on_deleteSubmodel_pushed(self):
        if self.index > 1:
            self.index -= 1
            self.subwidgets[self.index].setHidden(True)
            self.subwidgets[self.index].setValue(0)
            self.index_spin.setValue(self.index)
        else:
            print("Cannot delete any more submodels")

    def setupWidgets(self):
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox, self.minLabel, self.minSpinBox, self.maxLabel, self.maxSpinBox))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_2, self.minLabel_2, self.minSpinBox_2, self.maxLabel_2, self.maxSpinBox_2))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_3, self.minLabel_3, self.minSpinBox_3, self.maxLabel_3, self.maxSpinBox_3))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_4, self.minLabel_4, self.minSpinBox_4, self.maxLabel_4, self.maxSpinBox_4))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_5, self.minLabel_5, self.minSpinBox_5, self.maxLabel_5, self.maxSpinBox_5))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_6, self.minLabel_6, self.minSpinBox_6, self.maxLabel_6, self.maxSpinBox_6))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_7, self.minLabel_7, self.minSpinBox_7, self.maxLabel_7, self.maxSpinBox_7))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_8, self.minLabel_8, self.minSpinBox_8, self.maxLabel_8, self.maxSpinBox_8))
        self.subwidgets.append(
            subWidgets(self.PredictionComboBox_9, self.minLabel_9, self.minSpinBox_9, self.maxLabel_9, self.maxSpinBox_9))
        self.subwidgets.append(subWidgets(self.PredictionComboBox_10, self.minLabel_10, self.minSpinBox_10, self.maxLabel_10,
                                          self.maxSpinBox_10))
        self.subwidgets.append(subWidgets(self.PredictionComboBox_11, self.minLabel_11, self.minSpinBox_11, self.maxLabel_11,
                                          self.maxSpinBox_11))
        self.subwidgets.append(subWidgets(self.PredictionComboBox_12, self.minLabel_12, self.minSpinBox_12, self.maxLabel_12,
                                          self.maxSpinBox_12))
        self.subwidgets.append(subWidgets(self.PredictionComboBox_13, self.minLabel_13, self.minSpinBox_13, self.maxLabel_13,
                                          self.maxSpinBox_13))
        self.subwidgets.append(subWidgets(self.PredictionComboBox_14, self.minLabel_14, self.minSpinBox_14, self.maxLabel_14,
                                          self.maxSpinBox_14))
        self.subwidgets.append(subWidgets(self.PredictionComboBox_15, self.minLabel_15, self.minSpinBox_15, self.maxLabel_15,
                                          self.maxSpinBox_15))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = SubmodelBlend()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
