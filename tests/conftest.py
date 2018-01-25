import pytest
import numpy as np
import pandas as pd

@pytest.fixture
def repeat_df(n):
    data =  np.repeat(np.arange(1, n + 1), (n)).reshape(n, -1)
    columns = np.arange(1, n + 1)
    return pd.DataFrame(data, columns = columns)
