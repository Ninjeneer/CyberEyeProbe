# Nmap Scanner

## Mission

Scan a given server for open services, retrieve their version and try to find associated CVEs

## Required env variables

- HOST [IP / domain name] (target to scan)
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

## Optional env variables

- DEBUG [true / false] (show additional logs)

## Technical stack
- Python 3.10
- Nmap
- AWS SQS