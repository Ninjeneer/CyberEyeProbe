# Nmap Scanner

## Mission

Scan a given server for open services, retrieve their version and try to find associated CVEs

## Required env variables

- PROBE_ID
- TARGET [IP / domain name] (target to scan)
- NVD_API_KEY
  
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- AWS_QUEUE_URL
- AWS_QUEUE_RESPONSE_URL

## Optional env variables

- DEV [true / false] (load .env file)

## Technical stack
- Python 3.10
- Nmap
- AWS SQS
- AWS S3