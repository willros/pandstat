import statsmodels.formula.api as smf
import pandas as pd
from typing import Union
import numpy as np


def ols_model(df_: pd.DataFrame, dependent: str, independent: list) -> pd.DataFrame:
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


def one_sample_ttest(
    df_: pd.DataFrame, variables: str, weights: Union[None, str] = None
) -> pd.DataFrame:
    """
    Runs a one sample ttest (linear regression with only 1 term (only returns the intercept).
    :param df_: pd.DataFrame. The dataframe to run the function on.
    :param variable: str. The name of the column with the variable.
    :param weights: None | str. A column of weigths to multiply the variables with. Example:
    variable = [1,2,3], weights = [1,3,5] --> [1,2,2,2,3,3,3,3,3]

    :returns: pd.DataFrame
    """

    if weights is None:
        new_variables = np.array(df_[variables])
    else:
        new_variables = np.repeat(df_[variables], df_[weights])

    df = pd.DataFrame().assign(new_variables=new_variables)

    model = smf.ols("new_variables ~ 1", data=df).fit()

    model_df = (
        model.summary2()
        .tables[1]
        .reset_index()
        .rename(
            columns={
                "P>|t|": "p_value",
                "index": "term",
                "Coef.": "mean",
                "Std.Err.": "std_error",
                "[0.025": "conf_low",
                "0.975]": "conf_high",
            }
        )
        .assign(n_observations=len(new_variables))
    )

    return model_df


def one_sample_ttest_grouped(
    df_: pd.core.groupby.generic.DataFrameGroupBy,
    variables: str,
    weights: Union[None, str] = None,
) -> pd.DataFrame:

    list_of_df = []

    for name, groups in df_:

        if weights is None:
            new_variables = np.array(groups[variables])
        else:
            new_variables = np.repeat(groups[variables], groups[weights])

        df = pd.DataFrame().assign(new_variables=new_variables)

        model = smf.ols("new_variables ~ 1", data=df).fit()

        model_df = (
            model.summary2()
            .tables[1]
            .reset_index()
            .rename(
                columns={
                    "P>|t|": "p_value",
                    "index": "term",
                    "Coef.": "mean",
                    "Std.Err.": "std_error",
                    "[0.025": "conf_low",
                    "0.975]": "conf_high",
                }
            )
            .assign(group=name, n_observations=len(new_variables))
        )

        list_of_df.append(model_df)

    models = pd.concat(list_of_df)

    return models
