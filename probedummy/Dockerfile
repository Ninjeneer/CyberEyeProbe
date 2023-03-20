# Connectivity Build
FROM python:3.10-alpine as connectivity-builder

WORKDIR /tmp
RUN apk add make
RUN pip install --upgrade pip

COPY ./connectivity .
RUN make build



# Probe build
FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY probedummy/requirements.txt .
RUN pip install -r requirements.txt

COPY --from=connectivity-builder /tmp/dist ./dist
RUN pip install ./dist/*.whl
RUN rm -rf dist

COPY ./probedummy .

CMD ["python", "main.py"]