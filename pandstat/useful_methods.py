import pandas as pd
import pandas_flavor as pf


@pf.register_dataframe_method
def add_count(df_: pd.DataFrame, col: str, name: str = None) -> pd.DataFrame:
    """
    Adds new column called n with count values of the provided column.
    :param col str: The name of the column that should be counted
    :param name str: Name of the count column
    :returns: pd.DataFrame

    Used as a regular pandas method.
    """
    count_dict = df_.value_counts(col).to_dict()

    df = df_.assign(n=lambda x: x[col].map(count_dict))

    if name:
        return df.rename(columns={"n": name})
    return df


@pf.register_dataframe_method
def counting(df_: pd.DataFrame, *cols: str, name: str = None) -> pd.DataFrame:
    """
    Counts the records in a column and returns a dataframe
    :param cols str: The name of the column that should be counted. Can be many columns.
    :param name str: Name of the count column
    :returns: pd.DataFrame

    Used as a regular pandas method.
    """
    df = df_.value_counts([*cols]).to_frame("n").reset_index()

    if name:
        return df.rename(columns={"n": name})
    return df
