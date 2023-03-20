FROM python:alpine

WORKDIR /app

RUN pip install --upgrade pip
# Install probe dependencies
RUN apk add nmap nmap-scripts

COPY probenmap/requirements.txt .
RUN pip install -r requirements.txt

COPY ./connectivity/dist ./dist
RUN ls -la
RUN pip install ./dist/*.whl
RUN rm -rf dist

COPY ./probenmap .

CMD ["python", "main.py"]