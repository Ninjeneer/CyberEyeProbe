# Nmap scanner : scan open services on a given server
# and cross the result with CVE database to identify vulnerabilities

import os
from cve import get_cve_for_service

from nmap import scan_server_services

if __name__ == "__main__":
    # Get host from env variable
    host = 'pilot-plus.fr'

    scan_result = scan_server_services(host)

    # TODO parallelize this to improve speed
    for service in scan_result.services:
        cves = get_cve_for_service(service)
