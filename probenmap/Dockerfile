FROM python:alpine

WORKDIR /app

# Install probe dependencies
RUN apk add nmap nmap-scripts

RUN pip install --upgrade pip

COPY ./probenmap/requirements.txt .
RUN pip install -r requirements.txt

COPY ./connectivity ./connectivity
COPY ./probenmap .

CMD ["python", "-u", "main.py"]