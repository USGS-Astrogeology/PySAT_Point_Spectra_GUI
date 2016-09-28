from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd


class pysat_func():
    # Thus make sure that you have if's for all instances in functions where unknown_data doesn't exist.


    def set_file_outpath(self, outpath):
        try:
            self.outpath = outpath
        except Exception as e:
            print(e)

    def set_file_knowndatacsv(self, db):
        try:
            self.db = db
        except Exception as e:
            print(e)

    def set_file_unknowndatacsv(self, unknowndatacsv):
        try:
            self.unknowndatacsv = unknowndatacsv
        except Exception as e:
            print(e)

    def set_file_maskfile(self, maskfile):
        try:
            self.maskfile = maskfile
        except Exception as e:
            print(e)

    def get_spectra(self):
        try:
            self.data = pd.read_csv(self.db, header=[0, 1])
            self.data = spectral_data(self.data)
            self.unknown_data = pd.read_csv(self.unknowndatacsv, header=[0, 1])
            self.unknown_data = spectral_data(self.unknown_data)
        except Exception as e:
            print(e)

    def set_interp(self):
        # TODO interp should be it's ownn function
        try:
            self.unknown_data.interp(self.data.df['wvl'].columns)
        except Exception as e:
            print(e)

    def set_mask(self):
        try:
            self.data.mask(self.maskfile)
            self.unknown_data.mask(self.maskfile)
        except Exception as e:
            print(e)

    def get_ranges(self, ranges):
        print("{}".format(ranges))
        try:
            self.data.norm(ranges)
            self.unknown_data.norm(ranges)
        except Exception as e:
            print(e)


    def set_element_name(self, el):
        try:
            self.el = el
        except Exception as e:
            print(e)

    def set_nfolds(self, nfolds_test):
        try:
            self.nfolds_test = nfolds_test
        except Exception as e:
            print(e)

    def set_testfold_test(self, testfold_test):
        try:
            self.testfold_test = testfold_test
        except Exception as e:
            print(e)

    def get_nfolds(self):
        try:
            return self.nfolds_test
        except Exception as e:
            print(e)

    def get_testfold_test(self):
        try:
            return self.testfold_test
        except Exception as e:
            print(e)

    def set_compranges(self, compranges):
        try:
            self.compranges = compranges
        except Exception as e:
            print(e)

    def set_stratified(self):
        try:
            self.data.stratified_folds(nfolds=self.nfolds_test, sortby=('meta', self.el))
            self.data1_train = self.data.rows_match(('meta', 'Folds'), [self.testfold_test], invert=True)
            self.data1_test = self.data.rows_match(('meta', 'Folds'), [self.testfold_test])
        except Exception as e:
            print(e)

    def get_number_components(self, ncs):
        # ncs = [7, 7, 5, 9]
        try:
            self.ncs = ncs
        except Exception as e:
            print(e)

    def get_train_data(self):
        try:
            self.traindata = [self.data1_train.df, self.data1_train.df, self.data1_train.df, self.data1_train.df]
        except Exception as e:
            print(e)

    def get_test_data(self):
        try:
            self.testdata = [self.data1_test.df, self.data1_test.df, self.data1_test.df, self.data1_test.df]
        except Exception as e:
            print(e)

    def set_sm(self):
        try:
            self.sm = pls_sm()
        except Exception as e:
            print(e)

    def get_sm_fit(self):
        try:
            self.sm.fit(self.traindata, self.compranges, self.ncs, self.el, figpath=self.outpath)
            self.predictions_train = self.sm.predict(self.traindata)
            self.predictions_test = self.sm.predict(self.testdata)
            self.blended_train = self.sm.do_blend(self.predictions_train, self.traindata[0]['meta'][self.el])
            self.blended_test = self.sm.do_blend(self.predictions_test)
        except Exception as e:
            print(e)

    def get_plots(self):
        try:
            self.sm.final(self.testdata[0]['meta'][self.el],
                      self.blended_test,
                      el=self.el,
                      xcol='Ref Comp Wt. %',
                      ycol='Predicted Comp Wt. %',
                      figpath=self.outpath)
        except Exception as e:
            print(e)

