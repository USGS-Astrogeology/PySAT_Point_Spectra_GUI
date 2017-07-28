import traceback

from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox, make_listwidget, change_combo_list_vars
from point_spectra_gui.ui_modules.Error_ import error_print


class cv_:
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
        self.cv_ui()
        self.set_cv_parameters()
        self.cv_choosealg.currentIndexChanged.connect(lambda: self.make_reg_widget(self.cv_choosealg.currentText()))
        self.get_cv_parameters()
        self.pysat_fun.set_greyed_modules(self.cv_train)

    def get_cv_parameters(self):

        method = self.cv_choosealg.currentText()
        datakey = self.cv_choosedata.currentText()
        xvars = [str(x.text()) for x in self.cv_train_choosex.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.cv_train_choosey.selectedItems()]
        yrange = [self.yvarmin_spin.value(), self.yvarmax_spin.value()]
        params = {}
        kws = {}
        try:
            if method == 'PLS':
                nc = self.reg_widget.pls_nc.text().split(',')
                nc = [int(i) for i in nc]
                params = {'n_components': nc,
                          'scale': [False]}
                # modelkey=[method+' (nc='+str(i)+')' for i in self.reg_widget.pls_nc_lineedit.text().split(',')]

            if method == 'GP':
                nc = [int(i) for i in self.reg_widget.gp_dim_red_nc.text().split(',')]
                random_start = [int(i) for i in self.reg_widget.gp_rand_starts.text().split(',')]
                theta0 = [float(i) for i in self.reg_widget.gp_theta0.text().split(',')]
                thetaL = [float(i) for i in self.reg_widget.gp_thetaL.text().split(',')]
                thetaU = [float(i) for i in self.reg_widget.gp_thetaU.text().split(',')]

                params = {'reduce_dim': self.reg_widget.gp_dim_red.text().split(','),
                          'n_components': nc,
                          'random_start': random_start,
                          'theta0': theta0,
                          'thetaL': thetaL,
                          'thetaU': thetaU}

        except:
            pass

        args = [datakey, xvars, yvars, yrange, method, params]

        ui_list = 'do_cv'
        fun_list = 'do_cv_train'
        r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def set_cv_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guiRestore(self.restr_list)
        if self.arg_list is not None:
            try:
                datakey = self.arg_list[0]
                xvars = self.arg_list[1]
                yvars = self.arg_list[2]
                yrange = self.arg_list[3]
                method = self.arg_list[4]
                params = self.arg_list[5]
                # ransacparams = self.arg_list[6]
                change_combo_list_vars(self.cv_train_choosey, self.restr_list['self.cv_train_choosey_values'])
                change_combo_list_vars(self.cv_train_choosex, self.restr_list['self.cv_train_choosex_values'])
                self.cv_choosedata.setCurrentIndex(self.cv_choosedata.findText(str(datakey)))
                try:
                    self.cv_train_choosex.setCurrentItem(
                        self.cv_train_choosex.findItems(xvars[0], QtCore.Qt.MatchExactly)[0])
                except:
                    pass
                try:
                    self.cv_train_choosey.setCurrentItem(
                        self.cv_train_choosey.findItems(yvars[0][1], QtCore.Qt.MatchExactly)[0])
                except:
                    pass
                self.yvarmin_spin.setValue(yrange[0])
                self.yvarmax_spin.setValue(yrange[1])
                self.cv_choosealg.setCurrentIndex(self.cv_choosealg.findText(str(method)))
                self.make_reg_widget(self.cv_choosealg.currentText(), params=params)
            except Exception as e:
                print(e)

    def make_reg_widget(self, alg, params=None):
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget = QtWidgets.QWidget()
        if alg == 'PLS':
            self.reg_widget.pls_hlayout = QtWidgets.QHBoxLayout(self.reg_widget)
            self.reg_widget.pls_nc_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.pls_nc_label.setText('# of components:')
            self.reg_widget.pls_nc_label.setObjectName("self.reg_widget.pls_nc_label")
            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc_label)
            self.reg_widget.pls_nc = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.pls_nc.setObjectName("self.reg_widget.pls_nc")
            self.reg_widget.pls_hlayout.addWidget(self.reg_widget.pls_nc)
            self.reg_widget.pls_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                               QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.pls_hlayout.addItem(self.reg_widget.pls_spacer)
            self.reg_widget.pls_nc.textChanged.connect(lambda: self.get_cv_parameters())
            if params is not None:
                self.reg_widget.pls_nc.setText(','.join(str(e) for e in params['n_components']))
        if alg == 'GP':
            self.reg_widget = QtWidgets.QWidget()
            self.reg_widget.gp_vlayout = QtWidgets.QVBoxLayout(self.reg_widget)
            self.reg_widget.gp_dim_red_hlayout = QtWidgets.QHBoxLayout()
            self.reg_widget.gp_dim_red_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_dim_red_label.setText('Choose dimensionality reduction method:')
            self.reg_widget.gp_dim_red_label.setObjectName("self.reg_widget.gp_dim_red_label")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_label)
            self.reg_widget.gp_dim_red = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_dim_red.setText('PCA')
            self.reg_widget.gp_dim_red.setObjectName("self.reg_widget.gp_dim_red")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red)
            self.reg_widget.gp_dim_red_nc_label = QtWidgets.QLabel()
            self.reg_widget.gp_dim_red_nc_label.setText('# of components:')
            self.reg_widget.gp_dim_red_nc_label.setObjectName("self.reg_widget.gp_dim_red_nc_label")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc_label)
            self.reg_widget.gp_dim_red_nc = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_dim_red_nc.setObjectName("self.reg_widget.gp_dim_red_nc")
            self.reg_widget.gp_dim_red_hlayout.addWidget(self.reg_widget.gp_dim_red_nc)

            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_dim_red_hlayout)
            self.reg_widget.gp_rand_starts_hlayout = QtWidgets.QHBoxLayout()
            self.reg_widget.gp_rand_starts_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_rand_starts_label.setText('# of random starts:')
            self.reg_widget.gp_rand_starts_label.setObjectName("self.reg_widget.gp_rand_starts_label")
            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts_label)
            self.reg_widget.gp_rand_starts = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_rand_starts.setText('1')
            self.reg_widget.gp_rand_starts.setObjectName("self.reg_widget.gp_rand_starts")
            self.reg_widget.gp_rand_starts_hlayout.addWidget(self.reg_widget.gp_rand_starts)
            self.reg_widget.spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.gp_rand_starts_hlayout.addItem(self.reg_widget.spacerItem4)
            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_rand_starts_hlayout)
            self.reg_widget.gp_theta_vlayout = QtWidgets.QVBoxLayout()
            self.reg_widget.gp_theta0_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_theta0_label.setText('Starting Theta:')
            self.reg_widget.gp_theta0_label.setObjectName("self.reg_widget.gp_theta0_label")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0_label)
            self.reg_widget.gp_theta0 = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_theta0.setText('1')
            self.reg_widget.gp_theta0.setObjectName("self.reg_widget.gp_theta0")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_theta0)
            self.reg_widget.gp_thetaL_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_thetaL_label.setText('Lower bound on Theta:')
            self.reg_widget.gp_thetaL_label.setObjectName("self.reg_widget.gp_thetaL_label")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL_label)
            self.reg_widget.gp_thetaL = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_thetaL.setText('0.1')
            self.reg_widget.gp_thetaL.setObjectName("self.reg_widget.gp_thetaL")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaL)
            self.reg_widget.gp_thetaU_label = QtWidgets.QLabel(self.reg_widget)
            self.reg_widget.gp_thetaU_label.setText('Upper bound on Theta:')
            self.reg_widget.gp_thetaU_label.setObjectName("self.reg_widget.gp_thetaU_label")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU_label)
            self.reg_widget.gp_thetaU = QtWidgets.QLineEdit(self.reg_widget)
            self.reg_widget.gp_thetaU.setText('100.0')

            self.reg_widget.gp_thetaU.setObjectName("self.reg_widget.gp_thetaU")
            self.reg_widget.gp_theta_vlayout.addWidget(self.reg_widget.gp_thetaU)
            self.reg_widget.spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                QtWidgets.QSizePolicy.Minimum)
            self.reg_widget.gp_theta_vlayout.addItem(self.reg_widget.spacerItem5)
            self.reg_widget.gp_vlayout.addLayout(self.reg_widget.gp_theta_vlayout)
            self.reg_widget.gp_dim_red.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_dim_red_nc.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_rand_starts.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_theta0.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_thetaL.textChanged.connect(lambda: self.get_cv_parameters())
            self.reg_widget.gp_thetaU.textChanged.connect(lambda: self.get_cv_parameters())
            if params is not None:
                self.reg_widget.gp_dim_red.setText(','.join(str(e) for e in params['reduce_dim']))
                self.reg_widget.gp_dim_red_nc.setText(','.join(str(e) for e in params['n_components']))
                self.reg_widget.gp_rand_starts.setText(','.join(str(e) for e in params['random_start']))
                self.reg_widget.gp_theta0.setText(','.join(str(e) for e in params['theta0']))
                self.reg_widget.gp_thetaL.setText(','.join(str(e) for e in params['thetaL']))
                self.reg_widget.gp_thetaU.setText(','.join(str(e) for e in params['thetaU']))

        if alg == 'OLS':
            pass
        if alg == 'OMP':
            pass
        if alg == 'Lasso':
            pass
        if alg == 'Elastic Net':
            pass
        if alg == 'Ridge':
            pass
        if alg == 'Bayesian Ridge':
            pass
        if alg == 'ARD':
            pass
        if alg == 'LARS':
            pass
        if alg == 'Lasso LARS':
            pass
        if alg == 'SVR':
            pass
        if alg == 'KRR':
            pass

        self.reg_widget.setObjectName("self.reg_widget")
        self.cv_vlayout.addWidget(self.reg_widget)
        self.get_cv_parameters()

    def cv_ui(self):
        self.cv_train = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cv_train.setFont(font)
        self.cv_vlayout = QtWidgets.QVBoxLayout(self.cv_train)
        # choose data
        self.cv_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.cv_train_choosedata_label = QtWidgets.QLabel(self.cv_train)
        self.cv_train_choosedata_label.setText("Choose data:")
        self.cv_train_choosedata_label.setObjectName("self.cv_train_choosedata_label")
        self.cv_choosedata_hlayout.addWidget(self.cv_train_choosedata_label)
        datachoices = []
        try:
            datachoices = self.pysat_fun.datakeys
        except:
            pass
        self.cv_choosedata = make_combobox(datachoices)
        self.cv_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.cv_choosedata.setObjectName("self.cv_choosedata")
        self.cv_choosedata_hlayout.addWidget(self.cv_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cv_choosedata_hlayout.addItem(spacerItem)
        self.cv_vlayout.addLayout(self.cv_choosedata_hlayout)
        # choose variables
        self.cv_choosevars_hlayout = QtWidgets.QHBoxLayout()
        self.cv_choosexvars_vlayout = QtWidgets.QVBoxLayout()
        self.cv_chooseyvars_vlayout = QtWidgets.QVBoxLayout()
        self.cv_choosevars_hlayout.addLayout(self.cv_choosexvars_vlayout)
        self.cv_choosevars_hlayout.addLayout(self.cv_chooseyvars_vlayout)

        # choose x variables
        self.cv_train_choosex_label = QtWidgets.QLabel(self.cv_train)
        self.cv_train_choosex_label.setText('X variable:')
        self.cv_train_choosex_label.setObjectName("self.cv_train_choosex_label")
        self.cv_choosexvars_vlayout.addWidget(self.cv_train_choosex_label)
        self.cv_train_choosex = make_listwidget(self.cv_xvar_choices())
        self.cv_train_choosex.setObjectName("self.cv_train_choosex")
        self.cv_choosexvars_vlayout.addWidget(self.cv_train_choosex)

        # choose y variables
        self.cv_train_choosey_label = QtWidgets.QLabel(self.cv_train)
        self.cv_train_choosey_label.setText('Y variable:')
        self.cv_train_choosey_label.setObjectName("self.cv_train_choosey_label")
        self.cv_chooseyvars_vlayout.addWidget(self.cv_train_choosey_label)
        self.cv_train_choosey = make_listwidget(self.cv_yvar_choices())
        self.cv_train_choosey.setObjectName("self.cv_train_choosey")
        self.cv_chooseyvars_vlayout.addWidget(self.cv_train_choosey)

        # set limits
        self.cv_yvarlimits_hlayout = QtWidgets.QHBoxLayout()
        self.yvarmin_label = QtWidgets.QLabel(self.cv_train)
        self.yvarmin_label.setText('Min:')
        self.yvarmin_label.setObjectName("self.yvarmin_label")
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.yvarmin_spin = QtWidgets.QDoubleSpinBox()
        self.yvarmin_spin.setMaximum(99999)
        self.yvarmin_spin.setMinimum(0)
        self.yvarmin_label.setObjectName("self.yvarmin_label")
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.yvarmin_spin.setObjectName("self.yvarmin_spin")
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmin_spin)

        self.yvarmax_label = QtWidgets.QLabel(self.cv_train)
        self.yvarmax_label.setText('Max:')
        self.yvarmax_label.setObjectName("self.yvarmax_label")
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.yvarmax_spin = QtWidgets.QDoubleSpinBox()
        self.yvarmax_spin.setMaximum(99999)
        self.yvarmax_spin.setMinimum(0)
        self.yvarmax_spin.setValue(100)
        self.yvarmax_label.setObjectName("self.yvarmax_label")
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.yvarmax_spin.setObjectName("self.yvarmax_spin")
        self.cv_yvarlimits_hlayout.addWidget(self.yvarmax_spin)
        self.cv_chooseyvars_vlayout.addLayout(self.cv_yvarlimits_hlayout)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cv_choosevars_hlayout.addItem(spacerItem1)
        self.cv_vlayout.addLayout(self.cv_choosevars_hlayout)

        # ransac options
        # self.ransac_hlayout = QtWidgets.QHBoxLayout()
        # self.cv_ransac_checkbox = QtWidgets.QCheckBox(self.cv_train)
        # self.cv_ransac_checkbox.setText('RANSAC')
        # self.ransac_hlayout.addWidget(self.cv_ransac_checkbox)
        # self.cv_vlayout.addLayout(self.ransac_hlayout)

        # choose cv algorithm
        self.cv_choosealg_hlayout = QtWidgets.QHBoxLayout()
        self.cv_choosealg_label = QtWidgets.QLabel(self.cv_train)
        self.cv_choosealg_label.setObjectName("self.cv_choosealg_label")
        self.cv_choosealg_hlayout.addWidget(self.cv_choosealg_label)
        self.cv_alg_choices = ['Choose an algorithm', 'PLS', 'GP', 'More to come...']
        self.cv_choosealg = make_combobox(self.cv_alg_choices)
        self.cv_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.cv_choosealg.setObjectName("self.cv_choosealg")
        self.cv_choosealg_hlayout.addWidget(self.cv_choosealg)
        # TODO add logic that knows when args and kwargs are added.
        cv_choosealg_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
        self.cv_choosealg_hlayout.addItem(cv_choosealg_spacer)
        self.cv_vlayout.addLayout(self.cv_choosealg_hlayout)

        self.cv_train.setObjectName("self.cv_train")
        self.module_layout.addWidget(self.cv_train)
        self.cv_train.raise_()
        self.cv_train.setTitle("Cross Validation / Training")

        self.set_cv_parameters()
        self.cv_choosedata.currentIndexChanged.connect(lambda: self.get_cv_parameters())
        self.cv_choosealg.currentIndexChanged.connect(lambda: self.get_cv_parameters())
        self.cv_train_choosex.currentItemChanged.connect(lambda: self.get_cv_parameters())
        self.cv_train_choosey.currentItemChanged.connect(lambda: self.get_cv_parameters())
        self.cv_choosedata.activated[int].connect(
            lambda: change_combo_list_vars(self.cv_train_choosey, self.cv_yvar_choices()))
        self.cv_choosedata.activated[int].connect(
            lambda: change_combo_list_vars(self.cv_train_choosex, self.cv_xvar_choices()))

    def cv_yvar_choices(self):
        try:
            yvarchoices = self.pysat_fun.data[self.cv_choosedata.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def cv_xvar_choices(self):
        try:
            xvarchoices = self.pysat_fun.data[self.cv_choosedata.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices
