FROM python:alpine

WORKDIR /app

# Install probe dependencies
RUN apk add nmap nmap-scripts

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "main.py"]