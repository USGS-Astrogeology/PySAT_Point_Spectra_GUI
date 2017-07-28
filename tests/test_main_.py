import sys
import unittest

from PyQt5.QtWidgets import *

from point_spectra_gui.__main__ import Main


class TestSet(unittest.TestCase):
    def test_main(self):
        app = QApplication(sys.argv)
        main_window = Main()
        main_window.show()
        assert isinstance(main_window.centralWidget(), QWidget)
