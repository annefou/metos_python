FROM jupyter/scipy-notebook

MAINTAINER Anne Fouilloux <annefou@geo.uio.no>

# Install requirements for Python 3
ADD environment.yml environment.yml

RUN conda env update -n root -f environment.yml
RUN wget https://zenodo.org/record/995709/files/metos-python-data.tar \
    && tar xvf metos-python-data.tar  && rm -rf metos-python-data.tar
WORKDIR metos-python-data 
