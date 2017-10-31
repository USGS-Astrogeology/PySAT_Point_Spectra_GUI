export PATH="$HOME/miniconda/bin:$PATH"
conda config --set always_yes yes --set changeps1 no
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
git clone --depth=50 --branch=master https://github.com/USGS-Astrogeology/PySAT.git
cd PySAT
python setup.py install
cd ..
cd PySAT_Point_Spectra_GUI
python setup.py install