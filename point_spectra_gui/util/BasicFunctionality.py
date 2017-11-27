import inspect
import sys
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import *
from Qtickle import Qtickle



class Basics:
    """
    This class is a scaffolding class, it holds global
    functionality for all classes inheriting from it.
    It is here to simplify and globalize certain
    variables and functionalities to each of the
    UI classes.

    *Note: Rigorous prototyping is still occurring
    So, naturally, assume that something in this class
    is always getting changed or added to better serve
    all cases in each UI class.

    ...

    Since `Basics` is shared among all the UI
    classes it would make sense that we would have
    some variables, that are necessary among all these
    classes, be put here in a high place where they
    can be referenced often.
    """
    data = {}  # initialize with an empty dict to hold data frames
    datakeys = []  # hold all the specific key for a specific data frame
    modelkeys = []
    outpath = './'  # Default outpath; can be changed with OutputFolder.py
    figs = {}
    figname = []
    models = {}  # For regression training
    model_xvars = {}
    model_yvars = {}

    def __init__(self):
        self.qt = Qtickle.Qtickle(self)
        self.settings = QSettings('USGS', 'PPSG')
        self.flag = False

    def setupUi(self, Form):
        self.Form = Form
        self.Form.mousePressEvent = self.mousePressEvent
        self.connectWidgets()

    def mousePressEvent(self, QMouseEvent):
        """
        Right click event
        """
        # TODO Add mouse Event
        # print("Right Button Clicked {}".format(type(self).__name__))

    def get_widget(self):
        """
        This function specifies the variable that holds the
        styling. Use this function to get the variable
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "get_widget()" was not found in this module')

    def connectWidgets(self):
        """
        Connect the necessary widgets.
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "connectWidgets()" was not found in this module')

    def getGuiParams(self):
        """
        Return the contents from lineEdits, comboBoxes, etc.
        :return:
        """
        self.qt = Qtickle.Qtickle(self)
        s = self.qt.guiSave()
        return s

    def setGuiParams(self, dict):
        """
        Using a dictionary, restore the UI
        :param dict:
        :return:
        """
        self.qt = Qtickle.Qtickle(self)
        self.qt.guiRestore(dict)
        self.qt.isGuiChanged(self.setUiFlag)

    def getGuiState(self):
        """
        Get the state of the current module
        :return:
        """
        return self.getUiFlag()

    def function(self):
        """
        Each Module's functionality will be ran in this function.
        You will define what will happen to the data and parameters in here
        :return:
        """
        sys.exit('Error: Application closed unexpectedly\n'
                 'The method "function()" was not found in this module')

    def isEnabled(self):
        """
        Checks to see if current widget isEnabled or not
        :return:
        """
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        """
        After every execution we want to prevent the user from changing something.
        So, disable the layout by greying it out
        :param bool:
        :return:
        """
        self.get_widget().setDisabled(bool)

    def setProgressBar(self, progressBar):
        """
        This function makes it possible to reference the progress bar
        in MainWindow
        :param progressBar:
        :return:
        """
        self.progressBar = progressBar

    def checkMinAndMax(self):
        """
        Go through the entire UI and set the maximums and minimums of each widget
        :return:
        """
        for name, obj in inspect.getmembers(self):
            if isinstance(obj, QSpinBox):
                obj.setMaximum(999999)

            if isinstance(obj, QDoubleSpinBox):
                obj.setDecimals(7)

    def setUiFlag(self):
        """
        Set the flag to true when the state of the current module changes
        :return:
        """
        self.flag = True

    def getUiFlag(self):
        """
        Return the flag for the UI's state
        :return:
        """
        return self.flag

    @staticmethod
    def setComboBox(comboBox, keyValues):
        """
        Sets up the information inside comboBox widgets
        This function does not need to be overridden.
        :param comboBox: QtWidgets.QComboBox
        :param keyValues: []
        :return:
        """
        comboBox.clear()
        comboBox.addItems(keyValues)

    @staticmethod
    def checkoptions(selection, actual_options, message):
        if isinstance(selection,list):
            for i in selection:
                if i not in actual_options:
                    print('Selected '+message+' does not exist. Refreshing options...')
                    return True
        else:
            if selection not in actual_options:
                print('Selected ' + message + ' does not exist. Refreshing options...')
                return True
        return False

    @staticmethod
    def changeComboListVars(obj, newchoices):
        """
        Function changes combo boxes
        This function does not need to be overridden.
        :param obj:
        :param newchoices:
        :return:
        """
        obj.clear()
        for i in newchoices:
            if isinstance(i, tuple):
                obj.addItem(i[1])
            elif isinstance(i, str):
                obj.addItem(i)

    @staticmethod
    def setListWidget(obj, choices):
        """
        Function changes lists
        This function does not need to be overridden
        :param obj:
        :param choices:
        :return:
        """
        for item in choices:
            obj.addItem(item)

    @staticmethod
    def defaultComboItem(obj, item):
        """
        Set the default selected item in a box.
        :param obj:
        :param item:
        :return:
        """
        obj.setCurrentIndex(obj.findText(str(item)))
