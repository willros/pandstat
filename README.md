# pandstat
Package for easy integration of statistical tools in Pandas. 


## Usage: 
All functions are meant to be used in `pandas.pipe method`.
* All functions returns a new pd.DataFrame 

Example of usage:
```python
import pandstat

(dataframe
 .pipe(pandstat.ols_model, ['col1', 'col2'])
)
```




