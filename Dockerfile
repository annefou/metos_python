FROM andrewosh/binder-base

MAINTAINER Anne Fouilloux <annefou@geo.uio.no>

USER root

# Add dependency
RUN apt-get update && apt-get install -y wget tar

USER main

# Install requirements for Python 3
ADD environment.yml environment.yml

RUN /home/main/anaconda/envs/python3/bin/conda env create -f environment.yml
RUN wget https://zenodo.org/record/995709/files/metos-python-data.tar &&
tar xvf metos-python-data.tar && cd metos-python-data 
