"""
pandstats.

Easy statistical and useful dataframe methods for pandas!
"""

__version__ = "0.1.7"
__author__ = "William Rosenbaum"

from pandstat.linear_models import ols_model, one_sample_ttest, one_sample_ttest_grouped

from pandstat.dataframe_methods import add_count, counting, altair_plot, lump, top_n

__all__ = [
    "ols_model",
    "one_sample_ttest",
    "one_sample_ttest_grouped",
    "add_count",
    "counting",
    "altair_plot",
    "lump",
    "top_n",
]
