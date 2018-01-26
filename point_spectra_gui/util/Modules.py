import inspect

from PyQt5.QtCore import QSettings, pyqtSignal
from PyQt5.QtWidgets import *

from Qtickle import Qtickle


class Modules:
    """
    Modules class that UI modules will inherit from.

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

    # Hacky way of making a static string.
    _current_data = ['', '']

    @property
    def current_data(self):
        return self._current_data[0]
    
    @current_data.setter
    def current_data(self, value):
        self._current_data[0] = value

    @property
    def current_model(self):
        return self._current_data[1]
    
    @current_model.setter
    def current_model(self, value):
        self._current_data[1] = value

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
        TODO: Add right click event
        The hope is that we can add a right click dialogue for users
        The dialogue would give the option to delete particular
        modules from the UI, or insert modules, or copy modules.
        """
        # TODO Add mouse Event

    # @@TODO Remove all references to guiChanged
    def guiChanged(self):
        pass

    def get_widget(self):
        """
        This function specifies the variable that holds the
        styling. Use this function to get the variable
        :return:
        """
        raise NotImplementedError(
            'The method "get_widget()" was not found in the module {}'.format(type(self).__name__))

    def refresh(self):
        """
        This function is used to enable propagation, and is responsible for resetting widget properties
        based on the static variables found in this class.
        :return:
        """
        raise NotImplementedError(
            'The method "refresh()" was not found in the module {}'.format(type(self).__name__))


    def connectWidgets(self):
        """
        Connect the necessary widgets.
        :return:
        """
        raise NotImplementedError(
            'The method "connectWidgets()" was not found in the module {}'.format(type(self).__name__))

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

    def selectiveSetGuiParams(self, dict):
        """
        Selectively restore the UI.
        We don't want to lose the content we have selected
        but we don't want to override crucial information either

        :param dict:
        :return:
        """
        self.qt = Qtickle.Qtickle(self)
        self.qt.selectiveGuiRestore(dict)

    def run(self):
        """
        Each Module's functionality will be ran in this function.
        You will define what will happen to the data and parameters in here
        :return:
        """
        raise NotImplementedError('The method "run()" was not found in the module {}'.format(type(self).__name__))

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

    def setCurrentData(self, c):
        if isinstance(c, int):
            self.current_data = self.datakeys[c]
        elif isinstance(c, str):
            self.current_data = c
        else:
            raise TypeError("Current data must be assigned by a string value or integer index")



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
        dic = {}
        for key in input_dictionary:
            if input_dictionary[key] != getattr(algorithm, key):  # key gives us a string
                dic.update({key: input_dictionary[key]})

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
        comboBox.clear()
        comboBox.setMaximumWidth(200)
        comboBox.addItems(keyValues)

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
