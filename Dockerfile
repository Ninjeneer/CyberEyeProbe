FROM python:alpine

# Install probe dependencies
RUN apk add nmap
RUN apk add nmap-scripts

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]