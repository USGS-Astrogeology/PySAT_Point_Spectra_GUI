import pytest
import numpy as np
import pandas as pd

from point_spectra_gui.util.PandasModel import PandasModel

@pytest.fixture
def repeat_df(n):
    data =  np.repeat(np.arange(1, n + 1), (n)).reshape(n,-1)
    columns = np.arange(1, n+1)
    return pd.DataFrame(data, columns = columns)

@pytest.fixture
def repeat_df_len10():
    return repeat_df(10)

@pytest.fixture
def repeat_pandasmodel(n):
    df = repeat_df(n)
    return PandasModel(df)
