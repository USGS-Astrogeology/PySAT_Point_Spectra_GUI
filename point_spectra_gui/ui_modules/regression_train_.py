import traceback
from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox, make_listwidget, change_combo_list_vars
from point_spectra_gui.ui_modules.regressionMethods import *


class regression_train_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.algorithm_list = ['Choose an algorithm',  # 0
                               'PLS',  # 1
                               'GP',  # 2
                               'OLS',  # 3
                               'OMP',  # 4
                               'Lasso',  # 5
                               'Elastic Net',  # 6
                               'Ridge',  # 7
                               'Bayesian Ridge',  # 8
                               'ARD',  # 9
                               'LARS',  # 10
                               'Lasso LARS',  # 11
                               'SVR',  # 12
                               'KRR',  # 13
                               'More to come...']
        self.isRestore = False
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
        if self.arg_list is not None:
            self.isRestore = True
        self.regression_ui()  # start the regression UI. create our submodule
        self.set_regression_parameters()  # Do it the first time to get data
        # self.regression_ransac_checkbox.toggled.connect(  #
        #     lambda: self.make_ransac_widget(self.regression_ransac_checkbox.isChecked()))  #
        self.regression_choosealg.currentIndexChanged.connect(  #
            lambda: self.make_regression_widget(self.regression_choosealg.currentText()))  #
        self.get_regression_parameters()
        self.connectWidgets()
        self.pysat_fun.set_greyed_modules(self.regression_train)

    def get_regression_parameters(self):
        method = self.regression_choosealg.currentText()
        datakey = self.regression_choosedata.currentText()
        xvars = [str(x.text()) for x in self.regression_train_choosex.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.regression_train_choosey.selectedItems()]
        yrange = [self.yvarmin_spin.value(), self.yvarmax_spin.value()]
        params = {}
        ransacparams = {}
        kws = {}
        try:
            modelkey = method + ' - ' + str(yvars[0][-1]) + ' (' + str(yrange[0]) + '-' + str(yrange[1]) + ') '
        except:
            modelkey = method
        try:
            if method == 'OLS':
                params = {'fit_intercept': self.ols.fitInterceptCheckBox.isChecked()}
                modelkey = modelkey + str(params)
                print(params)

            if method == 'OMP':
                params = {'fit_intercept': self.omp.fitInterceptCheckBox.isChecked(),
                          'n_nonzero_coefs': self.omp.numOfNonZeroCoeffsSpinBox.value(),
                          'CV': self.omp.optimizeWCrossValidationCheckBox.isChecked()}
                self.omp.numOfNonZeroCoeffsSpinBox.setDisabled(params['CV'])
                modelkey = modelkey + str(params)
                print(params)

            if method == 'Lasso':
                params = {'alpha': self.lasso.alphaDoubleSpinBox.value(),
                          'fit_intercept': self.lasso.fitInterceptCheckBox.isChecked(),
                          'max_iter': int(self.lasso.maxNumOfIterationsSpinBox.value()),
                          'tol': self.lasso.toleranceDoubleSpinBox.value(),
                          'positive': self.lasso.forcePositiveCoefficientsCheckBox.isChecked(),
                          'selection': 'random',
                          'CV': self.lasso.optimizeWCrossValidaitonCheckBox.isChecked()}
                self.lasso.alphaDoubleSpinBox.setDisabled(params['CV'])
                print(params)

            if method == 'Elastic Net':
                p_attrib = {'False': False, 'True': True, 'Array-like': 'array-like'}
                r_attrib = {'None': None}
                try:
                    r_state = int(self.elastic_net.randomStateLineEdit.text())
                except:
                    r_state = r_attrib[self.elastic_net.randomStateLineEdit.text()]

                index = self.elastic_net.precomputeComboBox.currentIndex()
                precomputeComboBox = self.elastic_net.precomputeComboBox.itemText(index)

                params = {'alpha': self.elastic_net.alphaDoubleSpinBox.value(),
                          'l1_ratio': self.elastic_net.l1RatioDoubleSpinBox.value(),
                          'fit_intercept': self.elastic_net.fitInterceptCheckBox.isChecked(),
                          'normalize': self.elastic_net.normalizeCheckBox.isChecked(),
                          'precompute': p_attrib[precomputeComboBox],
                          'max_iter': int(self.elastic_net.maxNumOfIterationsSpinBox.value()),
                          'copy_X': self.elastic_net.copyXCheckBox.isChecked(),
                          'tol': self.elastic_net.toleranceDoubleSpinBox.value(),
                          'warm_start': self.elastic_net.warmStartCheckBox.isChecked(),
                          'positive': self.elastic_net.positiveCheckBox.isChecked(),
                          'selection': self.elastic_net.selectionLineEdit.text(),
                          'random_state': r_state,
                          'CV': self.elastic_net.crossValidateCheckBox.isChecked()}
                self.elastic_net.alphaDoubleSpinBox.setDisabled(params['CV'])
                self.elastic_net.l1RatioDoubleSpinBox.setDisabled(params['CV'])
                print(params)

            if method == 'Ridge':
                m_attrib = {'None': None}
                r_attrib = {'None': None}
                try:
                    m_state = int(self.ridge.maxNumOfIterationslineEdit.text())
                except:
                    m_state = m_attrib[self.ridge.maxNumOfIterationslineEdit.text()]
                try:
                    r_state = int(self.ridge.randomStateLineEdit.text())
                except:
                    r_state = r_attrib[self.elastic_net.randomStateLineEdit.text()]

                index = self.ridge.solverComboBox.currentIndex()
                params = {'alpha': self.ridge.alphaDoubleSpinBox.value(),
                          'copy_X': self.ridge.copyXCheckBox.isChecked(),
                          'fit_intercept': self.ridge.fitInterceptCheckBox.isChecked(),
                          'max_iter': m_state,
                          'normalize': self.ridge.normalizeCheckBox.isChecked(),
                          'solver': self.ridge.solverComboBox.itemText(index),
                          'tol': self.ridge.toleranceDoubleSpinBox.value(),
                          'random_state': r_state}

                print(params)

            if method == 'Bayesian Ridge':
                params = {'n_iter': self.br.numOfIterationsSpinBox.value(),
                          'tol': self.br.toleranceDoubleSpinBox.value(),
                          'alpha_1': self.br.alpha1DoubleSpinBox.value(),
                          'alpha_2': self.br.alpha2DoubleSpinBox.value(),
                          'lambda_1': self.br.lambdaDoubleSpinBox.value(),
                          'lambda_2': self.br.lambdaDoubleSpinBox.value(),
                          'compute_score': self.br.computerScoreCheckBox.isChecked(),
                          'fit_intercept': self.br.fitInterceptCheckBox.isChecked(),
                          'normalize': self.br.normalizeCheckBox.isChecked(),
                          'copy_X': self.br.copyXCheckBox.isChecked(),
                          'verbose': self.br.verboseCheckBox.isChecked()}
                print(params)

            if method == 'ARD':
                params = {'n_iter': self.ard.numOfIterationsSpinBox.value(),
                          'tol': self.ard.toleranceDoubleSpinBox.value(),
                          'alpha_1': self.ard.alpha1DoubleSpinBox.value(),
                          'alpha_2': self.ard.alpha2DoubleSpinBox.value(),
                          'lambda_1': self.ard.lambdaDoubleSpinBox.value(),
                          'lambda_2': self.ard.lambdaDoubleSpinBox.value(),
                          'compute_score': self.ard.computerScoreCheckBox.isChecked(),
                          'threshold_lambda': self.ard.thresholdLambdaSpinBox.value(),
                          'fit_intercept': self.ard.fitInterceptCheckBox.isChecked(),
                          'normalize': self.ard.normalizeCheckBox.isChecked(),
                          'copy_X': self.ard.copyXCheckBox.isChecked(),
                          'verbose': self.ard.verboseCheckBox.isChecked()}
                print(params)

            if method == 'LARS':
                params = {'n_nonzero_coefs': self.lars.numOfNonzeroCoeffsSpinBox.value(),
                          'fit_intercept': self.lars.fitInterceptCheckBox.isChecked(),
                          'positive': self.lars.positiveCheckBox.isChecked(),
                          'verbose': self.lars.verboseCheckBox.isChecked(),
                          'normalize': self.lars.normalizeCheckBox.isChecked(),
                          'precompute': self.lars.precomputeCheckBox.isChecked(),
                          'copy_X': self.lars.copyXCheckBox.isChecked(),
                          'eps': self.lars.epsDoubleSpinBox.value(),
                          'fit_path': self.lars.fitPathCheckBox.isChecked(),
                          'CV': self.lars.crossValidateCheckBox.isChecked()}
                self.lars.numOfNonzeroCoeffsSpinBox.setDisabled(params['CV'])
                self.lars.fitPathCheckBox.setDisabled(params['CV'])
                print(params)

            if method == 'Lasso LARS':
                p_attrib = {'Auto': 'auto', 'True': True, 'False': False, 'Array-like': 'array-like'}
                index = self.lassoLARS.precomputeComboBox.currentIndex()
                precomputeComboBox = self.lassoLARS.precomputeComboBox.itemText(index)

                params = {'alpha': self.lassoLARS.alphaDoubleSpinBox.value(),
                          'fit_intercept': self.lassoLARS.fitInterceptCheckBox.isChecked(),
                          'positive': self.lassoLARS.positiveCheckBox.isChecked(),
                          'verbose': self.lassoLARS.verboseCheckBox.isChecked(),
                          'normalize': self.lassoLARS.normalizeCheckBox.isChecked(),
                          'copy_X': self.lassoLARS.copyXCheckBox.isChecked(),
                          'precompute': p_attrib[precomputeComboBox],
                          'max_iter': int(self.lassoLARS.maxIterationsSpinBox.value()),
                          'eps': self.lassoLARS.epsDoubleSpinBox.value(),
                          'fit_path': self.lassoLARS.fitInterceptCheckBox.isChecked(),
                          'model': self.lassoLARS.modelComboBox.currentIndex()}
                print(params)

            if method == 'SVR':
                gamma_index = self.svr.gammaComboBox.currentIndex()
                kernel_index = self.svr.kernelComboBox.currentIndex()
                params = {'C': self.svr.cDoubleSpinBox.value(),
                          'epsilon': self.svr.epsilonDoubleSpinBox.value(),
                          'kernel': self.svr.kernelComboBox.itemText(kernel_index),
                          'degree': self.svr.degreeSpinBox.value(),
                          'gamma': self.svr.gammaComboBox.itemText(gamma_index),
                          'coef0': self.svr.coeff0DoubleSpinBox.value(),
                          'shrinking': self.svr.shrinkingCheckBox.isChecked(),
                          'tol': self.svr.toleranceDoubleSpinBox.value(),
                          'cache_size': self.svr.cacheSizeSpinBox.value(),
                          'verbose': self.svr.verboseCheckBox.isChecked(),
                          'max_iter': int(self.svr.maxIterationsSpinBox.value())}
                print(params)

            if method == 'KRR':
                k_attrib = {'None': None}
                params = {'alpha': self.krr.alphaSpinBox.value(),
                          'kernel': self.krr.kernelLineEdit.text(),
                          'gamma': self.krr.gammaLineEdit.text(),
                          'degree': self.krr.degreeDoubleSpinBox.value(),
                          'coef0': self.krr.coeff0DoubleSpinBox.value(),
                          'kernel_params': k_attrib[self.krr.kernelParametersLineEdit.text()]}
                print(params)

            if method == 'PLS':
                params = {'n_components': self.pls.numOfComponentsSpinBox.value(),
                          'scale': False}
                modelkey = modelkey + '(nc=' + str(params['n_components']) + ')'
                print(params)

            if method == 'GP':
                index = self.gp.chooseDimensionalityReductionMethodComboBox.currentIndex()
                params = {'reduce_dim': self.gp.chooseDimensionalityReductionMethodComboBox.itemText(index),
                          'n_components': self.gp.numOfComponentsSpinBox.value(),
                          'random_start': self.gp.numOfRandomStartsSpinBox.value(),
                          'theta0': self.gp.startingThetaDoubleSpinBox.value(),
                          'thetaL': self.gp.lowerBoundOnThetaDoubleSpinBox.value(),
                          'thetaU': self.gp.upperBoundOnThetaDoubleSpinBox.value()}

                modelkey = modelkey + str(params)
                print(params)

        except Exception as e:
            print(e)

        kws = {'modelkey': modelkey}
        ui_list = "do_regression_train"
        fun_list = "do_regression_train"

        args = [datakey, xvars, yvars, yrange, method, params, ransacparams]
        # TODO Stop the module when there are ill-formed parameters!
        self.r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, self.r, self.ui_id)

    def set_regression_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guiRestore(self.restr_list)
        if self.arg_list is not None:
            try:
                self.datakey = self.arg_list[0]
                self.xvars = self.arg_list[1]
                self.yvars = self.arg_list[2]
                yrange = self.arg_list[3]
                method = self.arg_list[4]
                params = self.arg_list[5]
                ransacparams = self.arg_list[6]

                change_combo_list_vars(self.regression_train_choosey,
                                       self.restr_list['regression_train_choosey_values'])
                self.regression_choosedata.setCurrentIndex(self.regression_choosedata.findText(str(self.datakey)))
                change_combo_list_vars(self.regression_train_choosey,
                                       self.restr_list['regression_train_choosey_values'])
                change_combo_list_vars(self.regression_train_choosex,
                                       self.restr_list['regression_train_choosex_values'])

                try:
                    self.regression_train_choosex.setCurrentItem(
                        self.regression_train_choosex.findItems(self.xvars[0], QtCore.Qt.MatchExactly)[0])
                    self.regression_train_choosey.setCurrentItem(
                        self.regression_train_choosey.findItems(self.yvars[0][1], QtCore.Qt.MatchExactly)[0])
                except:
                    pass
                self.yvarmin_spin.setValue(yrange[0])
                self.yvarmax_spin.setValue(yrange[1])
                self.regression_choosealg.setCurrentIndex(self.regression_choosealg.findText(str(method)))
                self.make_regression_widget(self.regression_choosealg.currentText(), params=params)
            except:
                pass

    def make_ransac_widget(self, isChecked):
        if not isChecked:
            self.ransac_widget.deleteLater()
        else:
            self.ransac_widget = QtWidgets.QWidget()
            self.ransac_widget.ransac_widget_hlayout = QtWidgets.QHBoxLayout(self.ransac_widget)
            self.ransac_widget.ransac_lossfunc_hlayout = QtWidgets.QHBoxLayout()
            self.ransac_widget.ransac_lossfunc_label = QtWidgets.QLabel(self.ransac_widget)
            self.ransac_widget.ransac_lossfunc_label.setText('Loss function:')
            self.ransac_widget.ransac_lossfunc_label.setObjectName("self.ransac_lossfunc_label")
            self.ransac_widget.ransac_lossfunc_hlayout.addWidget(self.ransac_widget.ransac_lossfunc_label)
            self.ransac_widget.ransac_lossfunc_combobox = QtWidgets.QComboBox(self.ransac_widget)
            self.ransac_widget.ransac_lossfunc_combobox.addItem(("Squared Error"))
            self.ransac_widget.ransac_lossfunc_combobox.addItem(("Absolute Error"))
            self.ransac_widget.ransac_lossfunc_combobox.setObjectName("self.ransac_lossfunc_combobox")
            self.ransac_widget.ransac_lossfunc_hlayout.addWidget(self.ransac_widget.ransac_lossfunc_combobox)
            self.ransac_widget.ransac_lossfunc_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                              QtWidgets.QSizePolicy.Minimum)
            self.ransac_widget.ransac_lossfunc_hlayout.addItem(self.ransac_widget.ransac_lossfunc_spacer)
            self.ransac_widget.ransac_widget_hlayout.addLayout(self.ransac_widget.ransac_lossfunc_hlayout)
            self.ransac_widget.ransac_thresh_hlayout = QtWidgets.QHBoxLayout()
            self.ransac_widget.ransac_thresh_label = QtWidgets.QLabel(self.ransac_widget)
            self.ransac_widget.ransac_thresh_label.setText('Threshold:')
            self.ransac_widget.ransac_thresh_label.setObjectName("self.ransac_thresh_label")
            self.ransac_widget.ransac_thresh_hlayout.addWidget(self.ransac_widget.ransac_thresh_label)
            self.ransac_widget.ransac_thresh_spin = QtWidgets.QDoubleSpinBox(self.ransac_widget)
            self.ransac_widget.ransac_thresh_spin.setObjectName("self.ransac_thresh_spin")
            self.ransac_widget.ransac_thresh_hlayout.addWidget(self.ransac_widget.ransac_thresh_spin)
            self.ransac_widget.ransac_thresh_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                            QtWidgets.QSizePolicy.Minimum)
            self.ransac_widget.ransac_thresh_hlayout.addItem(self.ransac_widget.ransac_thresh_spacer)
            self.ransac_widget.ransac_widget_hlayout.addLayout(self.ransac_widget.ransac_thresh_hlayout)
            self.ransac_widget.setObjectName("ransac_widget")
            self.ransac_hlayout.addWidget(self.ransac_widget)

            self.ransac_widget.ransac_lossfunc_combobox.currentIndexChanged.connect(
                lambda: self.get_regression_parameters())
            self.ransac_widget.ransac_thresh_spin.valueChanged.connect(lambda: self.get_regression_parameters())

    def make_regression_widget(self, alg, params=None):
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget = QtWidgets.QWidget()

        if alg == self.algorithm_list[1]:
            self.pls = PLS.Ui_Form()
            self.pls.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.pls, self.get_regression_parameters)

        if alg == self.algorithm_list[2]:
            self.gp = GP.Ui_Form()
            self.gp.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.gp, self.get_regression_parameters)

        if alg == self.algorithm_list[3]:
            self.ols = OLS.Ui_Form()
            self.ols.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.ols, self.get_regression_parameters)

            if params is not None:
                self.ols.fitInterceptCheckBox.setChecked(params['fit_intercept'])

        if alg == self.algorithm_list[4]:
            self.omp = OMP.Ui_Form()
            self.omp.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.omp, self.get_regression_parameters)

            if params is not None:
                self.omp.fitInterceptCheckBox.setChecked(params['fit_intercept'])
                self.omp.optimizeWCrossValidationCheckBox.setChecked(params['CV'])
                self.omp.numOfNonZeroCoeffsSpinBox.setValue(params['n_nonzero_coefs'])

        if alg == self.algorithm_list[5]:
            self.lasso = Lasso.Ui_Form()
            self.lasso.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.lasso, self.get_regression_parameters)

            # if params is not None:
            # self..lasso_alpha.setValue(params['alpha'])
            # self..lasso_intercept_checkbox.setChecked(params['fit_intercept'])
            # self..lasso_tol.setValue(params['tol'])
            # self..lasso_max.setValue(params['max_iter'])
            # self..lasso_positive_checkbox.setChecked(params['positive'])
            # self..lasso_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[6]:
            self.elastic_net = ElasticNet.Ui_Form()
            self.elastic_net.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.elastic_net, self.get_regression_parameters)

            # if params is not None:
            # self..elnet_alpha.setValue(params['alpha'])
            # self..elnet_l1.setValue(params['l1_ratio'])
            # self..elnet_intercept_checkbox.setChecked(params['fit_intercept'])
            # self..elnet_tol.setValue(params['tol'])
            # self..elnet_max.setValue(params['max_iter'])
            # self..elnet_positive_checkbox.setChecked(params['positive'])
            # self..elnet_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[7]:
            self.ridge = Ridge.Ui_Form()
            self.ridge.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.ridge, self.get_regression_parameters)

        if alg == self.algorithm_list[8]:
            self.br = bayesian_ridge.Ui_Form()
            self.br.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.br, self.get_regression_parameters)

            # if params is not None:
            # self..ridge_alpha.setValue(params['alpha'])
            # self..ridge_intercept_checkbox.setChecked(params['fit_intercept'])
            # self..ridge_tol.setValue(params['tol'])
            # self..ridge_max.setValue(params['max_iter'])
            # self..ridge_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[9]:
            self.ard = ARD.Ui_Form()
            self.ard.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.ard, self.get_regression_parameters)

        if alg == self.algorithm_list[10]:
            self.lars = LARS.Ui_Form()
            self.lars.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.lars, self.get_regression_parameters)

        if alg == self.algorithm_list[11]:
            self.lassoLARS = LassoLARS.Ui_Form()
            self.lassoLARS.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.lassoLARS, self.get_regression_parameters)

            # if params is not None:
            # self..lassoLARS_alpha.setValue(params['alpha'])
            # self..lassoLARS_intercept_checkbox.setChecked(params['fit_intercept'])
            # self..lassoLARS_max.setValue(params['max_iter'])
            # self..lassoLARS_positive_checkbox.setChecked(params['positive'])
            # self..lassoLARS_cv_checkbox.setChecked(params['CV'])

        if alg == self.algorithm_list[12]:
            self.svr = SVR.Ui_Form()
            self.svr.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.svr, self.get_regression_parameters)

        if alg == self.algorithm_list[13]:
            self.krr = KRR.Ui_Form()
            self.krr.setupUi(self.reg_widget)
            self.qtickle.isGuiChanged(self.krr, self.get_regression_parameters)

        self.reg_widget.setObjectName("")
        self.regression_vlayout.addWidget(self.reg_widget)
        self.get_regression_parameters()

    def regression_ui(self):
        self.regression_train = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regression_train.setFont(font)
        self.regression_vlayout = QtWidgets.QVBoxLayout(self.regression_train)
        # choose data
        self.regression_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.regression_train_choosedata_label = QtWidgets.QLabel(self.regression_train)
        self.regression_train_choosedata_label.setText("Choose data:")
        self.regression_train_choosedata_label.setObjectName("regression_train_choosedata_label")
        self.regression_choosedata_hlayout.addWidget(self.regression_train_choosedata_label)
        datachoices = self.pysat_fun.datakeys
        datachoices = [i for i in datachoices if i != 'CV Results']  # prevent CV results from showing up as an option

        self.regression_choosedata = make_combobox(datachoices)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName("regression_choosedata")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.regression_vlayout.addLayout(self.regression_choosedata_hlayout)
        # choose variables
        self.regression_choosevars_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosexvars_vlayout = QtWidgets.QVBoxLayout()
        self.regression_chooseyvars_vlayout = QtWidgets.QVBoxLayout()
        self.regression_choosevars_hlayout.addLayout(self.regression_choosexvars_vlayout)
        self.regression_choosevars_hlayout.addLayout(self.regression_chooseyvars_vlayout)
        # choose x variables
        self.regression_train_choosex_label = QtWidgets.QLabel(self.regression_train)
        self.regression_train_choosex_label.setText('X variable:')
        self.regression_train_choosex_label.setObjectName("regression_train_choosex_label")
        self.regression_choosexvars_vlayout.addWidget(self.regression_train_choosex_label)
        self.regression_train_choosex = make_listwidget(self.xvar_choices())
        self.regression_train_choosex.setObjectName("regression_train_choosex")
        self.regression_choosexvars_vlayout.addWidget(self.regression_train_choosex)

        # choose y variables
        self.regression_train_choosey_label = QtWidgets.QLabel(self.regression_train)
        self.regression_train_choosey_label.setText('Y variable:')
        self.regression_train_choosey_label.setObjectName("regression_train_choosey_label")
        self.regression_chooseyvars_vlayout.addWidget(self.regression_train_choosey_label)
        if self.isRestore == True:
            self.regression_train_choosey = make_listwidget([])
        else:
            self.regression_train_choosey = make_listwidget(self.yvar_choices())
        # TODO add ability to select multiple items
        # self.regression_train_choosey.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.regression_train_choosey.setObjectName("regression_train_choosey")
        self.regression_chooseyvars_vlayout.addWidget(self.regression_train_choosey)
        self.regression_yvarlimits_hlayout = QtWidgets.QHBoxLayout()
        self.yvarmin_label = QtWidgets.QLabel(self.regression_train)
        self.yvarmin_label.setText('Min:')
        self.yvarmin_label.setObjectName("yvarmin_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.yvarmin_spin = QtWidgets.QDoubleSpinBox()
        # TODO: eventually we may want the ability to handle values outside 0-100 for regressions not dealing with wt.%
        self.yvarmin_spin.setMaximum(99999)
        self.yvarmin_spin.setMinimum(0)
        self.yvarmin_label.setObjectName("yvarmin_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmin_label)
        self.yvarmin_spin.setObjectName("yvarmin_spin")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmin_spin)

        self.yvarmax_label = QtWidgets.QLabel(self.regression_train)
        self.yvarmax_label.setText('Max:')
        self.yvarmax_label.setObjectName("yvarmax_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.yvarmax_spin = QtWidgets.QDoubleSpinBox()
        self.yvarmax_spin.setMaximum(99999)
        self.yvarmax_spin.setMinimum(0)
        self.yvarmax_spin.setValue(100)
        self.yvarmax_label.setObjectName("yvarmax_label")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmax_label)
        self.yvarmax_spin.setObjectName("yvarmax_spin")
        self.regression_yvarlimits_hlayout.addWidget(self.yvarmax_spin)
        self.regression_chooseyvars_vlayout.addLayout(self.regression_yvarlimits_hlayout)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosevars_hlayout.addItem(spacerItem1)
        self.regression_vlayout.addLayout(self.regression_choosevars_hlayout)

        # ransac options
        # self.ransac_hlayout = QtWidgets.QHBoxLayout()
        # self.regression_ransac_checkbox = QtWidgets.QCheckBox(self.regression_train)
        # self.regression_ransac_checkbox.setText('RANSAC')
        # self.ransac_hlayout.addWidget(self.regression_ransac_checkbox)
        # self.regression_vlayout.addLayout(self.ransac_hlayout)

        # choose regression algorithm
        self.regression_choosealg_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosealg_label = QtWidgets.QLabel(self.regression_train)
        self.regression_choosealg_label.setObjectName("regression_choosealg_label")
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg_label)
        self.regression_alg_choices = self.algorithm_list
        self.regression_choosealg = make_combobox(self.regression_alg_choices)
        self.regression_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosealg.setObjectName("regression_choosealg")
        self.regression_choosealg_hlayout.addWidget(self.regression_choosealg)
        regression_choosealg_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum)
        self.regression_choosealg_hlayout.addItem(regression_choosealg_spacer)
        self.regression_vlayout.addLayout(self.regression_choosealg_hlayout)
        self.regression_train.setObjectName("regression_train")
        self.module_layout.addWidget(self.regression_train)
        self.regression_train.raise_()
        self.regression_train.setTitle(("Regression - Train"))

    def connectWidgets(self):
        self.regression_choosedata.currentIndexChanged.connect(lambda: self.get_regression_parameters())
        self.regression_choosealg.currentIndexChanged.connect(lambda: self.get_regression_parameters())
        self.regression_train_choosex.currentItemChanged.connect(lambda: self.get_regression_parameters())
        self.regression_train_choosey.currentItemChanged.connect(lambda: self.get_regression_parameters())
        self.yvarmin_spin.valueChanged.connect(lambda: self.get_regression_parameters())
        self.yvarmax_spin.valueChanged.connect(lambda: self.get_regression_parameters())
        self.regression_choosedata.activated[int].connect(
            lambda: change_combo_list_vars(self.regression_train_choosey, self.yvar_choices()))
        self.regression_choosedata.activated[int].connect(
            lambda: change_combo_list_vars(self.regression_train_choosex, self.xvar_choices()))

    def yvar_choices(self):
        try:
            yvarchoices = self.pysat_fun.data[self.regression_choosedata.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def xvar_choices(self):
        try:
            xvarchoices = self.pysat_fun.data[self.regression_choosedata.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices
