---
layout: page
title: Setup
permalink: /setup/
---

To follow this lesson, you would need:

1. [The Bash Shell](#installing-the-bash-shell)
2. [Git](#installing-git)
3. [Text editor](#installing-a-text-editor)
4. [Install Python](#installing-python-using-anaconda)
5. [Install netCDF, HDF python packages](#installing-additional-python-libraries-using-anaconda)

## Installing the Bash Shell

<div id="shell"> <!-- Start of 'shell' section. -->
  <h3>The Bash Shell</h3>

  <p>
    Bash is a commonly-used shell that gives you the power to do simple
    tasks more quickly.
  </p>

  <div class="row">
    <div class="col-md-4">
      <h4 id="shell-windows">Windows</h4>
      <a href="https://www.youtube.com/watch?v=339AEqk9c-8">Video Tutorial</a>
      <ol>
        <li>Download the Git for Windows <a href="https://git-for-windows.github.io/">installer</a>.</li>
        <li>Run the installer and follow the steps bellow:
          <ol>
            <!-- Git 2.8.2 Setup -->
            <!-- Information -->
            <li>Click on "Next".</li>
            <!-- Select Components -->
            <li>Click on "Next".</li>
            <!-- Adjusting your PATH environment -->
            <li>
              <strong>
                Keep "Use Git from the Windows Command Prompt" selected and click on "Next".
              </strong>
                If you forgot to do this programs that you need for the workshop will not work properly.
                If this happens rerun the installer and select the appropriate option.
            </li>
            <!-- Choosing the SSH executable -->
            <li>Click on "Next".</li>
            <!-- Configuring the line ending conversions -->
            <li>
              <strong>
                Keep "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".
              </strong>
            </li>
            <!-- Configuring the terminal emulator to use with Git Bash -->
            <li>
              <strong>
                Keep "Use Windows' default console window" selected and click on "Next".
              </strong>
            </li>
            <!-- Configuring experimental performance tweaks -->
            <li>Click on "Install".</li>
            <!-- Installing -->
            <!-- Completing the Git Setup Wizard -->
            <li>Click on "Finish".</li>
          </ol>
        </li>
        <li>
          If your "HOME" environment variable is not set (or you don't know what this is):
          <ol>
            <li>Open command prompt (Open Start Menu then type <code>cmd</code> and press [Enter])</li>
            <li>
              Type the following line into the command prompt window exactly as shown:
              <p><code>setx HOME "%USERPROFILE%"</code></p>
            </li>
            <li>Press [Enter], you should see <code>SUCCESS: Specified value was saved.</code></li>
            <li>Quit command prompt by typing <code>exit</code> then pressing [Enter]</li>
          </ol>
        </li>
      </ol>
      <p>This will provide you with both Git and Bash in the Git Bash program.</p>
    </div>
    <div class="col-md-4">
      <h4 id="shell-macosx">Mac OS X</h4>
      <p>
        The default shell in all versions of Mac OS X is Bash, so no
        need to install anything.  You access Bash from the Terminal
        (found in
        <code>/Applications/Utilities</code>).
        See the Git installation <a href="https://www.youtube.com/watch?v=9LQhwETCdwY ">video tutorial</a>
        for an example on how to open the Terminal.
        You may want to keep
        Terminal in your dock for this workshop.
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="shell-linux">Linux</h4>
      <p>
        The default shell is usually Bash, but if your
        machine is set up differently you can run it by opening a
        terminal and typing <code>bash</code>.  There is no need to
        install anything.
      </p>
    </div>
  </div>
</div> <!-- End of 'shell' section. -->



## Installing Git

<div id="git"> <!-- Start of 'Git' section. GitHub browser compatability
           is given at https://help.github.com/articles/supported-browsers/-->
  <h3>Git</h3>
  <p>
    Git is a version control system that lets you track who made changes
    to what when and has options for easily updating a shared or public
    version of your code
    on <a href="https://github.com/">github.com</a>. You will need a
    <a href="https://help.github.com/articles/supported-browsers/">supported</a>
    web browser (current versions of Chrome, Firefox or Safari,
    or Internet Explorer version 9 or above).
  </p>
  <p>
    You will need an account at <a href="https://github.com/">github.com</a>
    for parts of the Git lesson. Basic GitHub accounts are free. We encourage
    you to create a GitHub account if you don't have one already.
    Please consider what personal information you'd like to reveal. For
    example, you may want to review these
    <a href="https://help.github.com/articles/keeping-your-email-address-private/">instructions
    for keeping your email address private</a> provided at GitHub.
  </p>

  <div class="row">
    <div class="col-md-4">
      <h4 id="git-windows">Windows</h4>
      <p>
        Git should be installed on your computer as part of your Bash
        install (described above).
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="git-macosx">Mac OS X</h4>
      <a href="https://www.youtube.com/watch?v=9LQhwETCdwY ">Video Tutorial</a>
      <p>
        <strong>For OS X 10.9 and higher</strong>, install Git for Mac
        by downloading and running the most recent "mavericks" installer from
        <a href="http://sourceforge.net/projects/git-osx-installer/files/">this list</a>.
        After installing Git, there will not be anything in your <code>/Applications</code> folder,
        as Git is a command line program.
        <strong>For older versions of OS X (10.5-10.8)</strong> use the
        most recent available installer labelled "snow-leopard"
        <a href="http://sourceforge.net/projects/git-osx-installer/files/">available here</a>.
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="git-linux">Linux</h4>
      <p>
        If Git is not already available on your machine you can try to
        install it via your distro's package manager. For Debian/Ubuntu run
        <code>sudo apt-get install git</code> and for Fedora run
        <code>sudo yum install git</code>.
      </p>
    </div>
  </div>
</div> <!-- End of 'Git' section. -->

## Installing a Text Editor

<div id="editor"> <!-- Start of 'editor' section. -->
  <h3>Text Editor</h3>

  <p>
    When you're writing code, it's nice to have a text editor that is
    optimized for writing code, with features like automatic
    color-coding of key words.  The default text editor on Mac OS X and
    Linux is usually set to Vim, which is not famous for being
    intuitive.  if you accidentally find yourself stuck in it, try
    typing the escape key, followed by <code>:q!</code> (colon, lower-case 'q',
    exclamation mark), then hitting Return to return to the shell.
  </p>

  <div class="row">
    <div class="col-md-4">
      <h4 id="editor-windows">Windows</h4>
      <a href="https://www.youtube.com/watch?v=339AEqk9c-8">Video Tutorial</a>
      <p>
        nano is a basic editor and the default that instructors use in the workshop.
        To install it,
        download the <a href="{{site.swc_installer}}">
          {% if page.carpentry == "swc" %}
          Software Carpentry
          {% elsif page.carpentry == "dc" %}
          Data Carpentry
          {% elsif page.carpentry == "lc" %}
          Library Carpentry
          {% endif %}
          Windows installer
	</a>
        and double click on the file to run it.
        <strong>This installer requires an active internet connection.</strong>
      </p>
      <p>
        Others editors that you can use are
        <a href="http://notepad-plus-plus.org/">Notepad++</a> or
        <a href="http://www.sublimetext.com/">Sublime Text</a>.
        <strong>Be aware that you must
          add its installation directory to your system path.</strong>
        Please ask your instructor to help you do this.
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="editor-macosx">Mac OS X</h4>
      <p>
        nano is a basic editor and the default that instructors use in the workshop.
        See the Git installation <a href="https://www.youtube.com/watch?v=9LQhwETCdwY ">video tutorial</a>
        for an example on how to open nano.
        It should be pre-installed.
      </p>
      <p>
        Others editors that you can use are
        <a href="http://www.barebones.com/products/textwrangler/">Text Wrangler</a> or
        <a href="http://www.sublimetext.com/">Sublime Text</a>.
      </p>
    </div>
    <div class="col-md-4">
      <h4 id="editor-linux">Linux</h4>
      <p>
        nano is a basic editor and the default that instructors use in the workshop.
        It should be pre-installed.
      </p>
      <p>
        Others editors that you can use are
        <a href="https://wiki.gnome.org/Apps/Gedit">Gedit</a>,
        <a href="http://kate-editor.org/">Kate</a> or
        <a href="http://www.sublimetext.com/">Sublime Text</a>.
      </p>
    </div>
  </div>
</div> <!-- End of 'editor' section. -->

## Installing Python Using Anaconda

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well. Installing all of its scientific packages
individually can be a bit difficult, however, so we recommend the all-in-one
installer [Anaconda][anaconda].

Regardless of how you choose to install it, please make sure you install Python
version 3.6. Also, please set up your python environment at 
least a day in advance of the workshop.  If you encounter problems with the 
installation procedure, ask your workshop organizers via e-mail for assistance so
you are ready to go as soon as the workshop begins.

### Windows - [Video tutorial][video-windows]

1. Open [http://continuum.io/downloads][continuum-windows]
   with your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using _MOST_ of the
   default settings. The only exception is to check the 
   **Make Anaconda the default Python** option.

### Mac OS X - [Video tutorial][video-mac]

1. Open [http://continuum.io/downloads][continuum-mac]
   with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.

### Linux

Note that the following installation steps require you to work from the shell. 
If you run into any difficulties, please request help before the workshop begins.

1.  Open [http://continuum.io/downloads][continuum-linux] with your web browser.

2.  Download the Python 3 installer for Linux.

3.  Install Python 3 using all of the defaults for installation.

    a.  Open a terminal window.

    b.  Navigate to the folder where you downloaded the installer

    c.  Type

    ~~~
    $ bash Anaconda3-
    ~~~
    {: .bash}

    and press tab.  The name of the file you just downloaded should appear.

    d.  Press enter.

    e.  Follow the text-only prompts.  When the license agreement appears (a colon
        will be present at the bottom of the screen) hold the down arrow until the 
        bottom of the text. Type `yes` and press enter to approve the license. Press 
        enter again to approve the default location for the files. Type `yes` and 
        press enter to prepend Anaconda to your `PATH` (this makes the Anaconda 
        distribution the default Python).

## Getting the Data

The data we will be using is a small dataset created for this lesson. 
To obtain it, download and unzip the file 
[metos-python-data.tar](https://zenodo.org/record/995709/files/metos-python-data.tar).

In order to follow the presented material, you should launch a Jupyter 
notebook in the root directory (see [Starting Python](#Starting-Python)).

## Starting Python

We will teach Python using the [Jupyter notebook][jupyter], a 
programming environment that runs in a web browser. Jupyter requires a reasonably 
up-to-date browser, preferably a current version of Chrome, Safari, or Firefox 
(note that Internet Explorer version 9 and below are *not* supported). If you 
installed Python using Anaconda, Jupyter should already be on your system. If 
you did not use Anaconda, use the Python package manager pip
(see the [Jupyter website][jupyter-install] for details.)

To start the notebook, open a terminal or git bash and type the command:

~~~
$ jupyter notebook
~~~
{: .bash}

To start the Python interpreter without the notebook, open a terminal 
or Git Bash and type the command:

~~~
$ python
~~~
{: .bash}

[anaconda]: https://www.continuum.io/anaconda
[continuum-mac]: http://continuum.io/downloads#_macosx
[continuum-linux]: http://continuum.io/downloads#_unix
[continuum-windows]: http://continuum.io/downloads#_windows
[jupyter]: http://jupyter.org/
[jupyter-install]: http://jupyter.readthedocs.io/en/latest/install.html#optional-for-experienced-python-developers-installing-jupyter-with-pip
[python]: https://python.org
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA

## Installing additional Python libraries Using Anaconda

To install additional Python packages/libraries, you need to open a Terminal, and then follow the instructions below.

### netCDF4:

For Windows, Linux and Mac OS X:

~~~
$ conda config --add channels conda-forge
$ conda install netcdf4
~~~
{: .bash}



### HDF5

We will be using HDF5 python library and for Windows, Linux and Mac OS X:

~~~
$ conda install hdf5
~~~
{: .bash}

### Geospatial Data Abstraction Library (GDAL)

GDAL is a library for reading/writing raster and vector geospatial data formats.


~~~
$ conda install gdal
~~~
{: .bash}

### matplotlib and basemap 

~~~
$ conda install matplotlib basemap basemap-data-hires
~~~
{: .bash}


### pandas

~~~
$ conda install pandas geopandas pytables
~~~
{: .bash}




### plotly

~~~
$ conda install plotly
~~~
{: .bash}


### Animation ffmpeg

~~~
$ conda install  ffmpeg
~~~
{: .bash}


### pillow

~~~
$ conda install pillow
~~~
{: .bash}


### scipy, scikit-image and scikit-learn

~~~
$ conda install scipy scikit-learn scikit-image
~~~
{: .bash}



### xarray and dask

~~~
$ conda install xarray dask=0.15.2
~~~
{: .bash}



### cartopy, holoviews, datashader and dill

~~~
$ conda install cartopy holoviews datashader dill
~~~
{: .bash}


### ipyleaflet and gmaps

~~~
$ conda install ipyleaflet gmaps
~~~
{: .bash}


### graphviz

~~~
$ conda install graphviz python-graphviz
~~~
{: .bash}
