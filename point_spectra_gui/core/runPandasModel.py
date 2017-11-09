from PyQt5.QtCore import QThread

from point_spectra_gui.core.MainWindow import Ui_MainWindow


class runPandasModel(Ui_MainWindow, QThread):
    def run(self):
        self.on_refreshTable()
