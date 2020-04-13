FROM python:3.6-slim-stretch

# El Patio Wallee install
RUN apt-get -y update \
&& apt-get -y install git \
&& git clone --branch 2.0.0.1 https://github.com/elpatiostudio/python-sdk.git \
&& cd ./python-sdk \
&& python ./setup.py build \
&& python ./setup.py install \
&& cd .. \
&& rm -rf python-sdk