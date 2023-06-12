# Probe build
FROM python:3.10-alpine

WORKDIR /app

RUN apk update
RUN apk add perl perl-net-ssleay perl-crypt-ssleay curl
RUN curl -LO https://github.com/sullo/nikto/archive/master.tar.gz && tar -xvf master.tar.gz && cd nikto-master/program && chmod +x nikto.pl
RUN export PATH=~/nikto-master/program:$PATH


RUN pip install --upgrade pip

# COPY ./probenikto/requirements.txt .
# RUN pip install -r requirements.txt

COPY ./connectivity ./connectivity
COPY ./probenikto .

CMD ["python", "main.py"]