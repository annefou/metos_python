---
title: "Plotting spatio-temporal data with Python"
teaching: 0
exercises: 0
questions:
- "How can I create maps with python?"
objectives:
- "Learn how to plot spatio-temporal data with python."
keypoints:
- "matplotlib and basemap"
---

This tutorial is based from the [basemap tutorial](https://basemaptutorial.readthedocs.io/en/latest/).


# What is basemap? Why should we learn to use it?

While python offers a large range of python packages for plotting spatio-temporal data, we will focus here 
on the most generic python interface to create maps. Most of other python packages used for plotting spatio-temporal data are based on matplotlib and basemap.

`Basemap` is an extension of matplotlib; one of the most common plotting library for Python. You may have heard or will hear about other python packages for 
plotting spatio-temporal data (for instance pandas, geopandas, pynio & pyngl, pyqgis, plotly, bokeh, cartopy, iris, scikit-learn, seaborn, etc.); many of them
are using matplotlib/basemap underneath for plotting and are data specific. We think it is important to understand matplotlib/basemap and learn how to use
it effectively in your scientific workflow. At the end of the workshop, we will talk about other packages to visualize your data and we hope that this lesson
will make it easier.

# The main principle of matplotlib and basemap

First, matplotlib has two user interfaces:

- The first mimics MATLAB plotting and uses the pylab interface. 
- The second option is an object-oriented interface which is much more powerful.

When plotting with matplotlib, it is very important to know and understand that there are two approaches even though the reasons of this dual approach is outside
the scope of this lesson.

When searching for help on the internet, you will find solutions where the two approaches are mixed which may be very confusing for you. The best for new codes
is to stick to the object-oriented interface and this is what we will show in this lesson.

> ## Key Point
> New matplotlib users should learn and use the object oriented interface.
{: .callout}


## What is a `Figure` and an `Axes`?

The main idea with object-oriented programming is to have objects that one can apply functions and actions on, and 
no object or program states should be global (such as the MATLAB-like API). 
The real advantage of this approach becomes apparent when more than one figure is created, or when a figure contains more than one subplot 
as we will see in this tutorial.

To use the object-oriented API we need to create a new figure instance and store it in a variable; we call this variable `fig` but you can choose any name. 
Actually this is what we will need to do when we create more than one figure!

A figure can contain several plots (also called sub-plots) so the first thing to do is to choose how many sub-plots your figure will contain. This is done
with the `add_subplot` method of an object of type `figure`:

~~~
import matplotlib.pyplot as plt
fig = plt.figure()  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
~~~
{: .python}

The resulting figure is:

 
 <img src="{{ page.root }}/fig/figure_axes.png" width="200" alt="raster concept" align="middle">
 
Here we created one subplot and one axes only. We will give another example afterwards to explain the arguments of the function `add_subplot` in more details.

Then we use the `ax` object to make our plot. Let's make a very simple plot:

~~~
import pandas

data = pandas.read_csv('naoi_summer2001.csv')
~~~
{: .python}

 
## Plotting raster and vector data with basemap

### plotting raster data

### plotting vector data

## Customize your plots


> ## Summary
> 
> - Keep in mind the graphic below from the [matplotlib faq](https://matplotlib.org/faq/usage_faq.html) to remember the terminology of a matplotlib plot i.e. 
> what is a Figure and an Axes.
> 
> > <img src="{{ page.root }}/fig/matplotlib_terminology.png" width="400"> 
>
> - Always use the object-oriented interface. Get in the habit of using it from the start of your analysis.
> - For some inspiration, check out the [matplotlib example gallery](http://matplotlib.org/gallery.html) which includes the source code required to 
>    generate each example.
{: .callout}

