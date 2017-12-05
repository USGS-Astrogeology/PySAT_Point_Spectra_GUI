import multiprocessing as mp
import os.path
import pickle
import sys
import time
import warnings

from point_spectra_gui.core.About import About
from point_spectra_gui.util.themes import braceyourself, default

try:
    import qtmodern.styles

    q = True
except:
    q = False
    warnings.warn("You're missing the qtmodern package."
                  "to install it use pip install qtmodern")
import os
import logging
import platform
import traceback
from time import strftime

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSettings

from point_spectra_gui import core, __version__
from point_spectra_gui.ui.MainWindow import Ui_MainWindow
from point_spectra_gui.util import delete
from point_spectra_gui.util.BasicFunctionality import Basics
from point_spectra_gui.util.excepthook import my_exception_hook


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class TitleWindow:
    def __init__(self, mainName):
        self.mainName = mainName
        self.fileName = ''
        self.debugName = ''

    def setMainName(self, name):
        self.mainName = name

    def setFileName(self, name):
        self.fileName = name

    def setDebugName(self, bool):
        if bool:
            self.debugName = "Debug Mode"
        else:
            self.debugName = ''

    def display(self):
        if self.fileName == '' and self.debugName == '':
            return "{}".format(self.mainName)
        elif self.fileName == '':
            return "{} - {}".format(self.mainName, self.debugName)
        elif self.debugName == '':
            return "{} - {}".format(self.mainName, self.fileName)
        else:
            return "{} - {} - {}".format(self.mainName, self.fileName, self.debugName)


class MainWindow(Ui_MainWindow, QtCore.QThread, Basics):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.widgetList = []
        self.leftOff = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)  # Run the basic window UI
        self.MainWindow = MainWindow
        self.MainWindow.closeEvent = self.closeEvent
        self.title = TitleWindow(self.MainWindow.windowTitle())
        self._readAndApplyWindowAttributeSettings()
        self.menu_item_shortcuts()  # set up the shortcuts
        self.connectWidgets()

        # Check the mode for debugging
        if self.settings.value("debug") == 'true':
            self.debug_mode()
        else:
            self.normal_mode()

        # Check the theme for the UI
        if self.settings.value('theme') == 'braceyourself':
            braceyourself(self.MainWindow)

    def normal_mode(self):
        """
        Change the direction of stdout to print to the UI console instead

        :return:
        """
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = sys.__stderr__
        # sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)
        self._mode(self.actionOn, self.actionOff, False)

    def debug_mode(self):
        """
        Change the direction of stdout to print to the original console

        :return:
        """
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = sys.__stderr__
        self._mode(self.actionOff, self.actionOn, True)

    def _mode(self, obj1, obj2, debug):
        """
        Set the UI in debug or non-debug mode
        Save all the settings and grey out the necessary boxes

        :param obj1:
        :param obj2:
        :param debug:
        :return:
        """
        obj1.setDisabled(False)
        obj2.setDisabled(True)
        self.debug = debug
        self.title.setDebugName(debug)
        self.settings.setValue("debug", self.debug)
        self.MainWindow.setWindowTitle(self.title.display())

    def theme(self, name):
        """
        We have 3 themes
        each has a different situation
                   __________________
                 /__               __\ new()   Something to note:
               v    \            v    \ new()  As you can see whenever moving into or out of
        default     braceyourself    qtmodern  qtmodern we will have to start a new session
               \___^             \___^ new()   default and braceyourself can simply change
                \___________________/ new()    there styling on the spot

        :param name:
        :return:
        """
        settings = self.settings.value('theme')
        if name == settings:
            print("This is already your current theme")

        elif name == 'qtmodern':  # User is entering into qtmodern
            self.settings.setValue('theme', name)
            self.new()

        elif settings == 'qtmodern':  # User is leaving qtmodern
            self.settings.setValue('theme', name)
            self.new()

        elif name == 'default':
            self.settings.setValue('theme', name)
            default(self.MainWindow)

        elif name == 'braceyourself':
            self.settings.setValue('theme', name)
            braceyourself(self.MainWindow)
        else:
            print("Something went horribly wrong with your theme, try again?")

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def addWidget(self, obj):
        """
        Organize our widgets using a list
        Each widget is addressed separately due to being in a list

        :param obj:
        :return:
        """
        self.widgetList.append(obj())
        self.widgetList[-1].setupUi(self.centralwidget)
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.widgetLayout.addWidget(self.widgetList[-1].get_widget())
        # this should scroll the view all the way down after adding the new widget.
        scrollbar = self.scrollArea.verticalScrollBar()
        # this should scroll the view all the way down after adding the new widget.
        scrollbar.setValue(scrollbar.maximum())
        pass

    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")
        self.actionClear_Workflow.setShortcut("ctrl+K")
        self.actionCreate_New_Workflow.setShortcut("ctrl+N")
        self.actionRestore_Workflow.setShortcut("ctrl+O")
        self.actionSave_Current_Workflow.setShortcut("ctrl+S")
        self.okPushButton.setShortcut("Ctrl+Return")

    def connectWidgets(self):
        """
        Connect all the widgets associated with the MainWindow UI

        :return:
        """

        try:
            self.actionRead_ChemCam_Data.triggered.connect(
                lambda: self.addWidget(core.ReadChemCamData.ReadChemCamData))
            self.actionRemove_Baseline.triggered.connect(
                lambda: self.addWidget(core.BaselineRemoval.BaselineRemoval))
            self.actionCross_Validation.triggered.connect(
                lambda: self.addWidget(core.CrossValidation.CrossValidation))
            self.actionDimensionality_Reduction.triggered.connect(
                lambda: self.addWidget(core.DimensionalityReduction.DimensionalityReduction))
            self.actionInterpolate.triggered.connect(
                lambda: self.addWidget(core.Interpolation.Interpolation))
            self.actionLoad_Data.triggered.connect(
                lambda: self.addWidget(core.LoadData.LoadData))
            self.actionSave_Current_Data.triggered.connect(
                lambda: self.addWidget(core.WriteToCSV.WriteToCSV))
            self.actionRename_Data.triggered.connect(
                lambda: self.addWidget(core.RenameData.RenameData))
            self.actionApply_Mask.triggered.connect(
                lambda: self.addWidget(core.MaskData.MaskData))
            self.actionMultiply_by_Vector.triggered.connect(
                lambda: self.addWidget(core.MultiplyByVector.MultiplyByVector))
            self.actionNormalization.triggered.connect(
                lambda: self.addWidget(core.Normalization.Normalization))
            self.actionSet_Output_Path.triggered.connect(
                lambda: self.addWidget(core.OutputFolder.OutputFolder))
            self.actionPeak_Areas.triggered.connect(
                lambda: self.addWidget(core.PeakAreas.PeakAreas))
            self.actionPlot.triggered.connect(
                lambda: self.addWidget(core.Plot.Plot))
            self.actionPlot_ICA_PCA.triggered.connect(
                lambda: self.addWidget(core.Plot_ICA_PCA.Plot_ICA_PCA))
            self.actionPlot_Spectra.triggered.connect(
                lambda: self.addWidget(core.PlotSpectra.PlotSpectra))
            self.actionTrain.triggered.connect(
                lambda: self.addWidget(core.RegressionTrain.RegressionTrain))
            self.actionPredict.triggered.connect(
                lambda: self.addWidget(core.RegressionPredict.RegressionPredict))
            self.actionRemove_Rows.triggered.connect(
                lambda: self.addWidget(core.RemoveRows.RemoveRows))
            self.actionSplit_Data.triggered.connect(
                lambda: self.addWidget(core.SplitDataset.SplitDataset))
            self.actionOutlier_Removal.triggered.connect(
                lambda: self.addWidget(core.OutlierRemoval.OutlierRemoval))
            self.actionStratified_Folds.triggered.connect(
                lambda: self.addWidget(core.StratifiedFolds.StratifiedFolds))
            self.actionSubmodel_Predict.triggered.connect(
                lambda: self.addWidget(core.SubmodelPredict.SubmodelPredict))
            self.actionSpectral_Derivative.triggered.connect(
                lambda: self.addWidget(core.SpecDeriv.SpecDeriv))
            self.actionCombine_Data_Sets.triggered.connect(
                lambda: self.addWidget(core.CombineDataSets.CombineDataSets))
            self.actionData_Box.triggered.connect(
                lambda: self.addWidget(core.DataTable.DataTable))
            self.actionAbout.triggered.connect(self.on_About_clicked)
            self.actionQtmodern.triggered.connect(lambda: self.theme('qtmodern'))
            self.actionDefault.triggered.connect(lambda: self.theme('default'))
            self.actionBrace_yourself.triggered.connect(lambda: self.theme('braceyourself'))
            self.actionCreate_New_Workflow.triggered.connect(self.new)
            self.actionClear_Workflow.triggered.connect(self.clear)
            self.actionSave_Current_Workflow.triggered.connect(self.on_save_clicked)
            self.actionRestore_Workflow.triggered.connect(self.on_restore_clicked)
            self.deleteModulePushButton.clicked.connect(self.on_delete_module_clicked)
            self.okPushButton.clicked.connect(self.on_okButton_clicked)
            self.undoModulePushButton.clicked.connect(self.on_Rerun_Button_clicked)
            self.stopPushButton.clicked.connect(self.on_stopButton_clicked)
            self.actionOn.triggered.connect(self.debug_mode)
            self.actionOff.triggered.connect(self.normal_mode)
            self.actionExit.triggered.connect(self.MainWindow.close)

        except Exception as e:
            print(e)

    def closeEvent(self, event):
        """
        Write window size and position to config file
        """
        self._writeWindowAttributeSettings()
        event.accept()

    def getWidgetItems(self):
        """
        This function iterates through widgetList
        gets the name of all the fuctions
        and then all of the parameters in the UI
        and write it to a list to be returned

        Iterate through widgetList
        get the names of core, add it to a temp l
        add f list to be the first item in ui_items
        """
        f = []
        ui_items = []
        for f_items in self.widgetList:
            f.append(type(f_items).__name__)
        ui_items.append(f)

        for dat in self.widgetList:
            ui_items.append(dat.getGuiParams())
        return ui_items

    def setWidgetItems(self, dict):
        """
        This function iterates through a `dict`
        and restores the UI

        :param dict:
        :return:
        """
        for f_items in dict[0]:
            """
            Really complex way of running essentially this:
            `self.addWidget(core.SplitDataset.SplitDataset))`
            Part of the reason why we're doing this is because we're saving function
            names to a list, you can't save function instances. So this is the next
            best thing.
            """
            self.addWidget(getattr(getattr(core, f_items), f_items))

        for i in range(1, len(dict)):
            self.widgetList[i - 1].setGuiParams(dict[i])

    def on_save_clicked(self):
        """
        Save the workflow to a *.wrf file

        :return:
        """
        try:
            filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None,
                                                                      "Choose where you want save your file",
                                                                      self.outpath,
                                                                      '(*.wrf)')
            print(filename)
            with open(filename, 'wb') as fp:
                pickle.dump(self.getWidgetItems(), fp)
            self.title.setFileName(filename.split('/')[-1])
            self.MainWindow.setWindowTitle(self.title.display())
        except Exception as e:
            print("File not loaded {}".format(e))

    def on_restore_clicked(self):
        """
        Choose a file
        Set the file to be read
        Pickle load our data and push it through the function setWidgetItems

        :return:
        """
        try:
            self.restorefilename, _filter = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                                  "Open Workflow File",
                                                                                  self.outpath,
                                                                                  '(*.wrf)')
            print(self.restorefilename)
            with open(self.restorefilename, 'rb') as fp:
                self.setWidgetItems(pickle.load(fp))
            self.title.setFileName(self.restorefilename.split('/')[-1])
            self.MainWindow.setWindowTitle(self.title.display())
        except Exception as e:
            print("File not loaded: {}".format(e))

    def on_delete_module_clicked(self):
        """
        Check to see if the last item is enabled
        If it is, delete the last item in the list
        And then call the del_layout function, which will remove the item from the UI

        :return:
        """
        try:
            if self.widgetList[-1].isEnabled():
                del self.widgetList[-1]
                delete.del_layout(self.verticalLayout_3)
            else:
                print("Cannot delete")
        except:
            print("Cannot delete")

    def on_okButton_clicked(self):
        """
        Start the multithreading function

        :return:
        """
        self.onStart()
        self.taskFinished.connect(self.onFinished)

    def on_Rerun_Button_clicked(self):
        """
        Check to see if the last item in the list is enabled
        subtract 1 from leftOff
        enable the current leftOff item

        :return:
        """
        try:
            if not self.widgetList[-1].isEnabled():
                self.leftOff -= 1
                self.widgetList[self.leftOff].setDisabled(False)
        except:
            pass

    def on_stopButton_clicked(self):
        """
        Terminate running thread

        :return:
        """
        if self.isRunning():
            self.terminate()
            self.taskFinished.emit()
        else:
            print("There is nothing running right now")

    def on_About_clicked(self):
        self.form = About()
        self.form.show()

    def _writeWindowAttributeSettings(self):
        '''
        Save window attributes as settings.

        Called when window moved, resized, or closed.
        '''
        self.settings.beginGroup("mainWindow")
        self.settings.setValue("pos", self.MainWindow.pos())
        self.settings.setValue("maximized", self.MainWindow.isMaximized())
        if not self.MainWindow.isMaximized():
            self.settings.setValue("size", self.MainWindow.size())

        self.settings.endGroup()

    def _readAndApplyWindowAttributeSettings(self):
        '''
        Read window attributes from settings,
        using current attributes as defaults (if settings not exist.)

        Called at QMainWindow initialization, before show().
        '''
        self.settings.beginGroup("mainWindow")
        # No need for toPoint, etc. : PySide converts types
        try:
            self.MainWindow.move(self.settings.value("pos"))
            if self.settings.value("maximized") in 'true':
                self.MainWindow.showMaximized()
            else:
                self.MainWindow.resize(self.settings.value("size"))
        except:
            pass
        self.settings.endGroup()

    def onStart(self):
        """
        This is multithreading thus run() == start()
        make the bar pulse green
        TaskThread.start()

        :return:
        """
        self.progressBar.setRange(0, 0)
        self.start()

    def onFinished(self):  # onFinished function
        self.progressBar.setRange(0, 1)  # stop the bar pulsing green
        self.progressBar.setValue(1)  # displays 100% after process is finished.

    def clear(self):
        """
        Delete all modules in GUI

        :return:
        """
        while len(self.widgetList) > 0 and self.widgetList[-1].isEnabled():
            self.on_delete_module_clicked()
        self.title.setFileName('')
        self.MainWindow.setWindowTitle(self.title.display())
        self.textBrowser.clear()

    def new(self):
        """
        Start a new gui

        :return:
        """
        self._writeWindowAttributeSettings()
        p = mp.Process(target=main, args=())
        p.start()

    def runModules(self):
        """
        This function iterates through a list of object addresses
        which then run it's dot notated function()

        iterate through our widgets, start from the last left off item
        get the name of our current widget item
        start the timers
        print the name of the module running
        if a restored file exists
            run connectWidgets # to update the current UI widget
            run selectiveRestore # to select the right items
            Terminate running process, and let the user decide if they want to continue forward
        run our current modules function()
        get our end time
        print how long it took our current module to execute based on start time and end time
        disable our current module
        increment our left off module

        :return:
        """
        dic = None
        try:
            with open(self.restorefilename, 'rb') as fp:
                dic = pickle.load(fp)
        except:
            pass

        for modules in range(self.leftOff, len(self.widgetList)):
            name_ = type(self.widgetList[modules]).__name__
            s = time.time()
            print("{} Module is Running...".format(name_))
            # if dic is not None:
            #     self.widgetList[modules].connectWidgets()
            #     self.widgetList[modules].selectiveSetGuiParams(dic[modules + 1])
            self.widgetList[modules].function()
            e = time.time()
            print("Module {} executed in: {} seconds".format(name_, e - s))
            self.widgetList[modules].setDisabled(True)
            self.leftOff = modules + 1

    def _exceptionLogger(self, function):
        """
        Logs an exception that occurs during the running of a function
        Take a function address in as an input

        :param function:
        :return:
        """
        logfile = "file.log"
        logpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\logs')

        try:
            function()
        except:
            if not os.path.exists(logpath):
                os.makedirs(logpath)
            timenow = strftime('%d-%m-%y_%H-%M-%S')
            logfilename = "%s_%s" % (timenow, logfile)
            filename = os.path.join(str(os.getcwd()), "%s" % (os.path.join(logpath, logfilename)))
            logging.basicConfig(level=logging.DEBUG, filename=filename)
            logging.exception(
                '[%s %s] (%s) Version: %s:' % (platform.system(), platform.release(), timenow, __version__))
            traceback.print_exc()
            print('\nException was logged to "%s"' % (os.path.join(logpath, logfilename)))

    def run(self):
        """
        Start the thread for running all the modules

        :return:
        """
        if self.debug:
            self._exceptionLogger(self.runModules)
        else:
            try:
                self.runModules()
            except Exception as e:
                print("Your module broke: please fix.", e)
                try:
                    self.widgetList[self.leftOff].setDisabled(False)
                except:
                    pass
        self.taskFinished.emit()


def get_splash(app):
    """
    Get the splash screen for the application
    But check to see if the image even exists

    :param app:
    :return:
    """
    dirs = ['../images/', '/point_spectra_gui/images', './point_spectra_gui/images']
    for dir in dirs:
        if os.path.exists(dir + 'splash.png'):
            splash_pix = QPixmap(dir + 'splash.png')  # default
            app_icon = QtGui.QIcon(dir + 'icon.png')
            app.setWindowIcon(app_icon)
            splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
            splash.setMask(splash_pix.mask())
            splash.show()
            time.sleep(0.5)
            app.processEvents()
            return 0


def setDarkmode(app):
    settings = QSettings('USGS', 'PPSG')
    p = settings.value('theme') == 'qtmodern'
    if q and p:
        qtmodern.styles.dark(app)


def main():
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook
    app = QtWidgets.QApplication(sys.argv)
    get_splash(app)
    setDarkmode(app)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
