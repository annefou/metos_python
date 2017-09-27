---
title: "Machine Learning with Scikit-learn"
teaching: 0
exercises: 0
questions:
- "Learn about Scikits (SciPy Toolkits)"
- "Learn to use scikit-learn (python modules for machine learning and data mining) in meteorology and oceanography"
objectives:
- "First objective."
keypoints:
- "First key point."
---

SciKits (short for SciPy Toolkits), are add-on packages for SciPy, hosted and developed separately and independently from the main SciPy distribution.

We will give here a example on how to use scikit-learn with timeseries. We will be using a netCDF input file you can download 
[here](https://github.com/annefou/metos_python/blob/gh-pages/data/t2m_EI_sp_timeseries.nc).

Make sure you download or move this file to the directory where we have our notebooks.

To read this file, we will be using [xarray](http://xarray.pydata.org/en/stable/) which provides a [pandas](http://pandas.pydata.org/)-like and 
pandas-compatible toolkit for analytics on multi-dimensional arrays, rather than the tabular data for which pandas excels. In many cases, it simplifies how we read netCDF files and how
we manipulates them. 

~~~
import xarray as xr
d=xr.open_dataset('t2m_EI_sp_timeseries.nc')
df = d['t2m'].to_series()
df.head()
~~~
{: .python}

~~~
time                 lat   lon 
1979-01-01 00:00:00  60.0  10.0    248.872260
1979-01-01 06:00:00  60.0  10.0    248.719618
1979-01-01 12:00:00  60.0  10.0    252.385079
1979-01-01 18:00:00  60.0  10.0    253.424692
1979-01-02 00:00:00  60.0  10.0    257.389248
Name: t2m, dtype: float64
~~~
{: .output}



`xarray.Dataset` is an in-memory representation of a netCDF file similar to what we used with `netCDF-4-python` package.

