# pandstat
Package for easy integration of statistical tools in Pandas. 


## Usage: 
All functions are meant to be used in `pandas.pipe method`.
* All functions returns a new pd.DataFrame 

### Example of usage:
```python
from pandstat import ols_model, one_sample_ttest

df = (pd.DataFrame()
      .assign(x=[1,2,3,4,4,5,5,5,5,5,5,5])
     )

(df
 .pipe(one_sample_ttest, 'x')
)

```
*Output:*

|    | term      |    mean |   std_error |       t |     p_value |   conf_low |   conf_high |   n_observations |
|---:|:----------|--------:|------------:|--------:|------------:|-----------:|------------:|-----------------:|
|  0 | Intercept | 4.08333 |     0.39807 | 10.2578 | 5.72919e-07 |    3.20719 |     4.95948 |               12 |


## Dependencies

* `statsmodels`
* `pandas`



# TODO

How to write `complete`
make a pivot table and fillna(0) and melt back again! 
NOPE! That wont work...