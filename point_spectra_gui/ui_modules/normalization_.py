from PyQt5 import QtGui, QtCore, QtWidgets

from point_spectra_gui.ui_modules import make_combobox, Qtickle
from point_spectra_gui.ui_modules.del_layout_ import del_layout_
from point_spectra_gui.gui_utils import make_listwidget

# Normalization creates a UI
# and many smaller pieces of the UI called min_max
#
# normalization
#     |_ min_max
#     |_ min_max
#     |_ min_max
#
# each of these min_max's have connections that tell us what was updated
# each of these updates should return a value back to normalization so we can add it to a list
#
#      |---------------------|           |----------------------|
#      |    Normalization    |           |       min_max        |
#      |---------------------|           |----------------------|
#      | returned val in lst | <-------- | return value and pos |
#      | load UI/Boxes       | --------> |                      |
#      |---------------------|           |----------------------|
#
# every time we change boxes, we should know which box is getting updated, and what the updated value is
# so for example
#
#     min [      ]  max [      ]
#     min [      ]  max [ 1000 ]*
#     min [      ]  max [      ]
# the above box* was update4d
# it's position is data[1], max_lineEdit, and it's value is 1000

class normalization_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.qtickle = Qtickle.Qtickle(self)
        self.box_list = []
        self.pysat_fun = pysat_fun
        self.module_layout = module_layout
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.restr_list = restr_list
        self.ui_id = None
        self.main()

    def main(self):
        # driver function, calls UI and set's up connections
        # add function list calls here
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.normalization_ui()
        self.set_norm_parameters()
        self.get_norm_parameters()
        self.pysat_fun.set_greyed_modules(self.normalization)
        self.connectWidgets()

    def normalization_ui(self):
        datachoices = self.pysat_fun.datakeys
        self.normalization = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalization.setFont(font)
        self.normalization.setObjectName(("normalization"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.normalization)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(("verticalLayout"))
        self.choosedata_layout = QtWidgets.QHBoxLayout()
        self.choosedata_layout.setContentsMargins(11, 11, 11, 11)
        self.choosedata_layout.setSpacing(6)
        self.choosedata_layout.setObjectName(("choosedata_layout"))
        self.normalization_choosedata_label = QtWidgets.QLabel(self.normalization)
        self.normalization_choosedata_label.setObjectName(("normalization_choosedata_label"))
        self.choosedata_layout.addWidget(self.normalization_choosedata_label)
        self.normalization_choosedata = make_combobox(datachoices)
        self.normalization_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.normalization_choosedata.setObjectName(("normalization_choosedata"))
        self.choosedata_layout.addWidget(self.normalization_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.choosedata_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.choosedata_layout)

        self.norm_choosexcols_label = QtWidgets.QLabel(self.normalization)
        self.norm_choosexcols_label.setText('Variable to normalize:')
        self.norm_choosexcols_label.setObjectName("norm_choosexcols_label")
        self.verticalLayout.addWidget(self.norm_choosexcols_label)
        self.norm_choosexcols = make_listwidget(self.xvar_choices())
        self.norm_choosexcols.setObjectName("norm_choosexcols")
        self.verticalLayout.addWidget(self.norm_choosexcols)

        self.all_ranges_layout = QtWidgets.QVBoxLayout()
        self.all_ranges_layout.setContentsMargins(11, 11, 11, 11)
        self.all_ranges_layout.setSpacing(6)
        self.all_ranges_layout.setObjectName(("all_ranges_layout"))
        self.verticalLayout.addLayout(self.all_ranges_layout)
        self.min_max_horizontalLayout = QtWidgets.QHBoxLayout()
        self.min_max_horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.min_max_horizontalLayout.setSpacing(6)
        self.min_max_horizontalLayout.setObjectName(("min_max_horizontalLayout"))
        self.add_ranges_button = QtWidgets.QPushButton(self.normalization)
        self.add_ranges_button.setObjectName(("add_ranges_button"))
        self.min_max_horizontalLayout.addWidget(self.add_ranges_button)
        self.del_button = QtWidgets.QPushButton(self.normalization)
        self.del_button.setObjectName(("add_ranges_button_2"))
        self.min_max_horizontalLayout.addWidget(self.del_button)
        self.verticalLayout.addLayout(self.min_max_horizontalLayout)
        self.module_layout.addWidget(self.normalization)

        self.normalization.setTitle("Normalization")
        self.normalization_choosedata_label.setText("Choose data to normalize: ")
        self.add_ranges_button.setText("Add Range")
        self.del_button.setText("Delete Range")

    def add_ranges(self):

        self.ranges_layout = QtWidgets.QHBoxLayout()  # setup the ranges_layout, it will be a child of all_ranges_layout
        font = QtGui.QFont()
        font.setPointSize(10)
        self.min_label = QtWidgets.QLabel()  # setup the min label
        self.max_label = QtWidgets.QLabel()  # setup the max label
        self.min_label.setFont(font)
        self.max_label.setFont(font)
        self.min_spinbox = QtWidgets.QSpinBox()  # setup the min lineEdit
        self.max_spinbox = QtWidgets.QSpinBox()  # setup the max lineEdit
        self.max_spinbox.setMaximum(9999)
        self.min_spinbox.setMaximum(9999)
        self.min_spinbox.setFont(font)
        self.max_spinbox.setFont(font)
        try:
            minimum = int(self.box_list[-1].text())  # go to the last item in the list
            self.max_spinbox.setMinimum(minimum)  # set this as the minimum value
            self.min_spinbox.setMinimum(minimum)  # set this as the minimum value
        except:
            pass
        self.ranges_layout.addWidget(self.min_label)  # apply the min label to the widget
        self.ranges_layout.addWidget(self.min_spinbox)  # apply the min lineEdit to the widget
        self.ranges_layout.addWidget(self.max_label)  # apply the max label
        self.ranges_layout.addWidget(self.max_spinbox)  # apply the max lineEdit
        self.min_label.setText("Minimum wavelength")  # set the text of the min label
        self.max_label.setText("Maximum wavelength")  # set the text of the max label
        self.box_list.append(self.min_spinbox)  # set up an array of lineEdits
        self.box_list.append(self.max_spinbox)
        self.all_ranges_layout.addLayout(self.ranges_layout)
        self.min_spinbox.valueChanged.connect(lambda: self.get_norm_parameters())
        self.max_spinbox.valueChanged.connect(lambda: self.get_norm_parameters())

    def del_ranges(self):
        del_layout_(self.all_ranges_layout)
        del self.box_list[-1]  # delete left box
        del self.box_list[-1]  # delete right box
        self.get_norm_parameters()

    def set_norm_parameters(self):
        # TODO finish
        if self.restr_list is not None:
            self.qtickle.guiRestore(self.restr_list)

        if self.arg_list is not None:
            self.normalization_choosedata.setCurrentIndex(self.normalization_choosedata.findText(self.arg_list[0]))

            col_var = self.kw_list['col_var']
            items = self.norm_choosexcols.findItems(col_var, QtCore.Qt.MatchExactly)
            for item in items:
                item.setSelected(True)
            for i in range(len(self.arg_list[1])):
                box_list = self.arg_list[1]
                box_list = box_list[i]
                self.add_ranges()
                self.min_spinbox.setValue(box_list[0])
                self.max_spinbox.setValue(box_list[1])


    def get_norm_parameters(self):
        ranges = []
        len_box_list = len(self.box_list)
        try:
            for i in range(0, len_box_list, 2):
                ranges.append((int(self.box_list[i].text()), int(self.box_list[i + 1].text())))
            for i in range(len_box_list - 1):
                self.box_list[i].valueChanged.connect(self.box_list[i + 1].setMinimum)
        except Exception as e:
            import traceback
            print(e)
        datakey = self.normalization_choosedata.currentText()
        try:
            col_var = self.norm_choosexcols.selectedItems()[0].text()
        except:
            col_var = 'wvl'
        arg_list=[datakey,ranges]
        kw_list={'col_var': col_var}
        ui_list = "normalization"
        fun_list = "do_norm"

        r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, arg_list, kw_list, r, self.ui_id)

    def connectWidgets(self):
        self.norm_choosexcols.itemSelectionChanged.connect(lambda: self.get_norm_parameters())
        self.add_ranges_button.clicked.connect(lambda: self.add_ranges())
        self.del_button.clicked.connect(lambda: self.del_ranges())

    def xvar_choices(self):
        try:
            try:
                xvarchoices = self.pysat_fun.data[self.normalization_choosedata.currentText()].df.columns.levels[0].values
            except:
                xvarchoices = self.pysat_fun.data[self.normalization_choosedata.currentText()].columns.values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices