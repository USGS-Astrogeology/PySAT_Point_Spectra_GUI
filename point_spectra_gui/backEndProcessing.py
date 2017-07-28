import traceback

import numpy as np
# from plio import io_ccam_pds
import pandas as pd
import subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from pysat.fileio import io_ccam_pds
from pysat.plotting.plots import make_plot, pca_ica_plot
from pysat.regression import cv
from pysat.regression import regression
from pysat.regression import sm
from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui_modules.Error_ import error_print
from point_spectra_gui.ui_modules.del_layout_ import *


class Module:
    nodeCount = 0

    def __init__(self, ui_list, fun_list, arg_list, kw_list, ui_restore):
        self.ui_list = ui_list
        self.fun_list = fun_list
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_restore = ui_restore
        self.next = None
        self.UI_ID = Module.nodeCount
        Module.nodeCount += 1

    def setData(self, ui_list, fun_list, arg_list, kw_list, ui_restore):
        self.ui_list = ui_list
        self.fun_list = fun_list
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_restore = ui_restore

    def getID(self):
        return self.UI_ID

    def getData(self):
        list = []
        list.append(self.getID())
        list.append(self.ui_list)
        list.append(self.fun_list)
        list.append(self.arg_list)
        list.append(self.kw_list)
        list.append(self.ui_restore)
        return list

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class listOfModules:
    def __init__(self):
        self.head = None
        self.curr_count = 0

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def push(self, ui_list, fun_list, arg_list, kw_list, ui_restore, UI_ID=None):
        if not self.amend(ui_list, fun_list, arg_list, kw_list, ui_restore,
                          UI_ID):  # if the UI_ID that we are playing with exists, amend it, otherwise make something new
            if len(self) == 0:
                # Create a new head
                temp = Module(ui_list, fun_list, arg_list, kw_list, ui_restore)  # self.head = None; temp = 0x085817F0
                temp.setNext(self.head)  # temp = 0x085817F0; temp.next = None
                self.head = temp  # self.head = 0x085817F0; self.head.next = None; temp = 0x085817F0; temp.next = None
                return temp.getID()
            else:
                # Append new data into .next
                temp = Module(ui_list, fun_list, arg_list, kw_list,
                              ui_restore)  # self.head = 0x085817F0; temp = 0x00568330
                current = self.head  # current = 0x085817F0; current.next = None; self.head = 0x085817F0; temp = 0x00568330
                while current.getNext() != None:  #
                    current = current.getNext()  #
                current.setNext(temp)  # current = 0x085817F0; current.next = 0x00568330;
                return temp.getID()
        return UI_ID

    def amend(self, ui_list, fun_list, arg_list, kw_list, ui_restore, UI_ID=None):
        current = self.head
        found = False
        while current is not None and not found and UI_ID is not None:
            if current.getID() == UI_ID:
                found = True
                current.setData(ui_list, fun_list, arg_list, kw_list, ui_restore)
            else:
                current = current.getNext()
        return found

    def pop(self):
        try:
            current = self.head
            self.head = self.head.getNext()
            return current.getData()
        except:
            pass

    def del_module(self):
        current = self.head
        if len(self) == 1:
            self.head = None
            return 1
        while current.getNext().getNext() is not None:
            current = current.getNext()
        current.setNext(None)
        return 1

    def pull(self):
        i = 0
        current = self.head
        while i < self.curr_count and current.getNext() is not None:
            current = current.getNext()
            i += 1
        self.curr_count += 1
        return current.getData()

    def isEmpty(self):
        return self.head == None

    def remove(self, UI_ID):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getID() == UI_ID:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def display(self):
        current = self.head
        while current is not None:
            for items in current.getData():
                print(items)
            current = current.getNext()


class backEndProc(QThread):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.data = {}  # initialize with an empty dict to hold data frames
        self.datakeys = []
        self.models = {}
        self.modelkeys = []
        self.model_xvars = {}
        self.model_yvars = {}
        self.dim_reds = {}
        self.dim_red_keys = []
        self.figs = {}
        self._list = listOfModules()
        self.greyed_modules = []
        self.outpath = './'

    """
    Getter and setter functions below
    """

    def set_list(self, ui, fun, arg, kw, restore, ui_id=None):
        """
        pushing new information as well as returning the UI_ID
        we'll need the UI_ID in order to maintain order and bookkeeping
        :param ui:
        :param fun:
        :param arg:
        :param kw:
        :param ui_id:
        :return:
        """
        return self._list.push(ui, fun, arg, kw, restore, ui_id)

    def get_list(self):
        return self._list

    def display_list(self):
        return self._list.display

    def set_greyed_modules(self, modules):
        self.greyed_modules.append(modules)

    """
    Work functions below
    """

    def set_file_outpath(self, outpath):
        try:
            self.outpath = outpath
            print("Output path folder has been set to " + outpath)
        except Exception as e:
            print(e)

    def do_get_data(self, filename, keyname):
        try:
            print('Loading data file: ' + str(filename))
            self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1]))
            self.datakeys.append(keyname)
            pass
        except Exception as e:
            error_print('Problem reading data: {}'.format(e))

    def do_write_data(self, filename, datakey, cols):

        try:
            datatemp = self.data[datakey].df[cols]
        except:
            datatemp = self.data[datakey][cols]

        try:
            datatemp.to_csv(self.outpath + '/' + filename)
        except:
            datatemp.to_csv(filename)

    def do_read_ccam(self, searchdir, searchstring, to_csv=None, lookupfile=None, ave=True):
        progressbar = QtWidgets.QProgressDialog()
        io_ccam_pds.ccam_batch(searchdir, searchstring=searchstring, to_csv=self.outpath + '/' + to_csv,
                               lookupfile=lookupfile, ave=ave, progressbar=progressbar)
        self.do_get_data(self.outpath + '/' + to_csv, 'ChemCam')

    def removerows(self, datakey, colname, value):
        try:
            print(self.data[datakey].df.shape)
            vars_level0 = self.data[datakey].df.columns.get_level_values(0)
            vars_level1 = self.data[datakey].df.columns.get_level_values(1)
            vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
            vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
            colname = (vars_level0[vars_level1.index(colname)], colname)

            if value == 'Null':
                self.data[datakey] = spectral_data(self.data[datakey].df.ix[-self.data[datakey].df[colname].isnull()])
            else:
                # find where the values in the specified column match the value to be removed
                coldata = np.array([str(i) for i in self.data[datakey].df[colname]])
                match = coldata == value
                # keep everything except where match is true
                self.data[datakey] = spectral_data(self.data[datakey].df.ix[~match])
            print(self.data[datakey].df.shape)

        except Exception as e:
            print(e)

    def do_split_data(self, datakey, colname):
        try:
            vars_level0 = self.data[datakey].df.columns.get_level_values(0)
            vars_level1 = self.data[datakey].df.columns.get_level_values(1)
            vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
            vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
            colname = (vars_level0[vars_level1.index(colname)], colname)

            coldata = np.array([str(i) for i in self.data[datakey].df[colname]])
            unique_values = np.unique(coldata)
            for i in unique_values:
                new_datakey = datakey + ' - ' + str(i)
                self.datakeys.append(new_datakey)
                self.data[new_datakey] = spectral_data(self.data[datakey].df.ix[coldata == i])
        except Exception as e:
            print(e)

    def do_mask(self, datakey, maskfile, maskvar='wvl'):
        try:
            self.data[datakey].mask(maskfile,maskvar=maskvar)
            print("Mask applied")
        except Exception as e:
            print(e)

    def do_peak_area(self, datakey, peaks_mins_file):
        try:
            peaks,mins = self.data[datakey].peak_area(peaks_mins_file=peaks_mins_file)
            print("Peak Areas Calculated")
            
            np.savetxt(self.outpath + '/peaks.csv',peaks,delimiter=',')
            np.savetxt(self.outpath + '/mins.csv', mins, delimiter=',')

        except Exception as e:
            print(e)

    def do_multiply_vector(self, datakey, vectorfile):
        try:
            self.data[datakey].multiply_vector(vectorfile)
        except Exception as e:
            print(e)

    def do_interp(self, datakey_to_interp, datakey_ref):
        print(self.data[datakey_ref].df.columns.levels[0])
        try:
            self.data[datakey_to_interp].interp(self.data[datakey_ref].df['wvl'].columns)
        except Exception as e:
            print(e)

    def do_remove_baseline(self, datakey, method, params):
        datakey_new = datakey + '-Baseline Removed-' + method + str(params)
        datakey_baseline = datakey + '-Baseline-' + method + str(params)
        self.datakeys.append(datakey_new)
        self.datakeys.append(datakey_baseline)
        self.data[datakey_new] = spectral_data(self.data[datakey].df.copy(deep=True))
        self.data[datakey_new].remove_baseline(method, segment=True, params=params)
        self.data[datakey_baseline] = spectral_data(self.data[datakey_new].df_baseline)

    def do_dim_red(self, datakey, method, params, method_kws={}, col='wvl', load_fit=None, dim_red_key=None):
        try:
            if method == 'PCA' or method == 'ICA':
                self.dim_reds[dim_red_key] = self.data[datakey].dim_red(col, method, params, method_kws,
                                                                        load_fit=load_fit)
                self.dim_red_keys.append(dim_red_key)
            elif method == 'ICA-JADE':
                pass
                self.dim_reds[dim_red_key] = self.data[datakey].ica_jade(col)
        except Exception as e:
            print(e)

    def do_pca(self, datakey, nc, col, load_fit=None):
        print(self.data[datakey].df.columns.levels[0])
        try:
            self.data[datakey].pca(col, nc=nc, load_fit=load_fit)
        except Exception as e:
            print(e)

    def do_ica(self, datakey, nc, col, load_fit=None):
        try:
            self.data[datakey].ica(col, nc=nc, load_fit=load_fit)
        except Exception as e:
            print(e)

    def do_ica_jade(self, datakey, nc, col, load_fit=None, corrcols=None):
        try:
            self.data[datakey].ica_jade(col, nc=nc, load_fit=load_fit, corrcols=corrcols)
        except Exception as e:
            print(e)

    def do_norm(self, datakey, ranges, col_var='wvl'):
        print("{}".format(ranges))
        try:
            print(self.data[datakey].df.columns.levels[0])
            self.data[datakey].norm(ranges,col_var=col_var)
            print(self.data[datakey].df.columns.levels[0])
            print("Normalization has been applied to the ranges: " + str(ranges))
        except Exception as e:
            print(e)

    def do_strat_folds(self, datakey, nfolds, testfold, colname):
        self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        self.data[datakey + '-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey + '-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys = self.data.keys()

        print(self.data.keys())
        print(self.data[datakey + '-Test'].df.index.shape)
        print(self.data[datakey + '-Train'].df.index.shape)

    # TODO: This module needs to be looked at. It's parameters are not correct
    def do_regression_train(self, datakey, xvars, yvars, yrange, method, params, ransacparams, modelkey=None,
                            update=False, append=False):
        try:
            if modelkey is None:
                modelkey = method + '-' + str(yvars) + ' (' + str(yrange[0]) + '-' + str(yrange([1]) + ') ')

            self.models[modelkey] = regression.regression([method], [yrange], [params], i=0,
                                                          ransacparams=[ransacparams])
            if not append:
                self.modelkeys.append(modelkey)
            else:
                self.modelkeys[-1] = modelkey
            if not update:
                x = self.data[datakey].df[xvars]
                y = self.data[datakey].df[yvars]
                x = np.array(x)
                y = np.array(y)
                ymask = np.squeeze((y > yrange[0]) & (y < yrange[1]))
                y = y[ymask]
                x = x[ymask, :]
                self.models[modelkey].fit(x, y)
                self.model_xvars[modelkey] = xvars
                self.model_yvars[modelkey] = yvars
                try:
                    coef = np.squeeze(self.models[modelkey].model.coef_)
                    coef = pd.DataFrame(coef)
                    coef.index = pd.MultiIndex.from_tuples(self.data[datakey].df[xvars].columns.values)
                    coef = coef.T
                    coef[('meta', 'Model')] = modelkey

                    try:
                        self.data['Model Coefficients'] = spectral_data(
                            pd.concat([self.data['Model Coefficients'].df, coef]))
                    except:
                        self.data['Model Coefficients'] = spectral_data(coef)
                        self.datakeys.append('Model Coefficients')
                except:
                    pass

        except Exception as e:
            print(e)

    def do_cv_train(self, datakey, xvars, yvars, yrange, method, params):

        try:
            cv_obj = cv.cv(params)
            self.data[datakey].df, self.cv_results = cv_obj.do_cv(self.data[datakey].df, xcols=xvars, ycol=yvars,
                                                                  yrange=yrange, method=method)
            self.data['CV Results'] = self.cv_results
        except Exception as e:
            print(e)

    def do_regression_predict(self, datakey, modelkey, predictname):
        try:
            prediction = self.models[modelkey].predict(self.data[datakey].df[self.model_xvars[modelkey]])
            self.data[datakey].df[predictname] = prediction
            pass
        except Exception as e:
            print(e)

    def do_submodel_predict(self, datakey, submodel_names, modelranges, trueval_data):
        # Check if reference data name has been provided
        # if so, get reference data values
        if trueval_data is not None:
            truevals = self.data[trueval_data].df[self.model_yvars[submodel_names[0]]]
            x_ref = []
        else:
            truevals = None

        # step through the submodel names and get the actual models and the x data
        x = []
        submodels = []
        for i in submodel_names:
            x.append(self.data[datakey].df[self.model_xvars[i]])
            submodels.append(self.models[i])
            if trueval_data is not None:
                x_ref.append(self.data[trueval_data].df[self.model_xvars[i]])

        # create the submodel object
        sm_obj = sm.sm(modelranges, submodels)

        # optimize blending if reference data is provided (otherwise, modelranges will be used as blending ranges)
        if truevals is not None:
            ref_predictions = sm_obj.predict(x_ref)
            ref_predictions_blended = sm_obj.do_blend(ref_predictions, truevals=truevals)

        # get predictions for each submodel separately
        predictions = sm_obj.predict(x)

        # blend the predictions together
        predictions_blended = sm_obj.do_blend(predictions)

        # save the individual and blended predictions
        for i, j in enumerate(predictions):
            self.data[datakey].df[('predict', submodel_names[i] + '-Predict')] = j
        self.data[datakey].df[('predict', 'Blended-Predict')] = predictions_blended
        pass

    def do_plot(self, datakey,
                xvar, yvar,
                figfile=None, xrange=None,
                yrange=None, xtitle='Reference (wt.%)',
                ytitle='Prediction (wt.%)', title=None,
                lbl=None, one_to_one=False,
                dpi=1000, color=None,
                annot_mask=None,
                cmap=None, colortitle='', figname=None, masklabel='',
                marker='o', linestyle='None', alpha=0.5
                ):

        try:
            if self.data[datakey].df.columns.nlevels == 2:
                vars_level0 = self.data[datakey].df.columns.get_level_values(0)
                vars_level1 = self.data[datakey].df.columns.get_level_values(1)
                vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
                vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
                xvar = (vars_level0[vars_level1.index(xvar)], xvar)
                yvar = (vars_level0[vars_level1.index(yvar)], yvar)
        except:
            pass

        try:
            x = self.data[datakey].df[xvar]
            y = self.data[datakey].df[yvar]
        except:
            x = self.data[datakey][xvar]
            y = self.data[datakey][yvar]
        try:
            loadfig = self.figs[figname]
        except:
            loadfig = None
            # outpath=self.outpath
        try:
            outpath = self.outpath
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)
        except Exception as e:
            print(e)
            # dealing with the a possibly missing outpath
            outpath = './'
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)

    def do_plot_spect(self, datakey,
                      row,
                      xcol='wvl',
                      figfile=None, xrange=None,
                      yrange=None, xtitle='Wavelength (nm)',
                      ytitle=None, title=None,
                      lbl=None, one_to_one=False,
                      dpi=1000, color=None,
                      annot_mask=None,
                      cmap=None, colortitle='', figname=None, masklabel='',
                      marker=None, linestyle='-', col=None, alpha=0.5, linewidth=1.0):

        self.data[datakey].enumerate_duplicates(col)
        data = self.data[datakey].df

        y = np.squeeze(np.array(data.loc[data[('meta', col)].isin([row])][xcol].T))
        x = np.array(data[xcol].columns.values)
        if linestyle == 'None':
            marker='o'
        try:
            loadfig = self.figs[figname]
        except:
            loadfig = None

        try:
            outpath = self.outpath
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle,
                                           linewidth=linewidth)

        except Exception as e:
            print(e)
            # dealing with the a possibly missing outpath
            outpath = './'
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)


    def do_plot_dim_red(self, datakey,
                        x_component,
                        y_component,
                        figfile,
                        colorvar=None,
                        cmap='viridis',
                        method='PCA'
                        ):
        pca_ica_plot(self.data[datakey], x_component, y_component, colorvar=colorvar, cmap=cmap, method=method,
                     figpath=self.outpath, figfile=figfile)

    def __del__(self):
        self.wait()

    def del_layout(self):
        # Deleting a whole lotta lists... >_<
        try:
            del_qwidget_(self.greyed_modules[-1])
            del self.greyed_modules[-1]
            self._list.del_module()
        except:
            error_print("Cannot delete")

    def run(self):
        # TODO this function will take all the enumerated functions and parameters and run them
        try:
            for i in range(len(self.greyed_modules)):
                r_list = self._list.pull()
                print(r_list)
                getattr(self, r_list[2])(*r_list[3], **r_list[4])  # TODO add comment about who is who
                self.greyed_modules[0].setDisabled(True)
                del self.greyed_modules[0]
            self.taskFinished.emit()
        except Exception as e:
            print(e)
            self.taskFinished.emit()
