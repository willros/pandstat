"""
pandstats.

Easy statistical testing in Pandas
"""

__version__ = "0.0.1"
__author__ = "William Rosenbaum"

from pandstat.linear_models import ols_model, one_sample_ttest, one_sample_ttest_grouped

__all__ = ["ols_model", "one_sample_ttest", "one_sample_ttest_grouped"]
