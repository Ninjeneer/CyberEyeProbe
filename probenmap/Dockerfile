# Connectivity Build
FROM python:3.10-alpine as connectivity-builder

WORKDIR /tmp
RUN apk add make
RUN pip install --upgrade pip

COPY ./connectivity .
RUN make build



FROM python:alpine

WORKDIR /app

RUN pip install --upgrade pip
# Install probe dependencies
RUN apk add nmap nmap-scripts

COPY probenmap/requirements.txt .
RUN pip install -r requirements.txt

COPY --from=connectivity-builder /tmp/dist ./dist
RUN pip install ./dist/*.whl
RUN rm -rf dist

COPY ./probenmap .

CMD ["python", "main.py"]