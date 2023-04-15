# Probe build
FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY ./probedummy/requirements.txt .
RUN pip install -r requirements.txt

COPY ./connectivity ./connectivity
COPY ./probedummy .

CMD ["python", "main.py"]