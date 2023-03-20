FROM python:slim

WORKDIR /app

RUN pip install --upgrade pip

COPY probedummy/requirements.txt .
RUN pip install -r requirements.txt

COPY ./connectivity/dist ./dist
RUN ls -la
RUN pip install ./dist/*.whl
RUN rm -rf dist

COPY ./probedummy .

CMD ["python", "main.py"]