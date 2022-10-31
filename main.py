# Nmap scanner : scan open services on a given server
# and cross the result with CVE database to identify vulnerabilities

from dotenv import load_dotenv
load_dotenv()

import os
import threading

from cve import get_cve_for_service
from nmap import scan_server_services
from mq_queue import send_message

def assign_cves_to_service(service):
    service.cves = get_cve_for_service(service)

if __name__ == "__main__":
    # Get host from env variable
    host = os.getenv('HOST')

    # Scan open services on host
    scan_result = scan_server_services(host)

    # Run CVE scanner in parallel
    threads = []
    for service in scan_result.services:
        threads.append(threading.Thread(target=assign_cves_to_service, args=(service,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    send_message(service)
