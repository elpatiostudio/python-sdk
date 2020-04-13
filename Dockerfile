ARG PYTHON_VERSION=3.6-stretch

FROM python:${PYTHON_VERSION}
# FROM python:${PYTHON_VERSION} as builder

ENV PYTHONUNBUFFERED 1

WORKDIR /wheels

RUN pip install -U pip \
   && pip wheel -e git://github.com/elpatiostudio/python-sdk.git@2.0.0.2#egg=wallee


# FROM python:${PYTHON_VERSION}

# ENV PYTHONUNBUFFERED=1

# COPY --from=builder /wheels /wheels
# RUN pip install -U pip \
#         && pip install --no-cache-dir \
#                        'wallee==2.0.0' \
#                        -f /wheels \
#         && rm -rf /wheels