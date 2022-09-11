import pandas as pd
import pandas_flavor as pf
import numpy as np


@pf.register_dataframe_method
def add_count(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Adds new column called n with count values of the provided column.
    :param col str: The name of the column that should be counted
    :returns: pd.DataFrame

    Used as a regular pandas method.
    """
    return df.assign(n=lambda x: x.groupby(col, as_index=False)[col].transform(np.size))
