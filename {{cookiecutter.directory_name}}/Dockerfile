FROM ubuntu:18.04
LABEL maintainer="dipy@python.org"


RUN apt-get update && apt-get install -y python-pip git
RUN pip install numpy cython scipy matplotlib h5py nibabel
RUN pip install cvxpy scikit-learn joblib

{% if cookiecutter.dipy_version|lower == "master" %}

RUN git clone https://github.com/dipy/dipy.git && cd dipy && pip install .
ENV DEBIAN_FRONTEND=noninteractive
#RUN pip install dipy==1.1.1

{% else %}

#RUN git clone https://github.com/dipy/dipy.git && cd dipy && pip install .
ENV DEBIAN_FRONTEND=noninteractive
RUN pip install dipy=={{cookiecutter.dipy_version}}

{% endif %}

# move this up?
RUN apt-get update && apt-get install -y python-tk

# make it work under singularity
RUN ldconfig && mkdir -p /N/u /N/home /N/dc2 /N/soft

# https://wiki.ubuntu.com/DashAsBinSh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV PYTHONNOUSERSITE=true