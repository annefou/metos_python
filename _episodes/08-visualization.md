---
title: "Visualize and Publish with Python"
teaching: 0
exercises: 0
questions:
- "How to create animation plots and publish them on the web?"
objectives:
- "Learn how to create simple animations with python"
- "Learn to publish your python notebook on the web (gist and nbviewer)"
keypoints:
- "Get an overview of nbviewer"
---

# Save your animations in `mp4`

We are taking one of our first example where we plot the ECMWF ERA-Interim Vorticity over a pre-defined geographical area.

To avoid downloading large datasets on your laptop, we use one frame only and randomly "perturb" the Vorticity field to demonstrate how
to create and save your animations in python:


~~~
def drawmap(ax,map,x,y,VO, cmap, bounds, norm, title):
    
    ax.set_title(title, fontsize=14)

    map.drawcoastlines()
    map.fillcontinents(color='#ffe2ab')
# draw parallels and meridians.
    map.drawparallels(np.arange(-90.,91.,20.))
    map.drawmeridians(np.arange(-180.,181.,10.))
    map.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    cs = map.contourf(x,y,VO, cmap=cmap, norm=norm, levels=bounds,shading='interp', zorder=1, ax=ax)

    return cs
    
def myanimate(i, ax, map, x,y,VO, cmap, bounds, norm):
    ax.clear()
    # change VO (randomly...)
    VO += 0.1 * np.random.randn()
    new_contour = drawmap(ax,map,x,y,VO, cmap, bounds, norm, 'ECMWF ERA-Interim VO at 850 hPa: Frame %03d'%(i) ) 
    return new_contour
	
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib.animation as animation
%matplotlib inline
from mpl_toolkits.basemap import Basemap, shiftgrid
import numpy as np
import netCDF4


FFMpegWriter = animation.writers['ffmpeg']
metadata = dict(title='ECMWF ERA-Interim VO at 850 hPa from 2001-06-01 00:00', artist='Carpentry@UIO',
                comment='Movie for ECMWF ERA-Interim VO at 850 hPa from 2001-06-01 00:00')
writer = FFMpegWriter(fps=20, metadata=metadata)


f = netCDF4.Dataset('EI_VO_850hPa_Summer2001.nc', 'r')
lats = f.variables['lat'][:]
lons = f.variables['lon'][:]
VO = f.variables['VO'][0,0,:,:]*100000  # read first time and unique level
fig = plt.figure(figsize=[12,15])  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)


map = Basemap(projection='merc',llcrnrlat=38,urcrnrlat=76,\
            llcrnrlon=-65,urcrnrlon=30, resolution='c', ax=ax)
    
map.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
# make a color map of fixed colors
cmap = c.ListedColormap(['#00004c','#000080','#0000b3','#0000e6','#0026ff','#004cff',
                         '#0073ff','#0099ff','#00c0ff','#00d900','#33f3ff','#73ffff','#c0ffff', 
                         (0,0,0,0),
                         '#ffff00','#ffe600','#ffcc00','#ffb300','#ff9900','#ff8000','#ff6600',
                         '#ff4c00','#ff2600','#e60000','#b30000','#800000','#4c0000'])
bounds=[-200,-100,-75,-50,-30,-25,-20,-15,-13,-11,-9,-7,-5,-3,3,5,7,9,11,13,15,20,25,30,50,75,100,200]
norm = c.BoundaryNorm(bounds, ncolors=cmap.N) # cmap.N gives the number of colors of your palette
    

# shift data so lons go from -180 to 180 instead of 0 to 360.
VO,lons = shiftgrid(180.,VO,lons,start=False)
llons, llats = np.meshgrid(lons, lats)
x,y = map(llons,llats)

first_contour = drawmap(ax,map,x,y,VO,cmap, bounds, norm, 'ECMWF ERA-Interim VO at 850 hPa 2001-06-01 00:00' ) 

## make a color bar
fig.colorbar(first_contour, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds, ax=ax, orientation='horizontal')

ani = animation.FuncAnimation(fig, myanimate, frames=np.arange(50), 
    fargs=(ax, map, x,y,VO, cmap, bounds, norm), interval=50)
ani.save("writer_ECMWF_EI_VO_850hPa_2001060100.mp4")

f.close()
~~~
{: .python}


# Embedded animations within your jupyter notebook

The main goal here is to create animations embedded within your jupyter notebook. This is fairly simple to plot your animation within your jupyter notebook.

Let's continue our previous example, and add the following:

~~~
from IPython.display import HTML

HTML(ani.to_html5_video())
~~~
{: .python}

<video src="{{ page.root }}/fig/writer_ECMWF_EI_VO_850hPa_2001060100.mp4" poster="{{ page.root }}/fig/EI_VO850hPa_2001060100.png" width="400" controls preload></video>

# Share your jupyter notebooks (nbviewer)

To be able to share your jupyter notebook:

- Save your jupyter notebook on your local computer (rename it as `share_your_notebook_DC.ipynb`); 
the extension `ipynb` is the default extension for a jupyter notebook and you usually do not need to add it (added automatically)
- Open your saved notebook file (`share_your_notebook_DC.ipynb`) with your favorite editor and copy its content
- Open a new window in your web browser at [http://www.github.com](http://www.github.com) and login with your github username and password (you need to register 
beforehand if you don't have a github account yet).
- Open another window or tab in your web browser at [https://gist.github.com/](https://gist.github.com/) 
- Paste the content in the main window and add a title and a description
- Click on `Create public gist`
- Copy the `gist key` that appears in your url (it has been generated when you clicked on `create public key`)
- Go to  [http://nbviewer.jupyter.org](http://nbviewer.jupyter.org) and paste your `gist key` and click on `Go!`
- Then you can share the resulting url 

For instance, the jupyter notebook generated has been shared and can be viewed [here](http://nbviewer.jupyter.org/gist/annefou/5e5750b90a99b5d6b3de9f328a77dccc).

> ### Rendering jupyter notebook on github
> 
> You can also store your jupyter notebook on github (and you are strongly encouraged to use a version control to keep your programs...) and
> according there is no interactive features or any javascript embedded, github will automatically show your jupyter notebook.
>
{: .callout}



> ### Other interesting python packages 
>
> Packages that are worth to mention for analyzing spatio-temporal data:
> 
> - "matplotlib, geopandas, pynio & pyngl, pyqgis, plotly, bokeh & gmap, cartopy, iris"
> - "nodebox-opengl - For playing around with animations"
> - "pandas, pytables, fiona, descartes, pyproj"
{: .callout}
