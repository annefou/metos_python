---
title: "Most common Data Formats"
teaching: 0
exercises: 0
questions:
- "What are the most common data formats in the Ocean, Weather and Climate Sciences?"
- "What are the most common python packages to read/write netCDF, HDF, GRIB and BUFR data files?"
objectives:
- "Learn to recognize the most common data formats in the ocean, weather and climate sciences."
- "Learn to open, read and write netCDF, HDF, GRIB and BUFR files"
keypoints:
- "netCDF, HDF, GRIB and BUFR."
---

In this lesson we will first review the most common data formats used in meteorology and oceanography. Then we will learn how to recognize data coded in netCDF, HDF, GRIB and BUFR formats. Finally, we will learn to read and write files coded in these formats in python. 

### netCDF

[NetCDF](http://www.unidata.ucar.edu/software/netcdf/docs/netcdf_introduction.html) (network Common Data Form) is a machine-independent, self-describing, binary data format standard for exchanging scientific data. The project homepage is hosted by the Unidata program at the University Corporation for Atmospheric Research ([UCAR](http://www.unidata.ucar.edu)). 

#### self-describing?

This means that there is a header which describes the layout of the rest of the file, in particular the data arrays, as well as arbitrary file metadata in the form of name/value attributes.

#### machine-independent?

Issues such as endianness being addressed in the software libraries. 

#### CF conventions?

netCDF format is very flexible and to simplify developments of tools and speed-up netCDF data processing, metadata standards for netCDF files have been created. 
The most common in our discipline is the [Climate and Forecast metadata standard](http://cfconventions.org/), also called CF conventions.


The CF conventions have been adopted by the Program for Climate Model Diagnosis and Intercomparison ([PCMDI](http://www-pcmdi.llnl.gov/)), the Earth System Modeling Framework ([ESMF](https://www.earthsystemcog.org/projects/esmf/)), [NCAR](https://ncar.ucar.edu/), and various EU and international projects. 

#### netCDF3 versus netCDF4?

#### Check a netCDF file (ncdump)?

#### netCDF and python?

netcdf4 python package.

##### Create a netCDF file

##### Read a netCDF file

### HDF

Hierarchical Data Format ([HDF](https://support.hdfgroup.org/)) is a data file format designed by the National Center for Supercomputing Applications ([NCSA](http://www.ncsa.illinois.edu/)).

It is now developed and maintained by the [HDF group](https://www.hdfgroup.org/).

Hierarchical Data Format, commonly abbreviated HDF, HDF4, or HDF5, is a library and multi-object file format for the transfer of graphical and numerical data between computers. 

HDF supports several different data models, including multidimensional arrays, 
[raster images](https://en.wikipedia.org/wiki/Raster_graphics), and tables. 
Each defines a specific aggregate data type and provides an API for reading, writing, and organising the data and metadata. New data models can be added by the HDF developers or users. 

HDF is self-describing, allowing an application to interpret the structure and contents of a file without any outside information. One HDF file can hold a mixture of related objects, which can be accessed as a group or as individual objects.

##### Create an HDF file

##### Read an HDF file

### WMO Binary data exchange formats: GRIB and BUFR

WMO GRIB and BUFR data formats are Table Driven Code Forms which means you need the corresponding "table" to decode GRIB or BUFR data. 

These two formats have been widely adopted for the distribution of meteorological satellite products, especially those processed to level 2 or beyond. 
They are described in the Operational Codes and Manual on Codes. By packing information into the BUFR or GRIB code, data records can be made more compact than many other formats, resulting in faster computer-to-computer transmissions. 

The formats can equally well serve as a data storage formats, generating the same efficiencies relative to information storage and retrieval devices.

Software for encoding and decoding data in the BUFR and GRIB formats is freely available for download from the [ECMWF software](https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home).

#### BUFR

The WMO Binary Universal Form for the Representation of meteorological data (BUFR) is a binary code designed to represent any meteorological dataset employing a continuous binary stream. It has been designed to achieve efficient exchange and storage of meteorological and oceanographic data. It is self describing, table driven and very flexible data representation system, especially for huge volumes of data.

##### Read a BUFR file

##### Write a BUFR file

#### GRIB 

Similarly, another widely used bit-oriented data exchange scheme is the WMO GRIddedBinary (GRIB) format. GRIB is an efficient vehicle for transmitting large volumes of gridded data to automated centers over high-speed telecommunication lines, using modern protocols. An updated version of GRIB, commonly abbreviated to GRIB-2, is currently being introduced and is most relevant for use with satellite data.

##### Read a GRIB file

##### Write a GRIB file

