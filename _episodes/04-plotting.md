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


# What is matplotlib? Why should we learn to use it?

While python offers a large range of python packages for plotting spatio-temporal data, we will focus here 
on the most generic python interface to create maps. Most of other python packages used for plotting spatio-temporal data are based on matplotlib.

# The main principle of matplotlib

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

 
 <img src="{{ page.root }}/fig/figure_axes.png" width="400" alt="figures and axes" align="middle">
 
Here we created one subplot and one axes only. We will give another example afterwards to explain the arguments of the function `add_subplot` in more details.

Then we use the `ax` object to customize our subplot and finally plot data. For instance, we can add:

- a title to our subplot
- a title for x-axis and y-axis
- ticks at chosen location for x-axis and y-axis

~~~
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
ax.set_title('Title of my subplot', fontsize=14)

# set tick labels for x-axis
ax.set_xticklabels(np.arange(10), rotation=45, fontsize=10 )
# set a title for x-axis
ax.set_xlabel("title for x-axis")
# choose where and how many ticks on the x-axes
ax.set_xticks(np.arange(0, 10, 1.0))


# set tick labels for y-axis
ax.set_yticklabels(np.arange(5), rotation=45, fontsize=10 )
# set a title for y-axis
ax.set_ylabel("title for y-axis")
# choose where and how many ticks on the y-axes
ax.set_yticks(np.arange(0, 5, 1.0))
~~~
{: .python}


 
 <img src="{{ page.root }}/fig/figure_axes_customized.png" width="400" alt="figures and axes" align="middle">

## Simple plots - Timeseries

Our goal is to plot a timeserie for North Atlantic Oscillation (NAO) index. We take first sample data i.e. NAO indices
for 10 days only from the 1st of June 2001 to the 10th of June 2001:

~~~
import datetime
dates = [datetime.date( 2001,6,1), 
     datetime.date( 2001,6,2),
     datetime.date( 2001,6,3),
     datetime.date( 2001,6,4),
     datetime.date( 2001,6,5),
     datetime.date( 2001,6,6),
     datetime.date( 2001,6,7),
     datetime.date( 2001,6,8),
     datetime.date( 2001,6,9),
     datetime.date( 2001,6,10)]
# NAO index for each date
nao_index = [ 0.132, -0.058, -0.321, -0.395, -0.216, -0.082, -0.023, -0.012, -0.012, -0.02]
~~~
{: .python}

Then we plot with matplotlib:
~~~
import matplotlib.pyplot as plt
%matplotlib inline
fig = plt.figure()  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
# set a title for this sub-plot
ax.set_title('Time series for NAO index', fontsize=14)
# set labels for x-ticks (dates) and rotate them (45 degrees) for readability
ax.set_xticklabels(dates, rotation=45, fontsize=10 )
# set a title for x-axis
ax.set_xlabel("Dates (YYYY-MM-DD)")
# set a title for y-axis
ax.set_ylabel("NAO index")
# plot nao_index as a function of dates.
ax.plot(dates, nao_index)
~~~
{: .python}

 <img src="{{ page.root }}/fig/sample_data_ts.png" width="400" alt="figures and axes" align="middle">
 

> ## date formatting 
> You can fully control how your dates appear in your plot:
>
> ~~~
>import matplotlib.pyplot as plt
> import matplotlib.dates
> %matplotlib inline
> fig = plt.figure()  # a new figure window
> ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
> # set a title for this sub-plot
> ax.set_title('Time series for NAO index', fontsize=14)
> # set labels for x-ticks (dates) and rotate them (45 degrees) for readability
> ax.set_xticklabels(dates, rotation=45, fontsize=10 )
> # set a title for x-axis
> ax.set_xlabel("Dates")
> # set a title for y-axis
> ax.set_ylabel("NAO index")                
> 
> ax.xaxis.set_major_formatter(
>     matplotlib.dates.DateFormatter('%a %d %b %Y')
>  )
> # plot nao_index as a function of dates.
> ax.plot(dates, nao_index, 'r.-')
> ~~~
> {: .python}
> 
> <img src="{{ page.root }}/fig/sample_data_ts_customized.png" width="400" alt="figures and axes" align="middle">
>
> **DateFormatter**: use [strftime()](http://strftime.org/) format strings
{: .callout}


# What is basemap?

`Basemap` is an extension of matplotlib; one of the most common plotting library for Python. You may have heard or will hear about other python packages for 
plotting spatio-temporal data (for instance pandas, geopandas, pynio & pyngl, pyqgis, plotly, bokeh, cartopy, iris, scikit-learn, seaborn, etc.); many of them
are using matplotlib/basemap underneath for plotting and are data specific. We think it is important to understand matplotlib/basemap and learn how to use
it effectively in your scientific workflow. At the end of the workshop, we will talk about other packages to visualize your data and we hope that this lesson
will make it easier.

## Create simple maps with basemap

As explained in lesson [Intro to Coordinate Reference Systems & Spatial Projections](https://annefou.github.io/metos_python/03-crs_proj/), the projection you choose for
plotting your maps is very important and depends on what you want to visualize and over which region of the globe.

## Plotting raster and vector data with basemap

### plotting raster data

In our first example, we wish to plot the Vorticity fields from [ECMWF ERA-Interim reanalysis](https://www.ecmwf.int/en/research/climate-reanalysis/era-interim) 
for summer 2001 (June, July and August). ECMWF ERA-Interim is a global atmospheric reanalysis from 1979, continuously updated in real time and this dataset is
[freely available](http://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/). However, you would need to [register](https://apps.ecmwf.int/registration/) 
to fully access their [public dataset](http://apps.ecmwf.int/datasets/). If you wish to download your own set of data in python (various parameters and dates) 
you can install the python package called [ECMWF WEB-API](https://software.ecmwf.int/wiki/display/WEBAPI/Web-API+Downloads).
This part is out of scope of this tutorial and we provide a sample data set in netCDF format `EI_VO_Summer2001.nc`. 

> ## Inspect `EI_VO_Summer2001.nc` wth `ncdump`:
>
> ~~~
> ncdump -h ./track_summer2001/indat/EI_VO.nc
> ~~~
> {: .bash}
>
> What can you say about this file?
> 
> > ## Solution
> > ~~~
> > netcdf EI_VO {
> > dimensions:
> > 	lon = 512 ;
> > 	lat = 256 ;
> > 	lev = 1 ;
> > 	time = UNLIMITED ; // (368 currently)
> > variables:
> > 	double lon(lon) ;
> > 		lon:standard_name = "longitude" ;
> > 		lon:long_name = "longitude" ;
> > 		lon:units = "degrees_east" ;
> > 		lon:axis = "X" ;
> > 	double lat(lat) ;
> > 		lat:standard_name = "latitude" ;
> > 		lat:long_name = "latitude" ;
> > 		lat:units = "degrees_north" ;
> > 		lat:axis = "Y" ;
> > 	double lev(lev) ;
> > 		lev:standard_name = "air_pressure" ;
> > 		lev:long_name = "pressure" ;
> > 		lev:units = "Pa" ;
> > 		lev:positive = "down" ;
> > 		lev:axis = "Z" ;
> > 	double time(time) ;
> > 		time:standard_name = "time" ;
> > 		time:units = "hours since 2001-6-1 00:00:00" ;
> > 		time:calendar = "proleptic_gregorian" ;
> > 		time:axis = "T" ;
> > 	float VO(time, lev, lat, lon) ;
> > 		VO:standard_name = "atmosphere_relative_vorticity" ;
> > 		VO:long_name = "Vorticity (relative)" ;
> > 		VO:units = "s**-1" ;
> > 		VO:code = 138 ;
> > 		VO:table = 128 ;
> > 		VO:grid_type = "gaussian" ;
> > 
> > // global attributes:
> > 		:CDI = "Climate Data Interface version 1.7.0 (http://mpimet.mpg.de/cdi)" ;
> > 		:Conventions = "CF-1.4" ;
> > 		:history = "Thu Feb 04 14:28:54 2016: cdo -t ecmwf -f nc copy EI_VO.grb EI_VO.nc" ;
> > 		:institution = "European Centre for Medium-Range Weather Forecasts" ;
> > 		:CDO = "Climate Data Operators version 1.7.0 (http://mpimet.mpg.de/cdo)" ;
> > }
> > ~~~
> > This file contains one variable only called Vorticity (relative), in s**-1, stored on a [lat/lon gaussian grid](https://en.wikipedia.org/wiki/Gaussian_grid) for
> > one level only and 368 times (UNLIMITED dimension which means we can potentialy add more times).
> {: .solution}
{: .challenge}

<br>
Let's plot it on a world map:
~~~
import matplotlib.pyplot as plt
from matplotlib import colors as c
%matplotlib inline
from mpl_toolkits.basemap import Basemap, shiftgrid

import numpy as np
import netCDF4
f = netCDF4.Dataset('EI_VO_850hPa_Summer2001.nc', 'r')
lats = f.variables['lat'][:]
lons = f.variables['lon'][:]
 # read first time and unique level and scale it to the right units
VO = f.variables['VO'][0,0,:,:]*100000 
fig = plt.figure(figsize=[12,15])  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
ax.set_title('ECMWF ERA-Interim VO at 850 hPa 2001-06-01 00:00', fontsize=14)

map = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c', ax=ax)

map.drawcoastlines()
map.fillcontinents(color='#ffe2ab')
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
map.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])

# shift data so lons go from -180 to 180 instead of 0 to 360.
VO,lons = shiftgrid(180.,VO,lons,start=False)
llons, llats = np.meshgrid(lons, lats)
x,y = map(llons,llats)
# make a color map of fixed colors
cmap = c.ListedColormap(['#00004c','#000080','#0000b3','#0000e6','#0026ff','#004cff',
                         '#0073ff','#0099ff','#00c0ff','#00d900','#33f3ff','#73ffff','#c0ffff', 
                         (0,0,0,0),
                         '#ffff00','#ffe600','#ffcc00','#ffb300','#ff9900','#ff8000','#ff6600',
                         '#ff4c00','#ff2600','#e60000','#b30000','#800000','#4c0000'])
bounds=[-200,-100,-75,-50,-30,-25,-20,-15,-13,-11,-9,-7,-5,-3,3,5,7,9,11,13,15,20,25,30,50,75,100,200]
norm = c.BoundaryNorm(bounds, ncolors=cmap.N) # cmap.N gives the number of colors of your palette

cs = map.contourf(x,y,VO, cmap=cmap, norm=norm, levels=bounds,shading='interp')
#
#
## make a color bar
fig.colorbar(cs, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds, ax=ax, orientation='horizontal')
f.close()
~~~
{: .python}

<img src="{{ page.root }}/fig/EI_VO850hPa_2001060100_global.png" width="400" alt="figures and axes" align="middle">

And to zoom over a user-defined area:
~~~
import matplotlib.pyplot as plt
from matplotlib import colors as c
%matplotlib inline
from mpl_toolkits.basemap import Basemap, shiftgrid

import numpy as np
import netCDF4
f = netCDF4.Dataset('EI_VO_850hPa_Summer2001.nc', 'r')
lats = f.variables['lat'][:]
lons = f.variables['lon'][:]
VO = f.variables['VO'][0,0,:,:]*100000  # read first time and unique level
fig = plt.figure(figsize=[12,15])  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
ax.set_title('ECMWF ERA-Interim VO at 850 hPa 2001-06-01 00:00', fontsize=14)

map = Basemap(projection='merc',llcrnrlat=38,urcrnrlat=76,\
            llcrnrlon=-65,urcrnrlon=30, resolution='c', ax=ax)
map.drawcoastlines()
map.fillcontinents(color='#ffe2ab')
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,91.,20.))
map.drawmeridians(np.arange(-180.,181.,10.))
map.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
map.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])

# shift data so lons go from -180 to 180 instead of 0 to 360.
VO,lons = shiftgrid(180.,VO,lons,start=False)
llons, llats = np.meshgrid(lons, lats)
x,y = map(llons,llats)
# make a color map of fixed colors
cmap = c.ListedColormap(['#00004c','#000080','#0000b3','#0000e6','#0026ff','#004cff',
                         '#0073ff','#0099ff','#00c0ff','#00d900','#33f3ff','#73ffff','#c0ffff', 
                         (0,0,0,0),
                         '#ffff00','#ffe600','#ffcc00','#ffb300','#ff9900','#ff8000','#ff6600',
                         '#ff4c00','#ff2600','#e60000','#b30000','#800000','#4c0000'])
bounds=[-200,-100,-75,-50,-30,-25,-20,-15,-13,-11,-9,-7,-5,-3,3,5,7,9,11,13,15,20,25,30,50,75,100,200]
norm = c.BoundaryNorm(bounds, ncolors=cmap.N) # cmap.N gives the number of colors of your palette

cs = map.contourf(x,y,VO, cmap=cmap, norm=norm, levels=bounds,shading='interp')
#
#
## make a color bar
fig.colorbar(cs, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds, ax=ax, orientation='horizontal')
f.close()
~~~
{: .python}

<img src="{{ page.root }}/fig/EI_VO850hPa_2001060100.png" width="400" alt="figures and axes" align="middle">

<br>

### Overlay another field 

We can read another field "Mean Sea level pressure" and overlay it on top of the preceding plot:

~~~
# Add another field on top of the existing VO contours.

f = netCDF4.Dataset('EI_mslp_Summer2001.nc', 'r')
lats = f.variables['lat'][:]
lons = f.variables['lon'][:]
mslp = f.variables['MSL'][0,:,:]/100.0  # mean sea level pressure i.e. surface field.
# shift data so lons go from -180 to 180 instead of 0 to 360.
mslp,lons = shiftgrid(180.,mslp,lons,start=False)
llons, llats = np.meshgrid(lons, lats)
x,y = map(llons,llats)
cs = map.contour(x,y,mslp, zorder=2, colors='black')
ax.clabel(cs, fmt='%.1f',fontsize=9, inline=1)
f.close()
~~~
{: .python}

<img src="{{ page.root }}/fig/EI_VO850hPa_MSLP_2001060100.png" width="400" alt="figures and axes" align="middle">

### Inset locators

The location of the zoomed box can be specified with an integer value:

- 'upper right'  : 1,
- 'upper left'   : 2,
- 'lower left'   : 3,
- 'lower right'  : 4,
- 'right'        : 5,
- 'center left'  : 6,
- 'center right' : 7,
- 'lower center' : 8,
- 'upper center' : 9,
- 'center'       : 10

~~~
import matplotlib.pyplot as plt
from matplotlib import colors as c
%matplotlib inline
from mpl_toolkits.basemap import Basemap, shiftgrid

import numpy as np
import netCDF4
f = netCDF4.Dataset('EI_VO_850hPa_Summer2001.nc', 'r')
lats = f.variables['lat'][:]
lons = f.variables['lon'][:]
VO = f.variables['VO'][0,0,:,:]*100000  # read first time and unique level
fig = plt.figure(figsize=[20,15])  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
ax.set_title('ECMWF ERA-Interim VO at 850 hPa (shading) and MSLP (contour) at 2001-06-01 00:00', fontsize=14)

map = Basemap(projection='merc',llcrnrlat=38,urcrnrlat=76,\
            llcrnrlon=-65,urcrnrlon=30, resolution='c', ax=ax)

map.drawcoastlines()
map.fillcontinents(color='#ffe2ab', zorder=0)
# draw parallels and meridians.
# labels = [left,right,top,bottom]
map.drawparallels(np.arange(-90.,120.,20.),labels=[1,0,0,0])
map.drawmeridians(np.arange(-180.,180.,20.),labels=[0,0,0,1])

# shift data so lons go from -180 to 180 instead of 0 to 360.
VO,lons = shiftgrid(180.,VO,lons,start=False)
llons, llats = np.meshgrid(lons, lats)
x,y = map(llons,llats)
# make a color map of fixed colors
cmap = c.ListedColormap(['#00004c','#000080','#0000b3','#0000e6','#0026ff','#004cff',
                         '#0073ff','#0099ff','#00c0ff','#00d900','#33f3ff','#73ffff','#c0ffff', 
                         (0,0,0,0),
                         '#ffff00','#ffe600','#ffcc00','#ffb300','#ff9900','#ff8000','#ff6600',
                         '#ff4c00','#ff2600','#e60000','#b30000','#800000','#4c0000'])
bounds=[-200,-100,-75,-50,-30,-25,-20,-15,-13,-11,-9,-7,-5,-3,3,5,7,9,11,13,15,20,25,30,50,75,100,200]
norm = c.BoundaryNorm(bounds, ncolors=cmap.N) # cmap.N gives the number of colors of your palette

cs = map.contourf(x,y,VO, cmap=cmap, norm=norm, levels=bounds,shading='interp', zorder=1)
#
#
## make a color bar
fig.colorbar(cs, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds, ax=ax, orientation='horizontal')
f.close()

# Add another field on top of the existing VO contours.

f = netCDF4.Dataset('EI_mslp_Summer2001.nc', 'r')
lats = f.variables['lat'][:]
lons = f.variables['lon'][:]
mslp = f.variables['MSL'][0,:,:]/100.0  # mean sea level pressure i.e. surface field.
# shift data so lons go from -180 to 180 instead of 0 to 360.
mslp,lons = shiftgrid(180.,mslp,lons,start=False)
llons, llats = np.meshgrid(lons, lats)
x,y = map(llons,llats)
cs = map.contour(x,y,mslp, zorder=2, colors='black')
ax.clabel(cs, fmt='%.1f',fontsize=9, inline=1)
f.close()

# Add a rectangle
#import matplotlib.patches as patches

llat=56
ulat=66
llon=-40
rlon=0
x1,y1 = map(llon, llat)
x2,y2 = map(rlon,ulat)
#ax.add_patch(
#    patches.Rectangle(
#        (x1, y1),        # (x,y)
#        x2-x1,           # width
#        y2-y1,           # height
#        fill=False,      # remove background
#        edgecolor='red', # line color
#        linestyle='dashed',
#        linewidth=3
#    )
#)
# Inset locators

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
# 5 indicates the zoom ratio; loc=1 --> upper right
axins = zoomed_inset_axes(ax, 3, loc=1, bbox_to_anchor=(1.5, 1.0), 
                 bbox_transform=ax.figure.transFigure)

mapins = Basemap(projection='cyl',llcrnrlat=llat,urcrnrlat=ulat,\
            llcrnrlon=llon,urcrnrlon=rlon, resolution='c', ax=axins)
mapins.fillcontinents(color='#ddaa66', lake_color='#7777ff')
mapins.drawcoastlines()
#mapins.fillcontinents(color='#ffe2ab', zorder=1)
#mapins.drawcoastlines()
# draw parallels and meridians.
# labels = [left,right,top,bottom]
mapins.drawparallels(np.arange(-90.,120.,2.),labels=[0,0,0,0])
mapins.drawmeridians(np.arange(-180.,180.,10.),labels=[0,0,0,0])
csins = axins.contourf(x,y,VO, cmap=cmap, norm=norm, levels=bounds,shading='interp')
# sub region of the original image
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)


axins.xaxis.set_minor_locator(plt.NullLocator())
axins.yaxis.set_minor_locator(plt.NullLocator())

axes = mark_inset(ax, axins, loc1=2, loc2=4,  
        edgecolor='red', # line color
        linestyle='dashed',
        linewidth=3)
~~~
{:  .python}
### plotting vector data

## Customize your plots


> # Summary
> 
> - Keep in mind the graphic below from the [matplotlib faq](https://matplotlib.org/faq/usage_faq.html) to remember the terminology of a matplotlib plot i.e. 
> what is a Figure and an Axes.
> 
> > <img src="{{ page.root }}/fig/matplotlib_terminology.png" width="400"> 
>
> - Always use the object-oriented interface. Get in the habit of using it from the start of your analysis.
> - For some inspiration, check out the [matplotlib example gallery](http://matplotlib.org/gallery.html) which includes the source code required to 
>    generate each example.
> - Get colornames from matplotlib [here](https://matplotlib.org/examples/color/named_colors.html).
{: .callout}

