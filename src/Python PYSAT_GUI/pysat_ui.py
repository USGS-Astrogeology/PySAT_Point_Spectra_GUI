from PyQt4 import QtCore, QtGui
from pysat_func import pysat_func
import PYSAT_UI_MODULES
import pickle

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class pysat_ui(object):
    def __init__(self):
        self.pysat_fun = pysat_func()
        self.ui_list = []
        self.restore_list = None
        self.flag = False
        self.restore_flag = False

    """ =============================================
    This is the backbone of the UI, without this portion we have nothing to work with
    ============================================== """

    def main_window(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 1000)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_9.setMargin(11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 557, 800))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaWidgetContents_2.setFont(font)
        self.scrollAreaWidgetContents_2.setStyleSheet(_fromUtf8("QGroupBox {\n"
                                                                "  border: 2px solid gray;\n"
                                                                "  border-radius: 6px;\n"
                                                                "  margin-top: 0.5em;\n"
                                                                "}\n"
                                                                "\n"
                                                                "QGroupBox::title {\n"
                                                                "\n"
                                                                "  padding-top: -14px;\n"
                                                                "  padding-left: 8px;\n"
                                                                "}\n"
                                                                ""))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setMargin(11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.OK = QtGui.QGroupBox(self.centralWidget)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.ok = QtGui.QHBoxLayout(self.OK)
        self.ok.setMargin(11)
        self.ok.setSpacing(6)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.progressBar = QtGui.QProgressBar(self.OK)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.ok.addWidget(self.progressBar)
        self.delButton = QtGui.QPushButton(self.OK)
        self.okButton = QtGui.QPushButton(self.OK)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.delButton.setFont(font)
        self.delButton.setMouseTracking(False)
        self.delButton.setObjectName("delButton")
        self.ok.addWidget(self.delButton)
        self.okButton.setFont(font)
        self.okButton.setMouseTracking(False)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.ok.addWidget(self.okButton)
        self.verticalLayout_9.addWidget(self.OK)



        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuPreprocessing = QtGui.QMenu(self.menuBar)
        self.menuPreprocessing.setObjectName(_fromUtf8("menuPreprocessing"))
        self.menuBaseline_Removal = QtGui.QMenu(self.menuPreprocessing)
        self.menuBaseline_Removal.setObjectName(_fromUtf8("menuBaseline_Removal"))
        self.menuCalibration_Transfer = QtGui.QMenu(self.menuPreprocessing)
        self.menuCalibration_Transfer.setObjectName(_fromUtf8("menuCalibration_Transfer"))
        self.menuRegression = QtGui.QMenu(self.menuBar)
        self.menuRegression.setObjectName(_fromUtf8("menuRegression"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuClassification = QtGui.QMenu(self.menuBar)
        self.menuClassification.setObjectName(_fromUtf8("menuClassification"))
        self.menuSupervised = QtGui.QMenu(self.menuClassification)
        self.menuSupervised.setObjectName(_fromUtf8("menuSupervised"))
        self.menuClustering = QtGui.QMenu(self.menuClassification)
        self.menuClustering.setObjectName(_fromUtf8("menuClustering"))
        self.menuVisualization = QtGui.QMenu(self.menuBar)
        self.menuVisualization.setObjectName(_fromUtf8("menuVisualization"))
        MainWindow.setMenuBar(self.menuBar)

        self.actionLoad_reference_Data = QtGui.QAction(MainWindow)
        self.actionLoad_reference_Data.setObjectName(_fromUtf8("actionLoad_reference_Data"))
        self.actionLoad_Unknown_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Unknown_Data.setObjectName(_fromUtf8("actionLoad_Unknown_Data"))
        self.actionSave_Current_Workflow = QtGui.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName(_fromUtf8("actionSave_Current_Workflow"))
        self.actionSave_Current_Plots = QtGui.QAction(MainWindow)
        self.actionSave_Current_Plots.setObjectName(_fromUtf8("actionSave_Current_Plots"))
        self.actionSave_Current_Data = QtGui.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName(_fromUtf8("actionSave_Current_Data"))
        self.actionCreate_New_Workflow = QtGui.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName(_fromUtf8("actionCreate_New_Workflow"))
        self.actionOpen_Workflow = QtGui.QAction(MainWindow)
        self.actionOpen_Workflow.setObjectName(_fromUtf8("actionOpen_Workflow"))
        self.actionNoise_Reduction = QtGui.QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName(_fromUtf8("actionNoise_Reduction"))
        self.actionRemoveNull = QtGui.QAction(MainWindow)
        self.actionRemoveNull.setObjectName(_fromUtf8("actionRemoveNull"))

        self.actionApply_Mask = QtGui.QAction(MainWindow)
        self.actionApply_Mask.setObjectName(_fromUtf8("actionApply_Mask"))
        self.actionInterpolate = QtGui.QAction(MainWindow)
        self.actionInterpolate.setObjectName(_fromUtf8("actionInterpolate"))
        self.actionInstrument_Response = QtGui.QAction(MainWindow)
        self.actionInstrument_Response.setObjectName(_fromUtf8("actionInstrument_Response"))
        self.actionALS = QtGui.QAction(MainWindow)
        self.actionALS.setObjectName(_fromUtf8("actionALS"))
        self.actionDietrich = QtGui.QAction(MainWindow)
        self.actionDietrich.setObjectName(_fromUtf8("actionDietrich"))
        self.actionPolyFit = QtGui.QAction(MainWindow)
        self.actionPolyFit.setObjectName(_fromUtf8("actionPolyFit"))
        self.actionAirPLS = QtGui.QAction(MainWindow)
        self.actionAirPLS.setObjectName(_fromUtf8("actionAirPLS"))
        self.actionFABC = QtGui.QAction(MainWindow)
        self.actionFABC.setObjectName(_fromUtf8("actionFABC"))
        self.actionKK = QtGui.QAction(MainWindow)
        self.actionKK.setObjectName(_fromUtf8("actionKK"))
        self.actionMario = QtGui.QAction(MainWindow)
        self.actionMario.setObjectName(_fromUtf8("actionMario"))
        self.actionMedian = QtGui.QAction(MainWindow)
        self.actionMedian.setObjectName(_fromUtf8("actionMedian"))
        self.actionRubberband = QtGui.QAction(MainWindow)
        self.actionRubberband.setObjectName(_fromUtf8("actionRubberband"))
        self.actionUndecimated_Wavelet = QtGui.QAction(MainWindow)
        self.actionUndecimated_Wavelet.setObjectName(_fromUtf8("actionUndecimated_Wavelet"))
        self.actionRatio = QtGui.QAction(MainWindow)
        self.actionRatio.setObjectName(_fromUtf8("actionRatio"))
        self.actionTommy_s_Methgod = QtGui.QAction(MainWindow)
        self.actionTommy_s_Methgod.setObjectName(_fromUtf8("actionTommy_s_Methgod"))
        self.actionPiecewise_Direct_Standardization = QtGui.QAction(MainWindow)
        self.actionPiecewise_Direct_Standardization.setObjectName(
            _fromUtf8("actionPiecewise_Direct_Standardization"))
        self.actionPCA = QtGui.QAction(MainWindow)
        self.actionPCA.setObjectName(_fromUtf8("actionPCA"))
        self.actionICA = QtGui.QAction(MainWindow)
        self.actionICA.setObjectName(_fromUtf8("actionICA"))
        self.actionK_Means = QtGui.QAction(MainWindow)
        self.actionK_Means.setObjectName(_fromUtf8("actionK_Means"))
        self.actionHierarchical = QtGui.QAction(MainWindow)
        self.actionHierarchical.setObjectName(_fromUtf8("actionHierarchical"))
        self.actionOthers = QtGui.QAction(MainWindow)
        self.actionOthers.setObjectName(_fromUtf8("actionOthers"))
        self.actionOthers_2 = QtGui.QAction(MainWindow)
        self.actionOthers_2.setObjectName(_fromUtf8("actionOthers_2"))
        self.actionOthers_3 = QtGui.QAction(MainWindow)
        self.actionOthers_3.setObjectName(_fromUtf8("actionOthers_3"))
        self.actionPLS = QtGui.QAction(MainWindow)
        self.actionPLS.setObjectName(_fromUtf8("actionPLS"))
        self.actionSM_PLS = QtGui.QAction(MainWindow)
        self.actionSM_PLS.setObjectName(_fromUtf8("actionSM_PLS"))
        self.actionICA_Regression = QtGui.QAction(MainWindow)
        self.actionICA_Regression.setObjectName(_fromUtf8("actionICA_Regression"))
        self.actionGaussian_Process = QtGui.QAction(MainWindow)
        self.actionGaussian_Process.setObjectName(_fromUtf8("actionGaussian_Process"))
        self.actionMLP = QtGui.QAction(MainWindow)
        self.actionMLP.setObjectName(_fromUtf8("actionMLP"))
        self.actionSVM = QtGui.QAction(MainWindow)
        self.actionSVM.setObjectName(_fromUtf8("actionSVM"))
        self.actionOthers_4 = QtGui.QAction(MainWindow)
        self.actionOthers_4.setObjectName(_fromUtf8("actionOthers_4"))
        self.actionOthers_5 = QtGui.QAction(MainWindow)
        self.actionOthers_5.setObjectName(_fromUtf8("actionOthers_5"))
        self.actionIndex = QtGui.QAction(MainWindow)
        self.actionIndex.setObjectName(_fromUtf8("actionIndex"))
        self.actionContent_2 = QtGui.QAction(MainWindow)
        self.actionContent_2.setObjectName(_fromUtf8("actionContent_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_QtCreator = QtGui.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName(_fromUtf8("actionAbout_QtCreator"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNormalization = QtGui.QAction(MainWindow)
        self.actionNormalization.setObjectName(_fromUtf8("actionNormalization"))
        self.actionDimRed=QtGui.QAction(MainWindow)
        self.actionDimRed.setObjectName(_fromUtf8("actionDimRed"))
        self.actionICA_2 = QtGui.QAction(MainWindow)
        self.actionICA_2.setObjectName(_fromUtf8("actionICA_2"))
        self.actionPCA_2 = QtGui.QAction(MainWindow)
        self.actionPCA_2.setObjectName(_fromUtf8("actionPCA_2"))
        self.actionPLS_DA = QtGui.QAction(MainWindow)
        self.actionPLS_DA.setObjectName(_fromUtf8("actionPLS_DA"))
        self.actionSIMCA = QtGui.QAction(MainWindow)
        self.actionSIMCA.setObjectName(_fromUtf8("actionSIMCA"))
        self.actionK_means = QtGui.QAction(MainWindow)
        self.actionK_means.setObjectName(_fromUtf8("actionK_means"))
        self.actionHierarchical_2 = QtGui.QAction(MainWindow)
        self.actionHierarchical_2.setObjectName(_fromUtf8("actionHierarchical_2"))
        self.actionCross_Validation = QtGui.QAction(MainWindow)
        self.actionCross_Validation.setObjectName(_fromUtf8("actionCross_Validation"))
        self.actionTrain = QtGui.QAction(MainWindow)
        self.actionTrain.setObjectName(_fromUtf8("actionTrain"))
        self.actionPredict = QtGui.QAction(MainWindow)
        self.actionPredict.setObjectName(_fromUtf8("actionPredict"))
        self.actionPlot = QtGui.QAction(MainWindow)
        self.actionPlot.setObjectName(_fromUtf8("actionPlot"))
        self.actionPlotDimRed = QtGui.QAction(MainWindow)
        self.actionPlotDimRed.setObjectName(_fromUtf8("actionPlot"))

        self.actionSet_output_location = QtGui.QAction(MainWindow)
        self.actionSet_output_location.setObjectName(_fromUtf8("actionSet_output_location"))
        self.actionCreate_N_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_N_Folds.setObjectName(_fromUtf8("actionCreate_N_Folds"))
        self.actionCreate_Test_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_Test_Folds.setObjectName(_fromUtf8("actionCreate_Test_Folds"))
        self.actionStratified_Folds = QtGui.QAction(MainWindow)
        self.actionStratified_Folds.setObjectName(_fromUtf8("actionStratified_Folds"))
        self.actionTrain_Submodels = QtGui.QAction(MainWindow)
        self.actionTrain_Submodels.setObjectName(_fromUtf8("actionTrain_Submodels"))
        self.actionSubmodelPredict = QtGui.QAction(MainWindow)
        self.actionSubmodelPredict.setObjectName(_fromUtf8("actionSubmodelPredict"))
        self.menuFile.addAction(self.actionLoad_reference_Data)
        self.menuFile.addAction(self.actionLoad_Unknown_Data)
        self.menuFile.addAction(self.actionSet_output_location)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Current_Plots)
        self.menuFile.addAction(self.actionSave_Current_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Workflow)
        self.menuFile.addAction(self.actionOpen_Workflow)
        self.menuFile.addAction(self.actionSave_Current_Workflow)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBaseline_Removal.addAction(self.actionALS)
        self.menuBaseline_Removal.addAction(self.actionDietrich)
        self.menuBaseline_Removal.addAction(self.actionPolyFit)
        self.menuBaseline_Removal.addAction(self.actionAirPLS)
        self.menuBaseline_Removal.addAction(self.actionFABC)
        self.menuBaseline_Removal.addAction(self.actionKK)
        self.menuBaseline_Removal.addAction(self.actionMario)
        self.menuBaseline_Removal.addAction(self.actionMedian)
        self.menuBaseline_Removal.addAction(self.actionRubberband)
        self.menuBaseline_Removal.addAction(self.actionUndecimated_Wavelet)
        self.menuCalibration_Transfer.addAction(self.actionRatio)
        self.menuCalibration_Transfer.addAction(self.actionTommy_s_Methgod)
        self.menuCalibration_Transfer.addAction(self.actionPiecewise_Direct_Standardization)
        self.menuCalibration_Transfer.addAction(self.actionOthers_3)
        self.menuPreprocessing.addAction(self.actionNormalization)
        self.menuPreprocessing.addAction(self.actionNoise_Reduction)
        self.menuPreprocessing.addAction(self.actionApply_Mask)
        self.menuPreprocessing.addAction(self.actionRemoveNull)
        self.menuPreprocessing.addAction(self.actionInterpolate)
        self.menuPreprocessing.addAction(self.actionInstrument_Response)
        self.menuPreprocessing.addAction(self.menuBaseline_Removal.menuAction())
        self.menuPreprocessing.addAction(self.menuCalibration_Transfer.menuAction())
        self.menuPreprocessing.addAction(self.actionICA_2)
        self.menuPreprocessing.addAction(self.actionPCA_2)
        self.menuPreprocessing.addAction(self.actionDimRed)
        self.menuPreprocessing.addAction(self.actionStratified_Folds)
        self.menuRegression.addAction(self.actionCross_Validation)
        self.menuRegression.addAction(self.actionTrain)
        self.menuRegression.addAction(self.actionSubmodelPredict)
        # self.menuRegression.addAction(self.actionTrain_Submodels)
        self.menuRegression.addAction(self.actionPredict)
        self.menuHelp.addAction(self.actionIndex)
        self.menuHelp.addAction(self.actionContent_2)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_QtCreator)
        self.menuSupervised.addAction(self.actionPLS_DA)
        self.menuSupervised.addAction(self.actionSIMCA)
        self.menuClustering.addAction(self.actionK_means)
        self.menuClustering.addAction(self.actionHierarchical_2)
        self.menuClassification.addAction(self.menuSupervised.menuAction())
        self.menuClassification.addAction(self.menuClustering.menuAction())
        self.menuVisualization.addAction(self.actionPlot)
        self.menuVisualization.addAction(self.actionPlotDimRed)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPreprocessing.menuAction())
        self.menuBar.addAction(self.menuClassification.menuAction())
        self.menuBar.addAction(self.menuRegression.menuAction())
        self.menuBar.addAction(self.menuVisualization.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT", None))
        self.okButton.setText(_translate("MainWindow", "OK", None))
        self.delButton.setText(_translate("MainWindow", "Delete Module", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuPreprocessing.setTitle(_translate("MainWindow", "Preprocessing", None))
        self.menuBaseline_Removal.setTitle(_translate("MainWindow", "Baseline Removal", None))
        self.menuCalibration_Transfer.setTitle(_translate("MainWindow", "Calibration Transfer", None))
        self.menuRegression.setTitle(_translate("MainWindow", "Regression", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuClassification.setTitle(_translate("MainWindow", "Classification", None))
        self.menuSupervised.setTitle(_translate("MainWindow", "Supervised", None))
        self.menuClustering.setTitle(_translate("MainWindow", "Clustering", None))
        self.menuVisualization.setTitle(_translate("MainWindow", "Visualization", None))
        self.actionLoad_reference_Data.setText(_translate("MainWindow", "Load Reference Data", None))
        self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data", None))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow", None))
        self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots", None))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data", None))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow", None))
        self.actionOpen_Workflow.setText(_translate("MainWindow", "Open Workflow", None))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction", None))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask", None))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate", None))
        self.actionRemoveNull.setText(_translate("MainWindow", "Remove Null Data", None))
        self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response", None))
        self.actionALS.setText(_translate("MainWindow", "ALS", None))
        self.actionDietrich.setText(_translate("MainWindow", "Dietrich", None))
        self.actionPolyFit.setText(_translate("MainWindow", "PolyFit", None))
        self.actionAirPLS.setText(_translate("MainWindow", "AirPLS", None))
        self.actionFABC.setText(_translate("MainWindow", "FABC", None))
        self.actionKK.setText(_translate("MainWindow", "KK", None))
        self.actionMario.setText(_translate("MainWindow", "Mario", None))
        self.actionMedian.setText(_translate("MainWindow", "Median", None))
        self.actionRubberband.setText(_translate("MainWindow", "Rubberband", None))
        self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet", None))
        self.actionRatio.setText(_translate("MainWindow", "Ratio", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))
        self.actionPiecewise_Direct_Standardization.setText(
            _translate("MainWindow", "Piecewise Direct Standardization", None))
        self.actionPCA.setText(_translate("MainWindow", "PCA", None))
        self.actionICA.setText(_translate("MainWindow", "ICA", None))
        self.actionDimRed.setText((_translate("MainWindow","Dimensionality Reduction",None)))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means", None))
        self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionOthers.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_2.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_3.setText(_translate("MainWindow", "Others...", None))
        self.actionPLS.setText(_translate("MainWindow", "PLS", None))
        self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS", None))
        self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression", None))
        self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process", None))
        self.actionMLP.setText(_translate("MainWindow", "MLP", None))
        self.actionSVM.setText(_translate("MainWindow", "SVM", None))
        self.actionOthers_4.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_5.setText(_translate("MainWindow", "Others...", None))
        self.actionIndex.setText(_translate("MainWindow", "Index", None))
        self.actionContent_2.setText(_translate("MainWindow", "Content", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionAbout_QtCreator.setText(_translate("MainWindow", "About Qt...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization", None))
        self.actionICA_2.setText(_translate("MainWindow", "ICA", None))
        self.actionPCA_2.setText(_translate("MainWindow", "PCA", None))
        self.actionPLS_DA.setText(_translate("MainWindow", "PLS-DA", None))
        self.actionSIMCA.setText(_translate("MainWindow", "SIMCA", None))
        self.actionK_means.setText(_translate("MainWindow", "K-means", None))
        self.actionHierarchical_2.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation", None))
        self.actionTrain.setText(_translate("MainWindow", "Train", None))
        self.actionSubmodelPredict.setText(_translate("MainWindow", "Submodel Predict", None))
        self.actionPredict.setText(_translate("MainWindow", "Predict", None))
        self.actionPlot.setText(_translate("MainWindow", "Plot", None))
        self.actionPlotDimRed.setText(_translate("MainWindow", "Plot ICA/PCA", None))

        self.actionSet_output_location.setText(_translate("MainWindow", "Output Location", None))
        self.actionCreate_N_Folds.setText(_translate("MainWindow", "Create N Folds", None))
        self.actionStratified_Folds.setText(_translate("MainWindow", "Stratified Folds", None))
        self.okButton.clicked.connect(lambda: self.on_okButton_clicked())
        self.delButton.clicked.connect(lambda: self.pysat_fun.del_layout())

    def get_known_data(self, arg_list=None, kw_list=None):
        self.flag = PYSAT_UI_MODULES.get_data_k_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def get_unknown_data(self, arg_list=None, kw_list=None):
        self.flag = PYSAT_UI_MODULES.get_data_u_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_mask(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.get_mask_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def save_data(self):
        self.flag = PYSAT_UI_MODULES.write_data_(self.pysat_fun,self.verticalLayout_8)

    def file_outpath(self, arg_list=None, kw_list=None):
        self.flag = PYSAT_UI_MODULES.file_outpath_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_removenull(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.removenull_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def normalization(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.normalization_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_strat_folds(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.strat_folds_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_dim_red(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.dim_reduction_(self.pysat_fun, self.verticalLayout_8,arg_list,kw_list)

    def do_regression_train(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.regression_train_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_regression_predict(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.regression_predict_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_submodel_predict(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.sm_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_plot(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.plot_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_plot_dim_red(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.dim_red_plot_(self.pysat_fun, self.verticalLayout_8,arg_list,kw_list)

    def do_cv(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.cv_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    def do_interp(self, arg_list=None, kw_list=None):
        PYSAT_UI_MODULES.interpolation_(self.pysat_fun, self.verticalLayout_8, arg_list, kw_list)

    """ =============================================
    Please do not delete the functions below this line!
    These functions are the working functions
    that allow the UI to operate and do work!
    ============================================== """

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionOpen_Workflow.setShortcut("ctrl+O")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")

    def menu_item_functions(self, MainWindow):
        self.actionSet_output_location.triggered.connect(lambda: pysat_ui.file_outpath(self))  # output location
        self.actionLoad_Unknown_Data.triggered.connect(lambda: pysat_ui.get_unknown_data(self))  # unknown data
        self.actionLoad_reference_Data.triggered.connect(lambda: pysat_ui.get_known_data(self))  # known data
        self.actionSave_Current_Data.triggered.connect(lambda: pysat_ui.save_data(self))
        self.actionNormalization.triggered.connect(lambda: pysat_ui.normalization(self))  # submodel
        self.actionApply_Mask.triggered.connect(lambda: pysat_ui.do_mask(self))  # get_mask
        self.actionRemoveNull.triggered.connect(lambda: pysat_ui.do_removenull(self))
        self.actionStratified_Folds.triggered.connect(lambda: pysat_ui.do_strat_folds(self))  # strat folds
        self.actionTrain.triggered.connect(lambda: pysat_ui.do_regression_train(self))  # regression train
        self.actionPredict.triggered.connect(lambda: pysat_ui.do_regression_predict(self))  # regression predict
        self.actionInterpolate.triggered.connect(lambda: pysat_ui.do_interp(self))
        self.actionPlot.triggered.connect(lambda: pysat_ui.do_plot(self))
        self.actionPlotDimRed.triggered.connect(lambda: pysat_ui.do_plot_dim_red(self))
        self.actionCross_Validation.triggered.connect(lambda: pysat_ui.do_cv(self))
        self.actionSubmodelPredict.triggered.connect(lambda:pysat_ui.do_submodel_predict(self))
        self.actionDimRed.triggered.connect(lambda: pysat_ui.do_dim_red(self))
        # Taking out menu items that don't have working UI modules yet. We don't want to delete them, so we'll make them disappear.
        self.actionOpen_Workflow.triggered.connect(lambda: self.on_load_clicked())
        self.actionSave_Current_Workflow.triggered.connect(lambda: self.on_save_clicked())
        self.set_greyed_out_items(True)
        self.set_visible_items()

        # TODO add auto scroll down feature
        # self.scrollArea.findChildren().triggered.connect(self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().value()+10))

        # These are the Restore functions
        #self.actionPredict.triggered.connect(lambda: self.set_ui_list("do_regression_predict"))  # regression predict
        # self.actionPlot.triggered.connect(lambda: self.set_ui_list("do_plot"))
        # self.actionCross_Validation.triggered.connect(lambda: self.set_ui_list("do_cv"))

    def set_greyed_out_items(self, bool):
        self.actionTrain.setDisabled(bool)
        self.actionPredict.setDisabled(bool)
        self.actionNormalization.setDisabled(bool)
        self.actionApply_Mask.setDisabled(bool)
        self.actionStratified_Folds.setDisabled(bool)
        self.actionTrain.setDisabled(bool)
        self.actionPredict.setDisabled(bool)
        self.actionInterpolate.setDisabled(bool)
        self.actionPlot.setDisabled(bool)
        self.actionRemoveNull.setDisabled(bool)
        self.actionCross_Validation.setDisabled(bool)
        self.actionSubmodelPredict.setDisabled(bool)
        self.actionSave_Current_Data.setDisabled(bool)
        self.actionSave_Current_Plots.setDisabled(bool)

    def set_visible_items(self):
        self.actionNoise_Reduction.setVisible(False)
        self.actionInstrument_Response.setVisible(False)
        self.menuBaseline_Removal.deleteLater()
        self.menuCalibration_Transfer.deleteLater()
        self.actionICA.setVisible(False)
        self.actionPCA.setVisible(False)
        self.actionICA_2.setVisible(False)
        self.actionPCA_2.setVisible(False)
        self.menuClassification.setTitle("")

    def handleMenuHovered(self, action):
        QtGui.QToolTip.showText(self, None, action, None)

    def on_okButton_clicked(self):
        if self.flag:
            self.set_greyed_out_items(False)
            self.onStart()
            self.pysat_fun.taskFinished.connect(self.onFinished)

    ################# Restoration toolset below

    def on_save_clicked(self):
        try:
            filename = QtGui.QFileDialog.getSaveFileName(None, "Choose where you want save your file", '.', '(*.wrf)')
            print(filename)
            with open(filename, 'wb') as fp:
                pickle.dump(self.pysat_fun.get_list(), fp)
        except:
            print("File not loaded")

    def on_load_clicked(self):
        filename = QtGui.QFileDialog.getOpenFileName(None, "Open Workflow File", '.', "(*.wrf)")
        print(filename)
        try:
            with open(filename, 'rb') as fp:
                self.restore_list = pickle.load(fp)
        except:
            PYSAT_UI_MODULES.error_print("File was not loaded")
        self.restore_first()

    def restore_first(self):
        # first run a single or double instance of getattr depending on what data is in the queue
        #   We'll need to remember 'i' so we don't accidentally run the instance too many times
        # then press ok
        # then we'll have another loop continue on it's merry way adding everything in.
        try:
            self.r_list = self.restore_list.pop()
            while self.r_list[1] == "get_unknown_data" or self.r_list[1] == "get_known_data":
                getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
                print(self.r_list)
                self.r_list = self.restore_list.pop()
            self.on_okButton_clicked()
            self.pysat_fun.taskFinished.connect(self.restore_rest)
        except Exception as e:
            print(e)

    def restore_rest(self):
        if self.restore_flag is False:
            getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
            for i in range(len(self.restore_list)):
                self.r_list = self.restore_list.pop()
                print(self.r_list)
                getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
            self.restore_flag = True

    ################# Progress bar toolset below

    def onStart(self):  # onStart function
        self.progressBar.setRange(0, 0)  # make the bar pulse green
        self.pysat_fun.start()  # TaskThread.start()
        # This is multithreading thus run() == start()

    def onFinished(self):  # onFinished function
        self.progressBar.setRange(0, 1)  # stop the bar pulsing green
        self.progressBar.setValue(1)  # displays 100% after process is finished.
