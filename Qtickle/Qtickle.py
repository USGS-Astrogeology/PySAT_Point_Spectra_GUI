import inspect
from distutils.util import strtobool

from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Qtickle(object):
    """
    A script designed to aid in saving values inside Qt objects.
    It works by inspecting for objectnames and then collecting their
    values.

    The name is a portmanteau of Qt and pickle. Originally the script
    utilized pickle to save data. Now data is returned in the form of
    a dictionary. This way the user gets to choose what happens to the
    data
    """

    def __init__(self, ui):
        self.ui = ui

    def guiSave(self):
        """
        Save all values in a particular UI
        :return:
        """
        dict = {}
        # Save geometry
        # self.settings.setValue('size', self.core.size())
        # self.settings.setValue('pos', self.core.pos())
        try:
            for name, obj in inspect.getmembers(self.ui):
                if isinstance(obj, QLineEdit):
                    name = obj.objectName()
                    value = obj.text()
                    dict[name] = value

                if isinstance(obj, QCheckBox):
                    name = obj.objectName()
                    state = obj.isChecked()
                    dict[name] = state

                if isinstance(obj, QRadioButton):
                    name = obj.objectName()
                    value = obj.isChecked()  # get stored value from registry
                    dict[name] = value

                if isinstance(obj, QSpinBox):
                    name = obj.objectName()
                    value = obj.value()  # get stored value from registry
                    dict[name] = value

                if isinstance(obj, QDoubleSpinBox):
                    name = obj.objectName()
                    value = obj.value()
                    dict[name] = value

                if isinstance(obj, QSlider):
                    name = obj.objectName()
                    value = obj.value()  # get stored value from registry
                    dict[name] = value

                if isinstance(obj, QLabel):
                    name = obj.objectName()
                    value = obj.text()
                    dict[name] = value

                if isinstance(obj, QComboBox):
                    values = []  # the list that will hold all values from QCombobox
                    name = obj.objectName()  # get the QCombobox object's name
                    for i in range(obj.count()):  # QCombobox contains a number of items
                        itemData = obj.itemText(i)
                        values.append(itemData)  # put those items into a list for saving
                    index = obj.findText(obj.currentText())  # return the index of the item, assign to selected
                    dict[name + "_values"] = values  # save all the values in settings
                    dict[name + "_index"] = index  # save the indexed value in settings

                if isinstance(obj, QListWidget):
                    values = []
                    name = obj.objectName()
                    for i in range(obj.count()):
                        itemData = obj.item(i).text()
                        values.append(itemData)
                    dict[name + "_values"] = values
                    # since there is a possibility of multiple items,
                    # we'll just save the string representation of those items to be restored
                    dict[name + "_index"] = [str(x.text()) for x in obj.selectedItems()]

            return dict
        except Exception as e:
            print(e)

    def guiRestore(self, dict):
        # Restore geometry
        # self.core.resize(self.settings.value('size', QtCore.QSize(500, 500)))
        # self.core.move(self.settings.value('pos', QtCore.QPoint(60, 60)))
        for name, obj in inspect.getmembers(self.ui):
            pass
            try:
                if isinstance(obj, QLineEdit):
                    name = obj.objectName()
                    value = dict[name]
                    obj.setText(value)  # restore lineEditFile

                if isinstance(obj, QCheckBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        try:
                            obj.setChecked(strtobool(value))  # restore checkbox
                        except:
                            obj.setChecked(value)

                if isinstance(obj, QRadioButton):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setChecked(strtobool(value))

                if isinstance(obj, QSlider):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(int(value))  # restore value from registry

                if isinstance(obj, QSpinBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(int(value))  # restore value from registry

                if isinstance(obj, QDoubleSpinBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(float(value))

                if isinstance(obj, QLabel):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setText(value)

                if isinstance(obj, QComboBox):
                    name = obj.objectName()
                    values = dict[name + "_values"]
                    # clear all the objects
                    # so that we don't run into issues
                    # with restoring the list of values
                    obj.clear()
                    if values is not None:
                        for value in values:
                            if not (value == '' or value == "") and len(value) > 0:
                                # if there are some values in the list, we should add them to the Combobox
                                obj.addItem(value)

                    index = dict[name + "_index"]  # next we want to select the item in question by getting it's index
                    obj.setCurrentIndex(int(index))

                if isinstance(obj, QListWidget):
                    name = obj.objectName()
                    values = dict[name + "_values"]
                    index = dict[name + "_index"]
                    obj.clear()
                    if values is not None:
                        for value in values:
                            list_item = QListWidgetItem(value)
                            obj.addItem(list_item)
                        for i in index:
                            matching_items = obj.findItems(i, QtCore.Qt.MatchExactly)
                            for item in matching_items:
                                obj.setCurrentItem(item)

            except Exception as e:
                print(e)

    def isGuiChanged(self, functionCall):
        try:
            for name, obj in inspect.getmembers(self.ui):
                if isinstance(obj, QLineEdit):
                    obj.textChanged.connect(lambda: functionCall())

                if isinstance(obj, QCheckBox):
                    obj.stateChanged.connect(lambda: functionCall())

                if isinstance(obj, QRadioButton):
                    obj.toggled.connect(lambda: functionCall())

                if isinstance(obj, QSpinBox):
                    obj.valueChanged.connect(lambda: functionCall())

                if isinstance(obj, QDoubleSpinBox):
                    obj.valueChanged.connect(lambda: functionCall())

                if isinstance(obj, QSlider):
                    obj.event.connect(lambda: functionCall())

                if isinstance(obj, QComboBox):
                    obj.currentIndexChanged.connect(lambda: functionCall())

                    # if isinstance(obj, QListWidget): This needs to be added at somepoint
                    #     obj.

        except Exception as e:
            print(e)

    def selectiveGuiRestore(self, dict):
        for name, obj in inspect.getmembers(self.ui):
            pass
            try:
                if isinstance(obj, QCheckBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        try:
                            obj.setChecked(strtobool(value))  # restore checkbox
                        except:
                            obj.setChecked(value)

                if isinstance(obj, QRadioButton):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setChecked(strtobool(value))

                if isinstance(obj, QSlider):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(int(value))  # restore value from registry

                if isinstance(obj, QSpinBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(int(value))  # restore value from registry

                if isinstance(obj, QDoubleSpinBox):
                    name = obj.objectName()
                    value = dict[name]
                    if value is not None:
                        obj.setValue(float(value))

                if isinstance(obj, QComboBox):
                    name = obj.objectName()
                    # select the item in question by setting it's index
                    index = dict[name + "_index"]
                    obj.setCurrentIndex(int(index))

                if isinstance(obj, QListWidget):
                    name = obj.objectName()
                    values = dict[name + "_values"]
                    index = dict[name + "_index"]
                    obj.clear()
                    if values is not None:
                        for value in values:
                            list_item = QListWidgetItem(value)
                            obj.addItem(list_item)
                        for i in index:
                            matching_items = obj.findItems(i, QtCore.Qt.MatchExactly)
                            for item in matching_items:
                                obj.setCurrentItem(item)

            except Exception as e:
                print(e)
