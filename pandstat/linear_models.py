import statsmodels.formula.api as smf
import pandas as pd


def ols_model(df_: pd.DataFrame, dependent: str,
              independent: list) -> pd.DataFrame:
    """
    Runs OLS by formula on columns in dataframe
    :param df_: pd.DataFrame. The dataframe to run the function on.
    :param dependent: str. The dependent variable
    :param independent: list. A list of variables to test the dependent variable against. Can be of length 1.
    :returns: A new pd.DataFrame
    """

    independent = (
        independent[0]
        if len(independent) == 1
        else " + ".join([x for x in independent])
    )
    model = smf.ols(f"{dependent} ~ {independent}", data=df_).fit()
    df = (
        model.summary2()
        .tables[1]
        .reset_index()
        .rename(
            columns={
                "P>|t|": "p_value",
                "index": "term",
                "Coef.": "coef",
                "Std.Err.": "std_error",
                "[0.025": "conf_low",
                "0.975]": "conf_high",
            }
        )
    )

    return df
