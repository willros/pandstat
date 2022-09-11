"""
pandstats.

Easy statistical testing in Pandas
"""

__version__ = "0.1.5"
__author__ = "William Rosenbaum"

from pandstat.linear_models import ols_model, one_sample_ttest, one_sample_ttest_grouped
from pandstat.useful_methods import add_count, counting

__all__ = [
    "ols_model",
    "one_sample_ttest",
    "one_sample_ttest_grouped",
    "add_count",
    "counting",
]
