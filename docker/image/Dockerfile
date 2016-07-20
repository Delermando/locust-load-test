FROM python:2.7

RUN pip install pip --upgrade locustio \
        pyzmq \
        gevent

RUN mkdir -p /var/local/tests

WORKDIR /var/local/tests