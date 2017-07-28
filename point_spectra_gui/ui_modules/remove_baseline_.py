import traceback
import inspect

from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.gui_utils import make_combobox
from point_spectra_gui.ui_modules.Error_ import error_print


class remove_baseline_:
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
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, self.ui_id)
        self.baseline_ui()  # start the baseline UI. create our submodule
        self.set_baseline_parameters()
        # self.baseline_ransac_checkbox.toggled.connect(  #
        #     lambda: self.make_ransac_widget(self.baseline_ransac_checkbox.isChecked()))  #
        self.baseline_choosealg.currentIndexChanged.connect(  #
            lambda: self.make_baseline_widget(self.baseline_choosealg.currentText()))  #
        self.get_baseline_parameters()
        self.pysat_fun.set_greyed_modules(self.remove_baseline)

    def get_baseline_parameters(self):
        method = self.baseline_choosealg.currentText()
        datakey = self.baseline_choosedata.currentText()
        params = {}
        kws = {}
        self.baseline_alg_choices = ['Choose an algorithm', 'ALS', 'Dietrich', 'Polyfit', 'AirPLS', 'FABC', 'KK',
                                     'Mario', 'Median', 'Rubberband', 'CCAM']
        try:
            if method == 'ALS':
                params = {'asymmetry_param': self.br_widget.als_asym_spinbox.value(),
                          'smoothness_param': self.br_widget.als_smooth_spinbox.value(),
                          'max_iters': self.br_widget.als_iters_spinbox.value(),
                          'conv_thresh': self.br_widget.als_conv_spinbox.value()}

            if method == 'Dietrich':
                self.br_widget.dietrich_half_win_spinbox.setValue(params['half_window'])
                self.br_widget.dietrich_erosions_spinbox.setValue(params['num_erosions'])

                params = {'half_window': self.br_widget.dietrich_half_win_spinbox.value(),
                          'num_erosions': self.br_widget.dietrich_erosions_spinbox.value()}

            if method == 'Polyfit':
                params = {'poly_order': self.br_widget.polyfit_order_spinbox.value(),
                          'num_stdev': self.br_widget.polyfit_nstdev_spinbox.value(),
                          'max_iter': self.br_widget.polyfit_iter_spinbox.value()}

            if method == 'AirPLS':
                params = {'smoothness_param': self.br_widget.airpls_smoothness_spinbox.value(),
                          'conv_thresh': self.br_widget.airpls_conv_spinbox.value(),
                          'max_iters': self.br_widget.airpls_iter_spinbox.value()}

            if method == 'FABC':
                params = {'smoothness_param': self.br_widget.fabc_smoothness_spinbox.value(),
                          'dilation_param': self.br_widget.fabc_dilation_spinbox.value()}

            if method == 'KK':
                params = {'top_width': self.br_widget.kk_top_width_spinbox.value(),
                          'bottom_width': self.br_widget.kk_bottom_width_spinbox.value(),
                          'tangent': self.br_widget.kk_tan_checkbox.isChecked(),
                          'exponent': self.br_widget.kk_exp_spinbox.value()}

            if method == 'Mario':
                params = {'poly_order': self.br_widget.mario_order_spinbox.value(),
                          'max_iters': self.br_widget.mario_iters_spinbox.value(),
                          'tol': self.br_widget.mario_tol_spinbox.value()}

            if method == 'Median':
                params = {'window_size': self.br_widget.median_window_spinbox.value()}

            if method == 'Rubberband':
                params = {'num_iters': self.br_widget.rubberband_iters_spinbox.value(),
                          'num_ranges': self.br_widget.rubberband_ranges_spinbox.value()}

            if method == 'CCAM':
                params = {'scale1': self.br_widget.ccam_scale1_spinbox.value(),
                          'scale2': self.br_widget.ccam_scale2_spinbox.value()}

                int_flag = self.br_widget.ccam_interp_combobox.currentText()
                if int_flag == 'Linear':
                    params['int_flag'] = 0
                elif int_flag == 'Quadratic':
                    params['int_flag'] = 1
                elif int_flag == 'Spline':
                    params['int_flag'] = 2


        except:
            pass
        kws = {}
        ui_list = "do_remove_baseline"
        fun_list = "do_remove_baseline"

        args = [datakey, method, params]
        r = self.qtickle.guiSave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def set_baseline_parameters(self):
        if self.restr_list is not None:
            self.qtickle.guiRestore(self.restr_list)
        if self.arg_list is not None:
            try:
                datakey = self.arg_list[0]
                method = self.arg_list[1]
                params = self.arg_list[2]

                self.baseline_choosedata.setCurrentIndex(self.baseline_choosedata.findText(str(datakey)))
                # TODO:
                self.baseline_choosealg.setCurrentIndex(self.baseline_choosealg.findText(str(method)))
                self.make_baseline_widget(self.baseline_choosealg.currentText(), params=params)
                self.get_baseline_parameters()
            except Exception as e:
                print(e)

    def make_baseline_widget(self, alg, params=None):
        print(alg)

        try:
            self.br_widget.deleteLater()
        except:
            pass
        self.br_widget = QtWidgets.QWidget()
        if alg == 'ALS':
            self.br_widget.als_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.als_asym_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.als_asym_label.setText('Asymmetry:')
            self.br_widget.als_asym_label.setObjectName("self.br_widget.als_asym_label")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_asym_label)
            self.br_widget.als_asym_spinbox = QtWidgets.QDoubleSpinBox(self.br_widget)
            self.br_widget.als_asym_spinbox.setObjectName("self.br_widget.als_asym_spinbox")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_asym_spinbox)
            self.br_widget.als_asym_spinbox.setRange(0, 1)
            self.br_widget.als_asym_spinbox.setValue(0.05)
            self.br_widget.als_asym_spinbox.setSingleStep(0.1)

            self.br_widget.als_smooth_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.als_smooth_label.setText('Smoothness:')
            self.br_widget.als_smooth_label.setObjectName("self.br_widget.als_smooth_label")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_smooth_label)
            self.br_widget.als_smooth_spinbox = QtWidgets.QDoubleSpinBox(self.br_widget)
            self.br_widget.als_smooth_spinbox.setObjectName("self.br_widget.als_smooth_spinbox")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_smooth_spinbox)
            self.br_widget.als_smooth_spinbox.setRange(0, 1e10)
            self.br_widget.als_smooth_spinbox.setDecimals(2)
            self.br_widget.als_smooth_spinbox.setValue(1e6)
            self.br_widget.als_smooth_spinbox.setSingleStep(1e5)

            self.br_widget.als_iters_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.als_iters_label.setText('Maximum # of iterations:')
            self.br_widget.als_iters_label.setObjectName("self.br_widget.als_iters_label")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_iters_label)
            self.br_widget.als_iters_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.als_iters_spinbox.setObjectName("self.br_widget.als_iters_spinbox")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_iters_spinbox)
            self.br_widget.als_iters_spinbox.setRange(1, 1000)
            self.br_widget.als_iters_spinbox.setValue(10)
            self.br_widget.als_iters_spinbox.setSingleStep(1)

            self.br_widget.als_conv_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.als_conv_label.setText('Convergence threshold:')
            self.br_widget.als_conv_label.setObjectName("self.br_widget.als_conv_label")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_conv_label)
            self.br_widget.als_conv_spinbox = QtWidgets.QDoubleSpinBox(self.br_widget)
            self.br_widget.als_conv_spinbox.setObjectName("self.br_widget.als_conv_spinbox")
            self.br_widget.als_hlayout.addWidget(self.br_widget.als_conv_spinbox)
            self.br_widget.als_conv_spinbox.setRange(0, 1)
            self.br_widget.als_conv_spinbox.setDecimals(6)
            self.br_widget.als_conv_spinbox.setValue(1e-5)
            self.br_widget.als_conv_spinbox.setSingleStep(1e-6)

            if params is not None:
                self.br_widget.als_asym_spinbox.setValue(params['asymmetry_param'])
                self.br_widget.als_smooth_spinbox.setValue(params['smoothness_param'])
                self.br_widget.als_iters_spinbox.setValue(params['max_iters'])
                self.br_widget.als_conv_spinbox.setValue(params['conv_thresh'])


        elif alg == 'Dietrich':
            self.br_widget.dietrich_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.dietrich_half_win_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.dietrich_half_win_label.setText('Half-window:')
            self.br_widget.dietrich_half_win_label.setObjectName("self.br_widget.dietrich_half_win_label")
            self.br_widget.dietrich_hlayout.addWidget(self.br_widget.dietrich_half_win_label)
            self.br_widget.dietrich_half_win_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.dietrich_half_win_spinbox.setObjectName("self.br_widget.dietrich_half_win_spinbox")
            self.br_widget.dietrich_hlayout.addWidget(self.br_widget.dietrich_half_win_spinbox)

            self.br_widget.dietrich_half_win_spinbox.setRange(1, 1000)
            self.br_widget.dietrich_half_win_spinbox.setValue(16)
            self.br_widget.dietrich_half_win_spinbox.setSingleStep(1)

            self.br_widget.dietrich_erosions_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.dietrich_erosions_label.setText('# of Erosions:')
            self.br_widget.dietrich_erosions_label.setObjectName("self.br_widget.dietrich_erosions_label")
            self.br_widget.dietrich_hlayout.addWidget(self.br_widget.dietrich_erosions_label)
            self.br_widget.dietrich_erosions_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.dietrich_erosions_spinbox.setObjectName("self.br_widget.dietrich_erosions_spinbox")
            self.br_widget.dietrich_hlayout.addWidget(self.br_widget.dietrich_erosions_spinbox)
            self.br_widget.dietrich_erosions_spinbox.setRange(0, 1000)
            self.br_widget.dietrich_erosions_spinbox.setValue(10)

            self.br_widget.dietrich_erosions_spinbox.setSingleStep(1)
            if params is not None:
                self.br_widget.dietrich_half_win_spinbox.setValue(params['half_window'])
                self.br_widget.dietrich_erosions_spinbox.setValue(params['num_erosions'])


        elif alg == 'Polyfit':
            self.br_widget.polyfit_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.polyfit_order_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.polyfit_order_label.setText('Order:')
            self.br_widget.polyfit_order_label.setObjectName("self.br_widget.polyfit_order_label")
            self.br_widget.polyfit_hlayout.addWidget(self.br_widget.polyfit_order_label)
            self.br_widget.polyfit_order_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.polyfit_order_spinbox.setObjectName("self.br_widget.polyfit_order_spinbox")
            self.br_widget.polyfit_hlayout.addWidget(self.br_widget.polyfit_order_spinbox)
            self.br_widget.polyfit_order_spinbox.setValue(5)
            self.br_widget.polyfit_order_spinbox.setRange(1, 100)
            self.br_widget.polyfit_order_spinbox.setSingleStep(1)

            self.br_widget.polyfit_nstdev_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.polyfit_nstdev_label.setText('# of standard deviations:')
            self.br_widget.polyfit_nstdev_label.setObjectName("self.br_widget.polyfit_nstdev_label")
            self.br_widget.polyfit_hlayout.addWidget(self.br_widget.polyfit_nstdev_label)
            self.br_widget.polyfit_nstdev_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.polyfit_nstdev_spinbox.setObjectName("self.br_widget.polyfit_nstdev_spinbox")
            self.br_widget.polyfit_hlayout.addWidget(self.br_widget.polyfit_nstdev_spinbox)
            self.br_widget.polyfit_nstdev_spinbox.setValue(3)
            self.br_widget.polyfit_nstdev_spinbox.setRange(1, 100)
            self.br_widget.polyfit_nstdev_spinbox.setSingleStep(1)

            self.br_widget.polyfit_iter_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.polyfit_iter_label.setText('Max # of iterations:')
            self.br_widget.polyfit_iter_label.setObjectName("self.br_widget.polyfit_iter_label")
            self.br_widget.polyfit_hlayout.addWidget(self.br_widget.polyfit_iter_label)
            self.br_widget.polyfit_iter_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.polyfit_iter_spinbox.setObjectName("self.br_widget.polyfit_iter_spinbox")
            self.br_widget.polyfit_hlayout.addWidget(self.br_widget.polyfit_iter_spinbox)
            self.br_widget.polyfit_iter_spinbox.setRange(1, 10000)
            self.br_widget.polyfit_iter_spinbox.setValue(200)

            self.br_widget.polyfit_iter_spinbox.setSingleStep(1)

            if params is not None:
                self.br_widget.polyfit_order_spinbox.setValue(params['poly_order'])
                self.br_widget.polyfit_nstdev_spinbox.setValue(params['num_stdev'])
                self.br_widget.polyfit_iter_spinbox.setValue(params['max_iter'])

        elif alg == 'AirPLS':
            self.br_widget.airpls_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.airpls_smoothness_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.airpls_smoothness_label.setText('Smoothness:')
            self.br_widget.airpls_smoothness_label.setObjectName("self.br_widget.airpls_smoothness_label")
            self.br_widget.airpls_hlayout.addWidget(self.br_widget.airpls_smoothness_label)
            self.br_widget.airpls_smoothness_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.airpls_smoothness_spinbox.setObjectName("self.br_widget.airpls_smoothness_spinbox")
            self.br_widget.airpls_hlayout.addWidget(self.br_widget.airpls_smoothness_spinbox)
            self.br_widget.airpls_smoothness_spinbox.setRange(1, 10000)
            self.br_widget.airpls_smoothness_spinbox.setValue(100)

            self.br_widget.airpls_smoothness_spinbox.setSingleStep(1)

            self.br_widget.airpls_iter_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.airpls_iter_label.setText('Max # of iterations:')
            self.br_widget.airpls_iter_label.setObjectName("self.br_widget.airpls_iter_label")
            self.br_widget.airpls_hlayout.addWidget(self.br_widget.airpls_iter_label)
            self.br_widget.airpls_iter_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.airpls_iter_spinbox.setObjectName("self.br_widget.airpls_iter_spinbox")
            self.br_widget.airpls_hlayout.addWidget(self.br_widget.airpls_iter_spinbox)
            self.br_widget.airpls_iter_spinbox.setRange(1, 10000)
            self.br_widget.airpls_iter_spinbox.setValue(10)

            self.br_widget.airpls_iter_spinbox.setSingleStep(1)

            self.br_widget.airpls_conv_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.airpls_conv_label.setText('Convergence threshold:')
            self.br_widget.airpls_conv_label.setObjectName("self.br_widget.airpls_conv_label")
            self.br_widget.airpls_hlayout.addWidget(self.br_widget.airpls_conv_label)
            self.br_widget.airpls_conv_spinbox = QtWidgets.QDoubleSpinBox(self.br_widget)
            self.br_widget.airpls_conv_spinbox.setObjectName("self.br_widget.airpls_conv_spinbox")
            self.br_widget.airpls_hlayout.addWidget(self.br_widget.airpls_conv_spinbox)
            self.br_widget.airpls_conv_spinbox.setRange(0, 100)
            self.br_widget.airpls_conv_spinbox.setDecimals(4)
            self.br_widget.airpls_conv_spinbox.setValue(0.001)

            self.br_widget.airpls_conv_spinbox.setSingleStep(0.01)

            if params is not None:
                self.br_widget.airpls_smoothness_spinbox.setValue(params['smoothness_param'])
                self.br_widget.airpls_conv_spinbox.setValue(params['conv_thresh'])
                self.br_widget.airpls_iter_spinbox.setValue(params['max_iters'])

        elif alg == 'FABC':

            self.br_widget.fabc_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.fabc_smoothness_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.fabc_smoothness_label.setText('Smoothness:')
            self.br_widget.fabc_smoothness_label.setObjectName("self.br_widget.fabc_smoothness_label")
            self.br_widget.fabc_hlayout.addWidget(self.br_widget.fabc_smoothness_label)
            self.br_widget.fabc_smoothness_spinbox = QtWidgets.QDoubleSpinBox(self.br_widget)
            self.br_widget.fabc_smoothness_spinbox.setObjectName("self.br_widget.fabc_smoothness_spinbox")
            self.br_widget.fabc_hlayout.addWidget(self.br_widget.fabc_smoothness_spinbox)
            self.br_widget.fabc_smoothness_spinbox.setRange(1, 1e6)
            self.br_widget.fabc_smoothness_spinbox.setValue(1e3)
            self.br_widget.fabc_smoothness_spinbox.setSingleStep(1e2)

            self.br_widget.fabc_dilation_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.fabc_dilation_label.setText('Dilation:')
            self.br_widget.fabc_dilation_label.setObjectName("self.br_widget.fabc_dilation_label")
            self.br_widget.fabc_hlayout.addWidget(self.br_widget.fabc_dilation_label)
            self.br_widget.fabc_dilation_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.fabc_dilation_spinbox.setObjectName("self.br_widget.fabc_dilation_spinbox")
            self.br_widget.fabc_hlayout.addWidget(self.br_widget.fabc_dilation_spinbox)
            self.br_widget.fabc_dilation_spinbox.setRange(1, 1000)
            self.br_widget.fabc_dilation_spinbox.setValue(50)
            self.br_widget.fabc_dilation_spinbox.setSingleStep(1)

            if params is not None:
                self.br_widget.fabc_smoothness_spinbox.setValue(params['smoothness_param'])
                self.br_widget.fabc_dilation_spinbox.setValue(params['dilation_param'])

        if alg == 'KK':
            '''bands, intensities, top_width=0,
                             bottom_width=50, exponent=2,
                             tangent=False'''
            self.br_widget.kk_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.kk_top_width_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.kk_top_width_label.setText('Top width:')
            self.br_widget.kk_top_width_label.setObjectName("self.br_widget.kk_top_width_label")
            self.br_widget.kk_hlayout.addWidget(self.br_widget.kk_top_width_label)
            self.br_widget.kk_top_width_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.kk_top_width_spinbox.setObjectName("self.br_widget.kk_top_width_spinbox")
            self.br_widget.kk_hlayout.addWidget(self.br_widget.kk_top_width_spinbox)
            self.br_widget.kk_top_width_spinbox.setValue(0)
            self.br_widget.kk_top_width_spinbox.setRange(0, 100000)
            self.br_widget.kk_top_width_spinbox.setSingleStep(1)

            self.br_widget.kk_bottom_width_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.kk_bottom_width_label.setText('Bottom width:')
            self.br_widget.kk_bottom_width_label.setObjectName("self.br_widget.kk_bottom_width_label")
            self.br_widget.kk_hlayout.addWidget(self.br_widget.kk_bottom_width_label)
            self.br_widget.kk_bottom_width_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.kk_bottom_width_spinbox.setObjectName("self.br_widget.kk_bottom_width_spinbox")
            self.br_widget.kk_hlayout.addWidget(self.br_widget.kk_bottom_width_spinbox)
            self.br_widget.kk_bottom_width_spinbox.setValue(50)
            self.br_widget.kk_bottom_width_spinbox.setRange(0, 100000)
            self.br_widget.kk_bottom_width_spinbox.setSingleStep(1)

            self.br_widget.kk_exp_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.kk_exp_label.setText('Exponent:')
            self.br_widget.kk_exp_label.setObjectName("self.br_widget.kk_exp_label")
            self.br_widget.kk_hlayout.addWidget(self.br_widget.kk_exp_label)
            self.br_widget.kk_exp_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.kk_exp_spinbox.setObjectName("self.br_widget.kk_exp_spinbox")
            self.br_widget.kk_hlayout.addWidget(self.br_widget.kk_exp_spinbox)
            self.br_widget.kk_exp_spinbox.setValue(2)
            self.br_widget.kk_exp_spinbox.setRange(1, 100)
            self.br_widget.kk_exp_spinbox.setSingleStep(1)

            self.br_widget.kk_tan_checkbox = QtWidgets.QCheckBox(self.br_widget)
            self.br_widget.kk_tan_checkbox.setText('Tangent ')
            self.br_widget.kk_tan_checkbox.setChecked(False)
            self.br_widget.kk_tan_checkbox.setObjectName("self.br_widget.kk_tan_checkbox")
            self.br_widget.kk_hlayout.addWidget(self.br_widget.kk_tan_checkbox)

            if params is not None:
                self.br_widget.kk_top_width_spinbox.setValue(params['top_width'])
                self.br_widget.kk_bottom_width_spinbox.setValue(params['bottom_width'])
                self.br_widget.kk_tan_checkbox.setChecked(params['tangent'])
                self.br_widget.kk_exp_spinbox.setValue(params['exponent'])
            pass
        if alg == 'Mario':
            '''bands, intensities, poly_order=10, max_iters=None,
                   verbose=False, tol=1e-2'''
            self.br_widget.mario_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.mario_order_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.mario_order_label.setText('Polynomial order:')
            self.br_widget.mario_order_label.setObjectName("self.br_widget.mario_order_label")
            self.br_widget.mario_hlayout.addWidget(self.br_widget.mario_order_label)
            self.br_widget.mario_order_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.mario_order_spinbox.setObjectName("self.br_widget.mario_order_spinbox")
            self.br_widget.mario_hlayout.addWidget(self.br_widget.mario_order_spinbox)
            self.br_widget.mario_order_spinbox.setValue(10)
            self.br_widget.mario_order_spinbox.setRange(1, 100)
            self.br_widget.mario_order_spinbox.setSingleStep(1)

            self.br_widget.mario_iters_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.mario_iters_label.setText('Maximum # of iterations:')
            self.br_widget.mario_iters_label.setObjectName("self.br_widget.mario_iters_label")
            self.br_widget.mario_hlayout.addWidget(self.br_widget.mario_iters_label)
            self.br_widget.mario_iters_spinbox = QtWidgets.QDoubleSpinBox(self.br_widget)
            self.br_widget.mario_iters_spinbox.setObjectName("self.br_widget.mario_iters_spinbox")
            self.br_widget.mario_hlayout.addWidget(self.br_widget.mario_iters_spinbox)
            self.br_widget.mario_iters_spinbox.setRange(1, 1e10)
            try:
                nfeatures_default = 10 * self.pysat_fun.data[self.baseline_choosedata.currentText()].df[
                    'wvl'].columns.levels[1].size
                self.br_widget.mario_iters_spinbox.setValue(nfeatures_default)
            except:
                self.br_widget.mario_iters_spinbox.setValue(1e5)

            self.br_widget.mario_iters_spinbox.setSingleStep(1e3)

            self.br_widget.mario_tol_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.mario_tol_label.setText('Tolerance:')
            self.br_widget.mario_tol_label.setObjectName("self.br_widget.mario_tol_label")
            self.br_widget.mario_hlayout.addWidget(self.br_widget.mario_tol_label)
            self.br_widget.mario_tol_spinbox = QtWidgets.QDoubleSpinBox(self.br_widget)
            self.br_widget.mario_tol_spinbox.setObjectName("self.br_widget.mario_tol_spinbox")
            self.br_widget.mario_hlayout.addWidget(self.br_widget.mario_tol_spinbox)
            self.br_widget.mario_tol_spinbox.setValue(1e-2)
            self.br_widget.mario_tol_spinbox.setRange(0, 100)
            self.br_widget.mario_tol_spinbox.setSingleStep(1e-3)

            if params is not None:
                self.br_widget.mario_order_spinbox.setValue(params['poly_order'])
                self.br_widget.mario_iters_spinbox.setValue(params['max_iters'])
                self.br_widget.mario_tol_spinbox.setValue(params['tol'])

        if alg == 'Median':
            '''intensities, window_size=501'''
            self.br_widget.median_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.median_window_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.median_window_label.setText('Window size:')
            self.br_widget.median_window_label.setObjectName("self.br_widget.median_window_label")
            self.br_widget.median_hlayout.addWidget(self.br_widget.median_window_label)
            self.br_widget.median_window_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.median_window_spinbox.setObjectName("self.br_widget.median_window_spinbox")
            self.br_widget.median_hlayout.addWidget(self.br_widget.median_window_spinbox)
            self.br_widget.median_window_spinbox.setRange(1, 10000)
            self.br_widget.median_window_spinbox.setValue(501)

            self.br_widget.median_window_spinbox.setSingleStep(1)
            if params is not None:
                self.br_widget.median_window_spinbox.setValue(params['window_size'])
            pass
        if alg == 'Rubberband':
            '''bands, intensities, num_iters=8, num_ranges=64'''
            self.br_widget.rubberband_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.rubberband_iters_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.rubberband_iters_label.setText('Window size:')
            self.br_widget.rubberband_iters_label.setObjectName("self.br_widget.rubberband_iters_label")
            self.br_widget.rubberband_hlayout.addWidget(self.br_widget.rubberband_iters_label)
            self.br_widget.rubberband_iters_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.rubberband_iters_spinbox.setObjectName("self.br_widget.rubberband_iters_spinbox")
            self.br_widget.rubberband_hlayout.addWidget(self.br_widget.rubberband_iters_spinbox)
            self.br_widget.rubberband_iters_spinbox.setRange(1, 10000)
            self.br_widget.rubberband_iters_spinbox.setValue(8)

            self.br_widget.rubberband_iters_spinbox.setSingleStep(1)

            self.br_widget.rubberband_ranges_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.rubberband_ranges_label.setText('# of ranges:')
            self.br_widget.rubberband_ranges_label.setObjectName("self.br_widget.rubberband_ranges_label")
            self.br_widget.rubberband_hlayout.addWidget(self.br_widget.rubberband_ranges_label)
            self.br_widget.rubberband_ranges_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.rubberband_ranges_spinbox.setObjectName("self.br_widget.rubberband_ranges_spinbox")
            self.br_widget.rubberband_hlayout.addWidget(self.br_widget.rubberband_ranges_spinbox)
            self.br_widget.rubberband_ranges_spinbox.setValue(64)
            self.br_widget.rubberband_ranges_spinbox.setRange(1, 1000)
            self.br_widget.rubberband_ranges_spinbox.setSingleStep(1)

            if params is not None:
                self.br_widget.rubberband_iters_spinbox.setValue(params['num_iters'])
                self.br_widget.rubberband_ranges_spinbox.setValue(params['num_ranges'])

            pass
        if alg == 'CCAM':
            '''x,y,lv,lvmin=2,int_flag=2'''
            ''';       Wavelength: One dimensional array of wavelengths
;       Spectrum: One dimensional array of libs intensity (same size as wavelength)
;       Wavelet_Scale1: Integer; Largest wavelet scale to start with
;       (2^Wavelet_scale) LT wavelength size)
;       Wavelet_Scale2: Integer; Lowest wavelet scale to look at (must be GE 2)
;       Interpolation_Flag: Integer; Flag to select interpolation method
;       between convex hull points
;         0: linear interpolation    
;         1: quadratic interpolation    
;         2: spline interpolation'''

            self.br_widget.ccam_hlayout = QtWidgets.QHBoxLayout(self.br_widget)
            self.br_widget.ccam_scale1_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.ccam_scale1_label.setText('Largest wavelet scale:')
            self.br_widget.ccam_scale1_label.setObjectName("self.br_widget.ccam_scale1_label")
            self.br_widget.ccam_hlayout.addWidget(self.br_widget.ccam_scale1_label)
            self.br_widget.ccam_scale1_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.ccam_scale1_spinbox.setObjectName("self.br_widget.ccam_scale1_spinbox")
            self.br_widget.ccam_hlayout.addWidget(self.br_widget.ccam_scale1_spinbox)
            self.br_widget.ccam_scale1_spinbox.setValue(10)
            self.br_widget.ccam_scale1_spinbox.setRange(1, 100)
            self.br_widget.ccam_scale1_spinbox.setSingleStep(1)

            self.br_widget.ccam_scale2_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.ccam_scale2_label.setText('Lowest wavelet scale:')
            self.br_widget.ccam_scale2_label.setObjectName("self.br_widget.ccam_scale2_label")
            self.br_widget.ccam_hlayout.addWidget(self.br_widget.ccam_scale2_label)
            self.br_widget.ccam_scale2_spinbox = QtWidgets.QSpinBox(self.br_widget)
            self.br_widget.ccam_scale2_spinbox.setObjectName("self.br_widget.ccam_scale2_spinbox")
            self.br_widget.ccam_hlayout.addWidget(self.br_widget.ccam_scale2_spinbox)
            self.br_widget.ccam_scale2_spinbox.setValue(6)
            self.br_widget.ccam_scale2_spinbox.setRange(2, 100)
            self.br_widget.ccam_scale2_spinbox.setSingleStep(1)

            self.br_widget.ccam_interp_label = QtWidgets.QLabel(self.br_widget)
            self.br_widget.ccam_interp_label.setText('Interpolation method:')
            self.br_widget.ccam_interp_label.setObjectName("self.br_widget.ccam_interp_label")
            self.br_widget.ccam_hlayout.addWidget(self.br_widget.ccam_interp_label)
            self.br_widget.ccam_interp_combobox = QtWidgets.QComboBox(self.br_widget)
            self.br_widget.ccam_interp_combobox.addItem(("Spline"))
            self.br_widget.ccam_interp_combobox.addItem(("Quadratic"))
            self.br_widget.ccam_interp_combobox.addItem(("Linear"))
            self.br_widget.ccam_interp_combobox.setObjectName("self.br_widget.ccam_interp_combobox")
            self.br_widget.ccam_hlayout.addWidget(self.br_widget.ccam_interp_combobox)

            if params is not None:
                self.br_widget.ccam_scale1_spinbox.setValue(params['scale1'])
                self.br_widget.ccam_scale2_spinbox.setValue(params['scale2'])
                if params['int_flag'] == 0:
                    self.br_widget.ccam_interp_combobox.setCurrentIndex(
                        self.br_widget.ccam_interp_combobox.findText('Linear'))
                elif params['int_flag'] == 1:
                    self.br_widget.ccam_interp_combobox.setCurrentIndex(
                        self.br_widget.ccam_interp_combobox.findText('Quadratic'))
                elif params['int_flag'] == 2:
                    self.br_widget.ccam_interp_combobox.setCurrentIndex(
                        self.br_widget.ccam_interp_combobox.findText('Spline'))

                    self.br_widget.setObjectName("self.br_widget")
        self.baseline_vlayout.addWidget(self.br_widget)
        for name, obj in inspect.getmembers(self.br_widget):
            if isinstance(obj, QtWidgets.QComboBox):
                obj.currentIndexChanged.connect(lambda: self.get_baseline_parameters())
            if isinstance(obj, QtWidgets.QLineEdit):
                obj.textChanged.connect(lambda: self.get_baseline_parameters())
            if isinstance(obj, QtWidgets.QDoubleSpinBox):
                obj.valueChanged.connect(lambda: self.get_baseline_parameters())
            if isinstance(obj, QtWidgets.QSpinBox):
                obj.valueChanged.connect(lambda: self.get_baseline_parameters())
            if isinstance(obj, QtWidgets.QCheckBox):
                obj.toggled.connect(lambda: self.get_baseline_parameters())
        self.get_baseline_parameters()

    def baseline_ui(self):
        self.remove_baseline = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_baseline.setFont(font)
        self.baseline_vlayout = QtWidgets.QVBoxLayout(self.remove_baseline)
        # choose data
        self.baseline_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.remove_baseline_choosedata_label = QtWidgets.QLabel(self.remove_baseline)
        self.remove_baseline_choosedata_label.setText("Choose data:")
        self.remove_baseline_choosedata_label.setObjectName("self.remove_baseline_choosedata_label")
        self.baseline_choosedata_hlayout.addWidget(self.remove_baseline_choosedata_label)
        datachoices = self.pysat_fun.datakeys
        datachoices = [i for i in datachoices if i != 'CV Results']  # prevent CV results from showing up as an option

        self.baseline_choosedata = make_combobox(datachoices)
        self.baseline_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.baseline_choosedata.setObjectName("self.baseline_choosedata")
        self.baseline_choosedata_hlayout.addWidget(self.baseline_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.baseline_choosedata_hlayout.addItem(spacerItem)
        self.baseline_vlayout.addLayout(self.baseline_choosedata_hlayout)

        # choose baseline algorithm
        self.baseline_choosealg_hlayout = QtWidgets.QHBoxLayout()
        self.baseline_choosealg_label = QtWidgets.QLabel(self.remove_baseline)
        self.baseline_choosealg_label.setObjectName("self.baseline_choosealg_label")
        self.baseline_choosealg_hlayout.addWidget(self.baseline_choosealg_label)
        self.baseline_alg_choices = ['Choose an algorithm', 'ALS', 'Dietrich', 'Polyfit', 'AirPLS', 'FABC', 'KK',
                                     'Mario', 'Median', 'Rubberband', 'CCAM']
        self.baseline_choosealg = make_combobox(self.baseline_alg_choices)
        self.baseline_choosealg.setIconSize(QtCore.QSize(50, 20))
        self.baseline_choosealg.setObjectName("self.baseline_choosealg")
        self.baseline_choosealg_hlayout.addWidget(self.baseline_choosealg)
        baseline_choosealg_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum)
        self.baseline_choosealg_hlayout.addItem(baseline_choosealg_spacer)
        self.baseline_vlayout.addLayout(self.baseline_choosealg_hlayout)

        self.remove_baseline.setObjectName("self.remove_baseline")
        self.module_layout.addWidget(self.remove_baseline)
        self.remove_baseline.raise_()
        self.remove_baseline.setTitle(("Baseline Removal"))

        self.baseline_choosedata.currentIndexChanged.connect(lambda: self.get_baseline_parameters())
        self.baseline_choosealg.currentIndexChanged.connect(lambda: self.get_baseline_parameters())
