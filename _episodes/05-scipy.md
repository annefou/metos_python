---
title: "Data analysis with python"
teaching: 0
exercises: 0
questions:
- "What is pandas, geopandas, SciPy?"
- "Why using GeoPandas?"
- "How can I use Scipy?"
objectives:
- "Learn about pandas and geopandas for spatio-temporal data analysis"
- "Learn about [SciPy](https://www.scipy.org/about.html), a Python-based ecosystem of open-source software for mathematics, science, and engineering."
- "Using SciPy clustering algorithms on satellite images"
keypoints:
- "pandas, geopandas, scipy library"
---

[SciPy](https://www.scipy.org/about.html) is a Python-based ecosystem of open-source software for mathematics, science, and engineering. 
In particular, these are some of the core packages:

- [NumPy](http://www.numpy.org/): the fundamental package for numerical computation. It defines the numerical array and matrix types and basic operations on them.
- [SciPy](https://www.scipy.org/scipylib/index.html) library:  a collection of numerical algorithms and domain-specific toolboxes, including signal processing, optimization, statistics and much more.
- [Matplotlib](http://matplotlib.org/): a mature and popular plotting package, that provides publication-quality 2D plotting as well as rudimentary 3D plotting
- [IPython](http://ipython.org/): a rich interactive interface, letting you quickly process data and test ideas. The IPython notebook works in your web browser, allowing you to document your computation in an easily reproducible form.
- [Sympy](http://www.sympy.org/): for symbolic mathematics and computer algebra.
- [pandas](http://pandas.pydata.org/): providing high-performance, easy to use data structures.
- [nose](https://nose.readthedocs.org/en/latest/): a framework for testing Python code.

We won't cover the usage of all these packages and will only give a few examples that are meaningful when working with spatio-temporal data.


You know some of these packages, for instance [NumPy](http://www.numpy.org/) and [Matplotlib](http://matplotlib.org/); we have used them in previous chapters.

We also use partly [IPython](http://ipython.org/) when using jupyter notebooks.

The usage of [nose](https://nose.readthedocs.org/en/latest/) and [Sympy](http://www.sympy.org/) are both outside the scope of this lesson.



# pandas and geopandas

Several parts of this lessons were copied from [Python for ecologists](http://www.datacarpentry.org/python-ecology-lesson/), [Plotting an Programming in Python](https://swcarpentry.github.io/python-novice-gapminder) and
[Vector Data processing Using Python Tools](https://geohackweek.github.io/vector/).

## Pandas in Python

One of the best options for working with tabular data in Python is to use the [Python Data Analysis Library](http://pandas.pydata.org/) (a.k.a. Pandas). 
The Pandas library provides data structures, produces high quality plots with [matplotlib](http://matplotlib.org/) and integrates nicely with other 
libraries that use [NumPy](http://www.numpy.org/) arrays.

To import the `pandas` library:

~~~
import pandas as pd
~~~
{: .python}

It is very common to give `pd` as a nickname for `pandas` to shorten the command. This means we don’t have to type out pandas each time we call a Pandas function.

`pandas` can handle a large variety of data formats ranging from `csv` to `HDF5` and `JSON`:


## Geopandas in Python

Geopandas is not part of the official SciPy ecosystem but has a number of features that can ease our work when manipulating spatio-temporal data.

# SciPy

- scipy.cluster Vector quantization / Kmeans
- scipy.constants Physical and mathematical constants
- scipy.fftpack Fourier transform
- scipy.integrate Integration routines
- scipy.interpolate Interpolation
- scipy.io Data input and output
- scipy.linalg Linear algebra routines
- scipy.ndimage n-dimensional image package
- scipy.odr Orthogonal distance regression
- scipy.optimize Optimization
- scipy.signal Signal processing
- scipy.sparse Sparse matrices
- scipy.spatial Spatial data structures and algorithms
- scipy.special Any special mathematical functions
- scipy.stats Statistics

## K-Means Clustering of a Satellite Images using Scipy

This part is taken from the excellent [blog of Max Köning](http://geoinformaticstutorial.blogspot.no/2016/02/k-means-clustering-of-satellite-images.html).

