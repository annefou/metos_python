---
title: "Intro to Coordinate Reference Systems & Spatial Projections"
teaching: 0
exercises: 0
questions:
- "What are Coordinate Reference Systems?"
objectives:
- "Learn about the key spatial attributes that are needed to work with spatial data including: Coordinate Reference Systems (CRS), Extent and spatial resolution."
keypoints:
- "Coordinate Reference Systems"
---


After completing this activity, you will understand:

- The basic concept of what a Coordinate Reference System (CRS) is and how it impacts data processing, analysis and visualization.
- Understand the basic differences between a geographic and a projected CRS.
- Become familiar with the Universal Trans Mercator (UTM) and Geographic (WGS84) CRSs


This lesson is a copy of the Data Carpentry lesson [Introduction to Coordinate reference systems](http://www.datacarpentry.org/r-spatial-data-management-intro/R/intro-to-coordinate-reference-systems).
Minor changes have been done and python codes have been added for this tutorial (the original lesson had examples in `R`).


#### Getting Started with CRS
Check out this short video highlighting how map projections can make continents
look proportionally larger or smaller than they actually are!

<iframe width="560" height="315" src="https://www.youtube.com/embed/KUF_Ckv8HbE" frameborder="0" allowfullscreen></iframe>

* For more on types of projections, visit
<a href="http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/Datums/003r00000008000000/" target="_blank"> ESRI's ArcGIS reference on projection types.</a>.  
* Read more about <a href="https://source.opennews.org/en-US/learning/choosing-right-map-projection/" target="_blank"> choosing a projection/datum.</a>


## What is a Coordinate Reference System

To define the location of something we often use a coordinate system. This system
consists of an X and a Y value, located within a 2 (or more) -dimensional space.
We live on a 3-dimensional earth that happens to be "round". To define the location of objects on the earth, which is round, we need a coordinate system that adapts to the Earth's shape. When we make maps on paper
or on a flat computer screen, we move from a 3-Dimensional space (the globe) to
a 2-Dimensional space (our computer
screens or a piece of paper). The components of the CRS define how the
"flattening" of data that exists in a 3-D globe space. The CRS also defines the
the coordinate system itself.

<figure>
	<a href="http://ayresriverblog.com/wp-content/uploads/2011/05/image.png">
	<img src="http://ayresriverblog.com/wp-content/uploads/2011/05/image.png"></a>
	<figcaption>A CRS defines the translation between a location on the round earth
	and that same location, on a flattened, 2 dimensional coordinate system.
	Source: http://ayresriverblog.com
	</figcaption>
</figure>

> A coordinate reference system (CRS) is a
> coordinate-based local, regional or global system used to locate geographical
> entities. -- Wikipedia
{; .callout}

## The Components of a CRS

The coordinate reference system is made up of several key components:

* **Coordinate System:** the X, Y grid upon which our data is overlayed and how we define where a point is located in space.
* **Horizontal and vertical units:** The units used to define the grid along the
x, y (and z) axis.
* **Datum:** A modeled version of the shape of the earth which defines the
origin used to place the coordinate system in space. We will explain this further,
below.
* **Projection Information:** the mathematical equation used to flatten objects
that are on a round surface (e.g. the earth) so we can view them on a flat surface
(e.g. our computer screens or a paper map).


## Why CRS is Important

It is important to understand the coordinate system that your data uses -
particularly if you are working with different data stored in different coordinate
systems. If you have data from the same location that are stored in different
coordinate reference systems, **they will not line up in any GIS or other program**
unless you have a program like ArcGIS or QGIS that supports **projection on the
fly**. Even if you work in a tool that supports projection on the fly, you will
want to all of your data in the same projection for performing analysis and processing
tasks.

> <i class="fa fa-star"></i> **Data Tip:** Spatialreference.org provides an
> excellent <a href="http://spatialreference.org/ref/epsg/" target="_blank">online
> library of CRS information.</a>
{: .callout}

### Coordinate System & Units

We can define a spatial location, such as a plot location, using an x- and a
y-value - similar to our cartesian coordinate system displayed in the figure,
above.

For example, the map below, generated in `python` with `matplotlib` shows all of the
continents in the world, in a `Geographic` Coordinate Reference System. The
units are Degrees and the coordinate system itself is **latitude** and
**longitude** with the `origin` being the location where the equator meets
the central meridian on the globe (0,0).


<pre data-executable="true" data-language="python">%matplotlib inline
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
map = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
map.drawcoastlines()
map.fillcontinents(color='black',lake_color='aqua')
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,91.,30.))
map.drawmeridians(np.arange(-180.,181.,60.))
map.drawmapboundary(fill_color='aqua')
plt.title("Global Map: Equidistant Cylindrical Projection \n Units: Degrees - Latitudes/Longitudes")
plt.xticks([-180,-100,0,100,180])
plt.yticks([-90,-50,0,50,90])
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Latitude (Degrees)')
plt.show()
</pre>

<img src="{{ page.root }}/fig/lat-long-example-1.png">

We can add three coordinate locations to our map. Note that the UNITS are
in decimal **degrees** (latitude, longitude):

* Boulder, Colorado:  40.0274, -105.2519
* Oslo, Norway: 59.9500, 10.7500
* Mallorca, Spain: 39.6167, 2.9833

Let's create a second map with the locations overlayed on top of the continental
boundary layer.

<pre data-executable="true" data-language="python">%matplotlib inline
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
map = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')


map.drawcoastlines()
map.fillcontinents(color='black',lake_color='aqua', zorder = 1)
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,91.,30.))
map.drawmeridians(np.arange(-180.,181.,60.))
map.drawmapboundary(fill_color='aqua', zorder=0)

# Add three coordinate locations to our map
# Boulder, Colorado:  40.0274, -105.2519
# Oslo, Norway: 59.9500, 10.7500
# Mallorca, Spain: 39.6167, 2.9833
lats = [40.0274, 59.9500, 39.6167]
lons = [-105.2519,10.7500,2.9833]
plt.scatter(lons,lats,s=100, c='red', zorder=2)

plt.title("Global Map: Equidistant Cylindrical Projection \n Units: Degrees - Latitudes/Longitudes")
plt.xticks([-180,-100,0,100,180])
plt.yticks([-90,-50,0,50,90])
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Latitude (Degrees)')

plt.show()
</pre>

<img src="{{ page.root }}/fig/add-lat-long-locations-1.png">

## Geographic CRS - The Good & The Less Good

Geographic coordinate systems in decimal degrees are helpful when we need to
locate places on the Earth. However, latitude and longitude
locations are not located using uniform measurement units. Thus, geographic
CRSs are not ideal for measuring distance. This is why other projected `CRS`
have been developed.


<figure>
	<a href="{{ page.root }}/fig/LatLongfromGlobeCenter-ESRI.gif">
	<img src="{{ page.root }}/fig/LatLongfromGlobeCenter-ESRI.gif"></a>
	<figcaption>A geographic coordinate system locates latitude and longitude
	location using angles. Thus the spacing of each line of latitude moving north
	and south is not uniform.
	Source: ESRI
	</figcaption>
</figure>

## Projected CRS - Robinson

We can view the same data above, in another CRS - `Robinson`. `Robinson` is a
**projected** `CRS`. Notice that the country boundaries on the map - have a
different shape compared to the map that we created above in the `CRS`:  
**Geographic lat/long WGS84**.


<pre data-executable="true" data-language="python">%matplotlib inline
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
map = Basemap(projection='robin',lon_0=0,resolution='c')
map.drawcoastlines()
map.fillcontinents(color='black',lake_color='aqua', zorder=1)
map.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0]) # draw parallels
map.drawmeridians(np.arange(0.,420.,60.),labels=[0,0,0,1]) # draw meridians
map.drawmapboundary(fill_color='aqua',zorder=0)
plt.title("Global Map: Robinson Projection \n Units: Degrees - Latitudes/Longitudes")
plt.show()
</pre>

<img src="{{ page.root }}/fig/robinson-example-2.png">

Now what happens if you try to add the same Lat / Long coordinate locations that
we used above, to our map, with the `CRS` of `Robinsons`?

<pre data-executable="true" data-language="python">%matplotlib inline
import matplotlib.pyplot as plt
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
map = Basemap(projection='robin',lon_0=0,resolution='c')
map.drawcoastlines()
map.fillcontinents(color='black',lake_color='aqua', zorder=1)
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0]) # draw parallels
map.drawmeridians(np.arange(0.,420.,60.),labels=[0,0,0,1]) # draw meridians
map.drawmapboundary(fill_color='aqua',zorder=0)
# Add three coordinate locations to our map
# Boulder, Colorado:  40.0274, -105.2519
# Oslo, Norway: 59.9500, 10.7500
# Mallorca, Spain: 39.6167, 2.9833
lats = [40.0274, 59.9500, 39.6167]
lons = [-105.2519,10.7500,2.9833]
plt.scatter(lons,lats,s=100, c='red', zorder=2)
plt.title("Global Map: Robinson Projection")
plt.show()
</pre>

<img src="{{ page.root }}/fig/add-robinson-locations-2.png">

Notice above that when we try to add lat/long coordinates in degrees, to a map
in a different `CRS`, that the points are not in the correct location. We need
to first convert the points to the new projection - a process often referred
to as **reprojection**.

<pre data-executable="true" data-language="python">%matplotlib inline
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
map = Basemap(projection='robin',lon_0=0,resolution='c')
map.drawcoastlines()
map.fillcontinents(color='black',lake_color='aqua', zorder=1)
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0]) # draw parallels
map.drawmeridians(np.arange(0.,420.,60.),labels=[0,0,0,1]) # draw meridians
map.drawmapboundary(fill_color='aqua',zorder=0)
# Add three coordinate locations to our map
# Boulder, Colorado:  40.0274, -105.2519
# Oslo, Norway: 59.9500, 10.7500
# Mallorca, Spain: 39.6167, 2.9833
lats = [40.0274, 59.9500, 39.6167]
lons = [-105.2519,10.7500,2.9833]
# notice the coordinate system in the Robinson projection (CRS) is DIFFERENT
# from the coordinate values for the same locations in a geographic CRS.
# Reprojection is very simple in python: 
x,y = map(lons,lats)
print(x)
print(y)
plt.scatter(x,y,s=100, c='red', zorder=2)
plt.title("Global Map: Robinson Projection)
plt.show()
</pre>

<img src="{{ page.root }}/fig/add-robinson-locations-reprojection-2.png">


## Compare Maps

Both of the plots above look visually different and also use a different
coordinate system. Let's look at both, side by side, with the actual **graticules**
or latitude and longitude lines rendered on the map.

NOTE: The code for this map can
be found in the .py document that is available for download at the bottom of this
page!

<img src="{{ page.root }}/fig/compare_cyl_robin.png" width="400">

<pre data-executable="true" data-language="python">%matplotlib inline
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# get two plots in the same figure: 2 lines and 1 row
fig, axes = plt.subplots(2, 1)

##########################################################
# Subplot -1 
##########################################################
axes[0].set_title("Equidistant Cylindrical Projection (long/lat Degrees)")
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
map = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c', ax=axes[0])


map.drawcoastlines()
map.fillcontinents(color='black',lake_color='aqua', zorder = 1)
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,91.,10.))
map.drawmeridians(np.arange(-180.,181.,10.))
map.drawmapboundary(fill_color='aqua', zorder=0)

# Add three coordinate locations to our map
# Boulder, Colorado:  40.0274, -105.2519
# Oslo, Norway: 59.9500, 10.7500
# Mallorca, Spain: 39.6167, 2.9833
lats = [40.0274, 59.9500, 39.6167]
lons = [-105.2519,10.7500,2.9833]
axes[0].scatter(lons,lats,s=100, c='red', zorder=2)


###########################################################
# Subplot-2
###########################################################

axes[1].set_title("Robinson projection (meters)")
# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.
map = Basemap(projection='robin',lon_0=0,resolution='c', ax=axes[1])
map.drawcoastlines()
map.fillcontinents(color='black',lake_color='aqua', zorder=1)
# draw parallels and meridians.
map.drawparallels(np.arange(-90.,120.,10.))
map.drawmeridians(np.arange(0.,360.,10.))
map.drawmapboundary(fill_color='aqua',zorder=0)
# Add three coordinate locations to our map
# Boulder, Colorado:  40.0274, -105.2519
# Oslo, Norway: 59.9500, 10.7500
# Mallorca, Spain: 39.6167, 2.9833
lats = [40.0274, 59.9500, 39.6167]
lons = [-105.2519,10.7500,2.9833]
x,y = map(lons,lats)
axes[1].scatter(x,y,s=100, c='red', zorder=2)

plt.show()
</pre>


## Why Multiple CRS?

You may be wondering, why bother with different CRSs if it makes our
analysis more complicated? Well, each `CRS` is optimized to best represent:

* Shape and/or
* Scale / distance and/or
* Area

of features in the data. And no one CRS is great at optimizing shape, distance AND
area. Some CRSs are optimized for shape, some distance, some area. Some
CRSs are also optimized for particular regions -
for instance the United States, or Europe or Nordic countries. Discussing `CRS` as it optimizes shape,
distance and area is beyond the scope of this tutorial, but it's important to
understand that the `CRS` that you chose for your data, will impact working with
the data!


> ## Challenge
>
> 1. Compare the maps of the globe above. What do you notice about the shape of the
> various countries. Are there any signs of distortion in certain areas on either
> map? Which one is better?
> 
> 2. Look at the image below - which depicts maps of the United States in 4 different
> `CRS`s. What visual differences do you notice in each map? Look up each projection
> online, what elements (shape,area or distance) does each projection used in
> the graphic below optimize?
>
{: .challenge}
***

<figure>
    <a href="https://earthdatascience.org/images/course-materials/earth-analytics/week-5/different_projections.jpg">
    <img src="{{ page.root }}/fig/different_projections.jpg">
    </a>

    <figcaption>Maps of the United States in different CRS including Mercator
    (upper left), Albers equal area (lower left), UTM (Upper RIGHT) and
    WGS84 Geographic (Lower RIGHT).
    Notice the differences in shape and orientation associated with each
    CRS. These differences are a direct result of the
    calculations used to "flatten" the data onto a two dimensional map.
    Source: opennews.org</figcaption>
</figure>


## Geographic vs Projected CRS


The above maps provide examples of the two main types of coordinate systems:

1. **Geographic coordinate systems:** coordinate systems that span the entire
globe (e.g. latitude / longitude).
2. **Projected coordinate Systems:** coordinate systems that are localized to
minimize visual distortion in a particular region (e.g. Robinson, UTM, State Plane)


All the projections available in matplotlib can be found [here](https://matplotlib.org/basemap/users/mapsetup.html).
