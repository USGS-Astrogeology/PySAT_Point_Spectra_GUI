import traceback

from PyQt5 import QtGui, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox
from point_spectra_gui.ui_modules.Error_ import error_print


class regression_predict_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.qtickle = Qtickle.Qtickle(self)
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.restr_list = restr_list
        self.pysat_fun = pysat_fun
        self.ui_id = None
        self.module_layout = module_layout
        self.main()

    def main(self):
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.regression_ui()
        self.set_predict_parameters()
        self.get_predict_parameters()
        self.pysat_fun.set_greyed_modules(self.regression_predict)

        self.regression_predict_choosedata.currentIndexChanged.connect(lambda: self.get_predict_parameters())
        self.regression_predict_choosemodel.currentIndexChanged.connect(lambda: self.get_predict_parameters())

    def get_predict_parameters(self):

        datakey = self.regression_predict_choosedata.currentText()
        modelkey = self.regression_predict_choosemodel.currentText()
        predictname = ('predict', modelkey + ' - ' + datakey + ' - Predict')

        args = [datakey, modelkey, predictname]
        kws = {}
        ui_list = 'do_regression_predict'
        fun_list = 'do_regression_predict'
        r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def set_predict_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guiRestore(self.restr_list)
        if self.arg_list is not None:
            try:
                datakey = self.arg_list[0]
                modelkey = self.arg_list[1]
                # self.regression_predict_choosedata = make_combobox(datakey)
                # self.regression_predict_choosemodel = make_combobox(modelkey)
                self.regression_predict_choosedata.setItemText(0, datakey)
                self.regression_predict_choosemodel.setItemText(0, modelkey)
                pass
            except Exception as e:
                print(e)

    def regression_ui(self):
        self.regression_predict = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regression_predict.setFont(font)
        self.regression_predict_vlayout = QtWidgets.QVBoxLayout(self.regression_predict)
        # create a layout for choosing data to predict on
        self.regression_predict_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.regression_predict_choosedata_label = QtWidgets.QLabel(self.regression_predict)
        self.regression_predict_choosedata_label.setObjectName("regression_predict_choosedata_label")
        self.regression_predict_choosedata_hlayout.addWidget(self.regression_predict_choosedata_label)
        # create the combobox with data choices
        datachoices = self.pysat_fun.datakeys
        # TODO add logic for dealing with restoring this module

        self.regression_predict_choosedata = make_combobox(datachoices)
        # self.regression_predict_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_predict_choosedata.setObjectName("regression_predict_choosedata")
        self.regression_predict_choosedata_hlayout.addWidget(self.regression_predict_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_predict_choosedata_hlayout.addItem(spacerItem)
        self.regression_predict_vlayout.addLayout(self.regression_predict_choosedata_hlayout)
        # create a layout for choosing which model to use
        self.regression_predict_choosemodel_hlayout = QtWidgets.QHBoxLayout()
        self.regression_predict_choosemodel_label = QtWidgets.QLabel(self.regression_predict)
        self.regression_predict_choosemodel_label.setObjectName("regression_predict_choosemodel_label")
        self.regression_predict_choosemodel_hlayout.addWidget(self.regression_predict_choosemodel_label)
        # create the combobox with model choices

        modelchoices = self.pysat_fun.modelkeys
        if modelchoices == []:
            modelchoices = ['No model has been trained!']
        self.regression_predict_choosemodel = make_combobox(modelchoices)
        self.regression_predict_choosemodel.setObjectName("regression_predict_choosemodel")
        self.regression_predict_choosemodel_hlayout.addWidget(self.regression_predict_choosemodel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_predict_choosemodel_hlayout.addItem(spacerItem1)
        self.regression_predict_vlayout.addLayout(self.regression_predict_choosemodel_hlayout)

        self.regression_predict.setObjectName("regression_predict")
        self.module_layout.addWidget(self.regression_predict)
        self.regression_predict.raise_()
        self.regression_predict.setTitle(("Regression - Predict"))
        self.regression_predict_choosedata_label.setText("Choose data: ")
        self.regression_predict_choosemodel_label.setText("Choose Model: ")
