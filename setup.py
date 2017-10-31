# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import re
import sys
from io import StringIO

from point_spectra_gui import __version__

if sys.version_info < (3, 5):
    sys.exit("ERROR: You need Python 3.5 or higher to use point_spectra_gui.")

from distutils import log
from distutils.dep_util import newer
from distutils.spawn import find_executable
from setuptools import setup, Command, find_packages

PACKAGE_NAME = "point_spectra_gui"

exclude_modules = [
    'ssl', 'bz2',
    'distutils', 'unittest',
    'bdb', 'calendar', 'difflib', 'doctest', 'dummy_thread', 'gzip',
    'optparse', 'pdb', 'plistlib', 'pyexpat', 'quopri', 'repr',
    'stringio', 'tarfile', 'uu'
]

tx_executable = find_executable('tx')


def py_from_ui(uifile):
    return "%s.py" % os.path.splitext(os.path.basename(uifile))[0]


def py_from_ui_with_defaultdir(uifile):
    return os.path.join("point_spectra_gui", "ui", py_from_ui(uifile))


def ui_files():
    for uifile in glob.glob("ui/*.ui"):
        yield (uifile, py_from_ui_with_defaultdir(uifile))


class point_spectra_gui_build_ui(Command):
    description = "build Qt UI files and resources"
    user_options = [
        ("files=", None, "comma-separated list of files to rebuild"),
    ]

    def initialize_options(self):
        self.files = []

    def finalize_options(self):
        if self.files:
            files = []
            for f in self.files.split(","):
                head, tail = os.path.split(f)
                m = re.match(r'(?:ui_)?([^.]+)', tail)
                if m:
                    name = m.group(1)
                else:
                    log.warn('ignoring %r (cannot extract base name)' % f)
                    continue
                uiname = name + '.ui'
                uifile = os.path.join(head, uiname)
                if os.path.isfile(uifile):
                    pyfile = os.path.join(os.path.dirname(uifile),
                                          py_from_ui(uifile))
                    files.append((uifile, pyfile))
                else:
                    uifile = os.path.join('ui', uiname)
                    if os.path.isfile(uifile):
                        files.append((uifile,
                                      py_from_ui_with_defaultdir(uifile)))
                    else:
                        log.warn('ignoring %r' % f)
            self.files = files

    def run(self):
        from PyQt5 import uic
        _translate_re = (
            re.compile(
                r'QtGui\.QApplication.translate\(.*?, (.*?), None, '
                r'QtGui\.QApplication\.UnicodeUTF8\)'),
            re.compile(
                r'\b_translate\(.*?, (.*?)(?:, None)?\)')
        )

        def compile_ui(uifile, pyfile):
            log.info("compiling %s -> %s", uifile, pyfile)
            tmp = StringIO()
            uic.compileUi(uifile, tmp, True)
            source = tmp.getvalue()
            rc = re.compile(r'\n\n#.*?(?=\n\n)', re.MULTILINE | re.DOTALL)
            comment = ("\n\n# Automatically generated - don't edit.\n"
                       "# Use `python setup.py build_ui` to update it.")
            for r in list(_translate_re):
                source = r.sub(r'(\1)', source)
                source = rc.sub(comment, source)
            f = open(pyfile, "w")
            f.write(source)
            f.close()

        if self.files:
            for uifile, pyfile in self.files:
                compile_ui(uifile, pyfile)
        else:
            for uifile, pyfile in ui_files():
                if newer(uifile, pyfile):
                    compile_ui(uifile, pyfile)


class point_spectra_gui_clean_ui(Command):
    description = "clean up compiled Qt UI files and resources"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for uifile, pyfile in ui_files():
            try:
                os.unlink(pyfile)
                log.info("removing %s", pyfile)
            except OSError:
                log.warn("'%s' does not exist -- can't clean it", pyfile)
        pyfile = os.path.join("point_spectra_gui", "resources.py")
        try:
            os.unlink(pyfile)
            log.info("removing %s", pyfile)
        except OSError:
            log.warn("'%s' does not exist -- can't clean it", pyfile)


setup(
    name=PACKAGE_NAME,
    version=__version__,
    description="A PDART-funded effort to design a spectral analysis tool for LIBS (and other) spectra",
    url="https://github.com/USGS-Astrogeology/PySAT",
    author="Ryan B. Anderson, Nicholas Finch",
    author_email='rbanderson@usgs.gov, ngf4@nau.edu',
    license="Public Domain",
    keywords='PYSAT LIBS PDART Point Spectra',
    package_dir={'point_spectra_gui': 'point_spectra_gui'},
    packages=find_packages(),
    entry_points={
        'gui_scripts': [
            'point_spectra_gui=point_spectra_gui.core.MainWindow:main'
        ],
    },
    cmdclass={
        'build_ui': point_spectra_gui_build_ui,
        'clean_ui': point_spectra_gui_clean_ui,
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering',
    ]
)
