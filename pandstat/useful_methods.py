import pandas as pd
import pandas_flavor as pf
import altair as alt


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


@pf.register_dataframe_method
def altair_plot(df: pd.DataFrame, kind: str) -> alt.vegalite.v4.api.Chart:
    """
    :param kind: str. Kind of chart to plot.
    Choose between:
    bar, point, line, area, circle, rule, square, rect, text, trail, boxplot

    Returns an altair graph object
    """

    if kind == "bar":
        return alt.Chart(df).mark_bar()
    elif kind == "point":
        return alt.Chart(df).mark_point()
    elif kind == "line":
        return alt.Chart(df).mark_line()
    elif kind == "area":
        return alt.Chart(df).mark_area()
    elif kind == "circle":
        return alt.Chart(df).mark_circle()
    elif kind == "rule":
        return alt.Chart(df).mark_rule()
    elif kind == "square":
        return alt.Chart(df).mark_square()
    elif kind == "rect":
        return alt.Chart(df).mark_rect()
    elif kind == "text":
        return alt.Chart(df).mark_text()
    elif kind == "tick":
        return alt.Chart(df).mark_tick()
    elif kind == "trail":
        return alt.Chart(df).mark_trail()
    elif kind == "boxplot":
        return alt.Chart(df).mark_boxplot()
