# Nmap Scanner

## Mission

Scan a given server for open services, retrieve their version and try to find associated CVEs

## Required env variables

- PROBE_UID
- HOST [IP / domain name] (target to scan)
- NVD_API_KEY
  
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- AWS_QUEUE_URL
- AWS_BUCKET_NAME

## Optional env variables

- DEBUG [true / false] (show additional logs)

## Technical stack
- Python 3.10
- Nmap
- AWS SQS
- AWS S3