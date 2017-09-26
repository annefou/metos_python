---
title: "Handling very large files in Python"
teaching: 0
exercises: 0
questions:
- "How to manipulate large netCDF or HDF files?"
- "How to optimize my workflow?"
- "What are xarray and dask?"
objectives:
- "Learn how to access a portion of a netCDF-4 file"
- "Learn how to access a portion of an HDF5 file"
- "Learn how to perform out of core computation with dask"
keypoints:
- "Strategies to manipulate large files in python"
- "Dask: a flexible parallel computing library for analytic computing"
---

What we have seen so far is mostly valid when dealing with "small" datafiles. What we mean by small is whatever size your laptop can handle today within a 
"reasonable" time... In this lesson, our goal is to show you how introducing parallelism can speed up your data processing work.

By no means this lesson intends to make a review on existing possibilities with their strengths and drawbacks. 

# Reading "large" netCDF-4 or HDF-5 files

We first need to generate a "larger" netCDF dataset; for this we will be using an existing file that we first copy:

~~~
cp EI_VO_850hPa_Summer2001.nc large.nc
~~~
{: .bash}

And we add additional data to its unlimited dimension (time):

~~~
from netCDF4 import Dataset 
import numpy as np
# Read and Append to an existing netCDF file
d = Dataset('../../../../Downloads/large.nc', 'a')

data=d.variables['VO']
t=d.variables['time']

last_time=t[t.size-1]
VO=data[0,:,:,:]

appendvar = d.variables['VO']
for nt in range(t.size,t.size+200000):
# there are 100 times in the file originally
    VO += 0.1 * np.random.randn()
    last_time += 6.0
    appendvar[nt] = VO
    t[nt] = last_time
d.close()
~~~
{: .python}

As you can see writing this dataset is quite slow but we will see later how we can improve the performance when writing netCDF file. We first look how 
we can improve the reading.

## Reading a slice of a dataset

When your netCDF file becomes large, it is unlikely you can fit the entire file into your laptop memory. You can slice your dataset and load it so it can fit into 
memory. You can slice netCDF variables using a syntax similar to numpy arrays:

~~~
from netCDF4 import Dataset    
d = Dataset('large.nc', 'r')
# Do not load dataset yet
data=d.variables['VO']
# pick-up a time and read VO
slice_t=data[100,:,:,:]
~~~
{: .python}

> ## Timeseries
> 
> 1. Use the preceding example but extract all data for one single geographical location (pick-up any location). 
>
> > ## Solution
> > 1. 
> > ~~~
> > from netCDF4 import Dataset    
> > d = Dataset('large.nc', 'r')
> > # Do not load dataset yet
> > data=d.variables['VO']
> > # pick-up a time and read VO
> > slice_t=data[:,0,30,30]
> > ~~~
> > {: .python}
> > 
> {: .solution}
{: .challenge}


> ## Data Tip: 
> Use netCDF-4 / HDF-5 Data compression when writing your dataset to save disk space.
> NetCDF4 and HDF5 provide easy methods to compress data. When you create variables, 
> you can turn on data compression by setting the keyword argument zlib=True:
> 
> ~~~
> temp = d.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'), zlib=True)
> ~~~
> {: .python}
> 
> - The `complevel` keyword argument toggles the compression ratio and speed. Options range from 1 to 9 
> (1 being the fastest with least compression and 9 being the slowest with most compression. Default is 4). 
> - The precision of your data can be specified using the `least_significant_digit` keyword argument. 
> Floats are generally stored with much higher precision than the data it represents, especially if you 
> deal with observed values. Trailing digits take up a lot of space and may not be relevant. 
> By specifying the least significant digit, you can further enhance the data compression.
> This just gives netCDF more freedom when it packs the data into your harddrive. 
> For instance, knowing that temperature is only accurate to about 0.005 degrees K, it makes sense to just preserve the first 4 digits:
> 
> ~~~
> temp = d.createVariable('Temperature', 'f4', ('time', 'lon', 'lat', 'z'), zlib=True, least_significant_digit=4)
> ~~~
> {: .python}
> 
> Recreating the dataset using the above line can significantly reduce the size of your netCDF, especially on large datasets. 
> You can find more information [here](http://www.unidata.ucar.edu/software/netcdf/workshops/2011/nc4chunking/CompressionAdvice.html). 
> And [here](https://support.hdfgroup.org/HDF5/faq/compression.html) for HDF5 files; you may also be interested by the two following blogs:
> - [HDF5 data compression demystified Part-1](https://www.hdfgroup.org/2015/04/hdf5-data-compression-demystified-1/)
> - [HDF5 Data Compression Demystified Part-2: Performance Tuning](https://www.hdfgroup.org/2017/05/hdf5-data-compression-demystified-2-performance-tuning/)
>
{: .callout}

# Parallel computing for spatio-temporal data analysis: xarray and dask

## [Dask](https://dask.pydata.org/en/latest/) : a flexible parallel computing library for analytic computing


Show the very good introduction [Dask: Parallel Computing in Python](http://matthewrocklin.com/slides/strata-london-2017.html#/) made by [Matthew Rocklin](http://matthewrocklin.com/) at [Strata Data Conference 2017](https://conferences.oreilly.com/strata/strata-eu).
