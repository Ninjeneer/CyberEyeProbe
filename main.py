# Nmap scanner : scan open services on a given server
# and cross the result with CVE database to identify vulnerabilities

import os

from nmap import scan_server_services

if __name__ == "__main__":
    # Get host from env variable
    host = 'localhost'

    scan_result = scan_server_services(host)
    print(scan_result.__to_dict__())
