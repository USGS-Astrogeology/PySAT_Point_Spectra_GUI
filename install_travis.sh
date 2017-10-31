export PATH="$HOME/miniconda/bin:$PATH"                                             # Set up the miniconda path
conda config --set always_yes yes --set changeps1 no                                # Always say yes to questions
while read requirement; do                                                          # read through all the requirements
  conda install --yes $requirement || pip install $requirement;                     # conda install or pip install
  done < requirements.txt                                                           # get the information from requirements.txt
git clone --depth=50 --branch=master https://github.com/USGS-Astrogeology/PySAT.git # clone the PySAT repo
cd PySAT                                                                            # cd into it
python setup.py install                                                             # setup install
cd ..                                                                               # get out of the PySAT repo
cd PySAT_Point_Spectra_GUI                                                          # go into PySAT_Point_Spectra_GUI
python setup.py install                                                             # setup install