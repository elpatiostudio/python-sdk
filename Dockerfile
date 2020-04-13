FROM python:3.6-stretch

# El Patio Wallee install
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -e git://github.com/elpatiostudio/python-sdk.git@2.0.0.2#egg=wallee