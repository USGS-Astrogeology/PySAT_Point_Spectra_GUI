import inspect

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import *
from Qtickle import Qtickle


class Modules:
    """
    This class is the parent class that holds global
    functionality and variables for all classes
    inheriting from it.

    *Note: Rigorous prototyping is still occurring
    So, naturally, assume that something in this class
    is always getting changed or added to better serve
    all cases in each UI class.

    ...

    Since `Modules` is shared among all the UI
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
    parent = []
    LOCK = []

    def __init__(self):
        self.qt = Qtickle.Qtickle(self)
        self.settings = QSettings('USGS', 'PPSG')
        self.flag = False

    def setupUi(self, Form):
        self.Form = Form
        self.Form.mousePressEvent = self.mousePressEvent
        self.connectWidgets()
        self.guiChanged()

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
        raise NotImplementedError(
            'The method "get_widget()" was not found in the module {}'.format(type(self).__name__))

    def connectWidgets(self):
        """
        Connect the necessary widgets.
        :return:
        """
        raise NotImplementedError(
            'The method "connectWidgets()" was not found in the module {}'.format(type(self).__name__))

    def guiChanged(self):
        self.qt = Qtickle.Qtickle(self)
        self.qt.guiChanged(self.parent[0].setupModules)

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
        self.LOCK_ON()
        self.qt = Qtickle.Qtickle(self)
        self.qt.guiRestore(dict)
        self.LOCK_OFF()

    def selectiveSetGuiParams(self, dict):
        """
        Selectively restore the UI.
        We don't want to lose the content we have selected
        but we don't want to override crucial information either

        :param dict:
        :return:
        """
        self.LOCK_ON()
        self.qt = Qtickle.Qtickle(self)
        self.qt.selectiveGuiRestore(dict)
        self.LOCK_OFF()

    def setup(self):
        """
        This is a stripped down version of run()
        Each Module's functionality will be quickly ran through, so we have
        at least something in the UI to work with

        :return:
        """
        # raise NotImplementedError('The method "setup()" was not found in the module {}'.format(type(self).__name__))
        pass

    def run(self):
        """
        Each Module's functionality will be ran in this function.
        You will define what will happen to the data and parameters in here
        :return:
        """
        raise NotImplementedError('The method "run()" was not found in the module {}'.format(type(self).__name__))

    @staticmethod
    def LOCK_ON():
        Modules.LOCK = [True]

    @staticmethod
    def LOCK_OFF():
        Modules.LOCK = [False]

    def get_LOCK(self):
        return Modules.LOCK[0]

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

    @staticmethod
    def getChangedValues(input_dictionary, algorithm):
        """
        Check symmetrically if the values in the dictionary match with values in the algorithm
        If they don't, then we will want to record those changed values.

        Example input: getChangedValues(methodParameters, AirPLS())

        :param input_dictionary:
        :param algorithm:
        :return:
        """
        Modules.LOCK_ON()
        dic = {}
        for key in input_dictionary:
            if input_dictionary[key] != getattr(algorithm, key):  # key gives us a string
                dic.update({key: input_dictionary[key]})
        Modules.LOCK_OFF()
        return dic


    @staticmethod
    def setComboBox(comboBox, keyValues):
        """
        Sets up the information inside comboBox widgets
        This function does not need to be overridden.
        :param comboBox: QtWidgets.QComboBox
        :param keyValues: []
        :return:
        """
        Modules.LOCK_ON()
        comboBox.clear()
        comboBox.setMaximumWidth(200)
        comboBox.addItems(keyValues)
        Modules.LOCK_OFF()

    @staticmethod
    def changeComboListVars(obj, newchoices):
        """
        Function changes combo boxes
        This function does not need to be overridden.
        :param obj:
        :param newchoices:
        :return:
        """
        Modules.LOCK_ON()
        obj.clear()
        for i in newchoices:
            if isinstance(i, tuple):
                obj.addItem(i[1])
            elif isinstance(i, str):
                obj.addItem(i)
        Modules.LOCK_OFF()

    @staticmethod
    def setListWidget(obj, choices):
        """
        Function changes lists
        This function does not need to be overridden
        :param obj:
        :param choices:
        :return:
        """
        Modules.LOCK_ON()
        for item in choices:
            obj.addItem(item)
        Modules.LOCK_OFF()

    @staticmethod
    def defaultComboItem(obj, item):
        """
        Set the default selected item in a box.
        :param obj:
        :param item:
        :return:
        """
        Modules.LOCK_ON()
        obj.setCurrentIndex(obj.findText(str(item)))
        Modules.LOCK_OFF()
