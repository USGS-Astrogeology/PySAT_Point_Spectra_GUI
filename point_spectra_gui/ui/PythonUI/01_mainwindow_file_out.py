# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rbanderson\Documents\Projects\LIBS PDART\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\01_mainwindow_file_out.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 843)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 561, 721))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaWidgetContents_2.setFont(font)
        self.scrollAreaWidgetContents_2.setStyleSheet("QGroupBox {\n"
"                                    border: 2px solid gray;\n"
"                                    border-radius: 6px;\n"
"                                    margin-top: 0.5em;\n"
"                                    }\n"
"\n"
"                                    QGroupBox::title {\n"
"\n"
"                                    padding-top: -14px;\n"
"                                    padding-left: 8px;\n"
"                                    }\n"
"                                ")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.file_out_path = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_out_path.setFont(font)
        self.file_out_path.setObjectName("file_out_path")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.file_out_path)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_out_path_label = QtWidgets.QLabel(self.file_out_path)
        self.file_out_path_label.setObjectName("file_out_path_label")
        self.horizontalLayout.addWidget(self.file_out_path_label)
        self.file_out_path_line_edit = QtWidgets.QLineEdit(self.file_out_path)
        self.file_out_path_line_edit.setReadOnly(True)
        self.file_out_path_line_edit.setObjectName("file_out_path_line_edit")
        self.horizontalLayout.addWidget(self.file_out_path_line_edit)
        self.file_out_path_button = QtWidgets.QToolButton(self.file_out_path)
        self.file_out_path_button.setObjectName("file_out_path_button")
        self.horizontalLayout.addWidget(self.file_out_path_button)
        self.verticalLayout_8.addWidget(self.file_out_path)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.OK = QtWidgets.QGroupBox(self.centralWidget)
        self.OK.setObjectName("OK")
        self.ok = QtWidgets.QHBoxLayout(self.OK)
        self.ok.setContentsMargins(11, 11, 11, 11)
        self.ok.setSpacing(6)
        self.ok.setObjectName("ok")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(self.OK)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.okButton.setFont(font)
        self.okButton.setMouseTracking(False)
        self.okButton.setObjectName("okButton")
        self.ok.addWidget(self.okButton)
        self.verticalLayout_9.addWidget(self.OK)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreprocessing = QtWidgets.QMenu(self.menuBar)
        self.menuPreprocessing.setObjectName("menuPreprocessing")
        self.menuBaseline_Removal = QtWidgets.QMenu(self.menuPreprocessing)
        self.menuBaseline_Removal.setObjectName("menuBaseline_Removal")
        self.menuCalibration_Transfer = QtWidgets.QMenu(self.menuPreprocessing)
        self.menuCalibration_Transfer.setObjectName("menuCalibration_Transfer")
        self.menuRegression = QtWidgets.QMenu(self.menuBar)
        self.menuRegression.setObjectName("menuRegression")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuClassification = QtWidgets.QMenu(self.menuBar)
        self.menuClassification.setObjectName("menuClassification")
        self.menuSupervised = QtWidgets.QMenu(self.menuClassification)
        self.menuSupervised.setObjectName("menuSupervised")
        self.menuClustering = QtWidgets.QMenu(self.menuClassification)
        self.menuClustering.setObjectName("menuClustering")
        self.menuVisualization = QtWidgets.QMenu(self.menuBar)
        self.menuVisualization.setObjectName("menuVisualization")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLoad_Refence_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Refence_Data.setObjectName("actionLoad_Refence_Data")
        self.actionLoad_Unknown_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Unknown_Data.setObjectName("actionLoad_Unknown_Data")
        self.actionSave_Current_Workflow = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName("actionSave_Current_Workflow")
        self.actionSave_Current_Plots = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Plots.setObjectName("actionSave_Current_Plots")
        self.actionSave_Current_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName("actionSave_Current_Data")
        self.actionCreate_New_Workflow = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName("actionCreate_New_Workflow")
        self.actionNoise_Reduction = QtWidgets.QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName("actionNoise_Reduction")
        self.actionApply_Mask = QtWidgets.QAction(MainWindow)
        self.actionApply_Mask.setObjectName("actionApply_Mask")
        self.actionInterpolate = QtWidgets.QAction(MainWindow)
        self.actionInterpolate.setObjectName("actionInterpolate")
        self.actionInstrument_Response = QtWidgets.QAction(MainWindow)
        self.actionInstrument_Response.setObjectName("actionInstrument_Response")
        self.actionALS = QtWidgets.QAction(MainWindow)
        self.actionALS.setObjectName("actionALS")
        self.actionDietrich = QtWidgets.QAction(MainWindow)
        self.actionDietrich.setObjectName("actionDietrich")
        self.actionPolyFit = QtWidgets.QAction(MainWindow)
        self.actionPolyFit.setObjectName("actionPolyFit")
        self.actionAirPLS = QtWidgets.QAction(MainWindow)
        self.actionAirPLS.setObjectName("actionAirPLS")
        self.actionFABC = QtWidgets.QAction(MainWindow)
        self.actionFABC.setObjectName("actionFABC")
        self.actionKK = QtWidgets.QAction(MainWindow)
        self.actionKK.setObjectName("actionKK")
        self.actionMario = QtWidgets.QAction(MainWindow)
        self.actionMario.setObjectName("actionMario")
        self.actionMedian = QtWidgets.QAction(MainWindow)
        self.actionMedian.setObjectName("actionMedian")
        self.actionRubberband = QtWidgets.QAction(MainWindow)
        self.actionRubberband.setObjectName("actionRubberband")
        self.actionUndecimated_Wavelet = QtWidgets.QAction(MainWindow)
        self.actionUndecimated_Wavelet.setObjectName("actionUndecimated_Wavelet")
        self.actionRatio = QtWidgets.QAction(MainWindow)
        self.actionRatio.setObjectName("actionRatio")
        self.actionTommy_s_Methgod = QtWidgets.QAction(MainWindow)
        self.actionTommy_s_Methgod.setObjectName("actionTommy_s_Methgod")
        self.actionPiecewise_Direct_Standardization = QtWidgets.QAction(MainWindow)
        self.actionPiecewise_Direct_Standardization.setObjectName("actionPiecewise_Direct_Standardization")
        self.actionPCA = QtWidgets.QAction(MainWindow)
        self.actionPCA.setObjectName("actionPCA")
        self.actionICA = QtWidgets.QAction(MainWindow)
        self.actionICA.setObjectName("actionICA")
        self.actionK_Means = QtWidgets.QAction(MainWindow)
        self.actionK_Means.setObjectName("actionK_Means")
        self.actionHierarchical = QtWidgets.QAction(MainWindow)
        self.actionHierarchical.setObjectName("actionHierarchical")
        self.actionOthers = QtWidgets.QAction(MainWindow)
        self.actionOthers.setObjectName("actionOthers")
        self.actionOthers_2 = QtWidgets.QAction(MainWindow)
        self.actionOthers_2.setObjectName("actionOthers_2")
        self.actionOthers_3 = QtWidgets.QAction(MainWindow)
        self.actionOthers_3.setObjectName("actionOthers_3")
        self.actionPLS = QtWidgets.QAction(MainWindow)
        self.actionPLS.setObjectName("actionPLS")
        self.actionSM_PLS = QtWidgets.QAction(MainWindow)
        self.actionSM_PLS.setObjectName("actionSM_PLS")
        self.actionICA_Regression = QtWidgets.QAction(MainWindow)
        self.actionICA_Regression.setObjectName("actionICA_Regression")
        self.actionGaussian_Process = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Process.setObjectName("actionGaussian_Process")
        self.actionMLP = QtWidgets.QAction(MainWindow)
        self.actionMLP.setObjectName("actionMLP")
        self.actionSVM = QtWidgets.QAction(MainWindow)
        self.actionSVM.setObjectName("actionSVM")
        self.actionOthers_4 = QtWidgets.QAction(MainWindow)
        self.actionOthers_4.setObjectName("actionOthers_4")
        self.actionOthers_5 = QtWidgets.QAction(MainWindow)
        self.actionOthers_5.setObjectName("actionOthers_5")
        self.actionIndex = QtWidgets.QAction(MainWindow)
        self.actionIndex.setObjectName("actionIndex")
        self.actionContent_2 = QtWidgets.QAction(MainWindow)
        self.actionContent_2.setObjectName("actionContent_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_QtCreator = QtWidgets.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName("actionAbout_QtCreator")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNormalization = QtWidgets.QAction(MainWindow)
        self.actionNormalization.setObjectName("actionNormalization")
        self.actionICA_2 = QtWidgets.QAction(MainWindow)
        self.actionICA_2.setObjectName("actionICA_2")
        self.actionPCA_2 = QtWidgets.QAction(MainWindow)
        self.actionPCA_2.setObjectName("actionPCA_2")
        self.actionPLS_DA = QtWidgets.QAction(MainWindow)
        self.actionPLS_DA.setObjectName("actionPLS_DA")
        self.actionSIMCA = QtWidgets.QAction(MainWindow)
        self.actionSIMCA.setObjectName("actionSIMCA")
        self.actionK_means = QtWidgets.QAction(MainWindow)
        self.actionK_means.setObjectName("actionK_means")
        self.actionHierarchical_2 = QtWidgets.QAction(MainWindow)
        self.actionHierarchical_2.setObjectName("actionHierarchical_2")
        self.actionCross_Validation = QtWidgets.QAction(MainWindow)
        self.actionCross_Validation.setObjectName("actionCross_Validation")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionLine_Plot = QtWidgets.QAction(MainWindow)
        self.actionLine_Plot.setObjectName("actionLine_Plot")
        self.action1_to_1_Plot = QtWidgets.QAction(MainWindow)
        self.action1_to_1_Plot.setObjectName("action1_to_1_Plot")
        self.actionScatter_Plot = QtWidgets.QAction(MainWindow)
        self.actionScatter_Plot.setObjectName("actionScatter_Plot")
        self.actionSet_output_location = QtWidgets.QAction(MainWindow)
        self.actionSet_output_location.setObjectName("actionSet_output_location")
        self.actionCreate_N_Folds = QtWidgets.QAction(MainWindow)
        self.actionCreate_N_Folds.setObjectName("actionCreate_N_Folds")
        self.actionCreate_Test_Folds = QtWidgets.QAction(MainWindow)
        self.actionCreate_Test_Folds.setObjectName("actionCreate_Test_Folds")
        self.actionSubmodel_Ranges = QtWidgets.QAction(MainWindow)
        self.actionSubmodel_Ranges.setObjectName("actionSubmodel_Ranges")
        self.menuFile.addAction(self.actionLoad_Refence_Data)
        self.menuFile.addAction(self.actionLoad_Unknown_Data)
        self.menuFile.addAction(self.actionSet_output_location)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Current_Plots)
        self.menuFile.addAction(self.actionSave_Current_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Workflow)
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
        self.menuPreprocessing.addAction(self.actionInterpolate)
        self.menuPreprocessing.addAction(self.actionInstrument_Response)
        self.menuPreprocessing.addAction(self.menuBaseline_Removal.menuAction())
        self.menuPreprocessing.addAction(self.menuCalibration_Transfer.menuAction())
        self.menuPreprocessing.addAction(self.actionICA_2)
        self.menuPreprocessing.addAction(self.actionPCA_2)
        self.menuRegression.addAction(self.actionCross_Validation)
        self.menuRegression.addAction(self.actionTrain)
        self.menuRegression.addAction(self.actionPredict)
        self.menuRegression.addAction(self.actionCreate_N_Folds)
        self.menuRegression.addAction(self.actionCreate_Test_Folds)
        self.menuRegression.addAction(self.actionSubmodel_Ranges)
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
        self.menuVisualization.addAction(self.actionLine_Plot)
        self.menuVisualization.addAction(self.action1_to_1_Plot)
        self.menuVisualization.addAction(self.actionScatter_Plot)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPreprocessing.menuAction())
        self.menuBar.addAction(self.menuClassification.menuAction())
        self.menuBar.addAction(self.menuRegression.menuAction())
        self.menuBar.addAction(self.menuVisualization.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT"))
        self.file_out_path.setTitle(_translate("MainWindow", "Ouput Folder"))
        self.file_out_path_label.setText(_translate("MainWindow", "Folder Name"))
        self.file_out_path_line_edit.setText(_translate("MainWindow", "\n"
"                                                            */\n"
"                                                        "))
        self.file_out_path_button.setText(_translate("MainWindow", "..."))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPreprocessing.setTitle(_translate("MainWindow", "Preprocessing"))
        self.menuBaseline_Removal.setTitle(_translate("MainWindow", "Baseline Removal"))
        self.menuCalibration_Transfer.setTitle(_translate("MainWindow", "Calibration Transfer"))
        self.menuRegression.setTitle(_translate("MainWindow", "Regression"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuClassification.setTitle(_translate("MainWindow", "Classification"))
        self.menuSupervised.setTitle(_translate("MainWindow", "Supervised"))
        self.menuClustering.setTitle(_translate("MainWindow", "Clustering"))
        self.menuVisualization.setTitle(_translate("MainWindow", "Visualization"))
        self.actionLoad_Refence_Data.setText(_translate("MainWindow", "Load Refence Data"))
        self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data"))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow"))
        self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots"))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data"))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow"))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction"))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask"))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate (unknown to known)"))
        self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response"))
        self.actionALS.setText(_translate("MainWindow", "ALS"))
        self.actionDietrich.setText(_translate("MainWindow", "Dietrich"))
        self.actionPolyFit.setText(_translate("MainWindow", "PolyFit"))
        self.actionAirPLS.setText(_translate("MainWindow", "AirPLS"))
        self.actionFABC.setText(_translate("MainWindow", "FABC"))
        self.actionKK.setText(_translate("MainWindow", "KK"))
        self.actionMario.setText(_translate("MainWindow", "Mario"))
        self.actionMedian.setText(_translate("MainWindow", "Median"))
        self.actionRubberband.setText(_translate("MainWindow", "Rubberband"))
        self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet"))
        self.actionRatio.setText(_translate("MainWindow", "Ratio"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))
        self.actionPiecewise_Direct_Standardization.setText(_translate("MainWindow", "Piecewise Direct Standardization"))
        self.actionPCA.setText(_translate("MainWindow", "PCA"))
        self.actionICA.setText(_translate("MainWindow", "ICA"))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means"))
        self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical"))
        self.actionOthers.setText(_translate("MainWindow", "Others..."))
        self.actionOthers_2.setText(_translate("MainWindow", "Others..."))
        self.actionOthers_3.setText(_translate("MainWindow", "Others..."))
        self.actionPLS.setText(_translate("MainWindow", "PLS"))
        self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS"))
        self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression"))
        self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process"))
        self.actionMLP.setText(_translate("MainWindow", "MLP"))
        self.actionSVM.setText(_translate("MainWindow", "SVM"))
        self.actionOthers_4.setText(_translate("MainWindow", "Others..."))
        self.actionOthers_5.setText(_translate("MainWindow", "Others..."))
        self.actionIndex.setText(_translate("MainWindow", "Index"))
        self.actionContent_2.setText(_translate("MainWindow", "Content"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionAbout_QtCreator.setText(_translate("MainWindow", "About Qt..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization"))
        self.actionICA_2.setText(_translate("MainWindow", "ICA"))
        self.actionPCA_2.setText(_translate("MainWindow", "PCA"))
        self.actionPLS_DA.setText(_translate("MainWindow", "PLS-DA"))
        self.actionSIMCA.setText(_translate("MainWindow", "SIMCA"))
        self.actionK_means.setText(_translate("MainWindow", "K-means"))
        self.actionHierarchical_2.setText(_translate("MainWindow", "Hierarchical"))
        self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation"))
        self.actionTrain.setText(_translate("MainWindow", "Train"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
        self.actionLine_Plot.setText(_translate("MainWindow", "Line Plot"))
        self.action1_to_1_Plot.setText(_translate("MainWindow", "1 to 1 Plot"))
        self.actionScatter_Plot.setText(_translate("MainWindow", "Scatter Plot"))
        self.actionSet_output_location.setText(_translate("MainWindow", "Output Location"))
        self.actionCreate_N_Folds.setText(_translate("MainWindow", "Create N Folds"))
        self.actionCreate_Test_Folds.setText(_translate("MainWindow", "Create Test Folds"))
        self.actionSubmodel_Ranges.setText(_translate("MainWindow", "Submodel Ranges"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

