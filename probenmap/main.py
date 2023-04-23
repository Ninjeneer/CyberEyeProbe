# Nmap scanner : scan open services on a given server
# and cross the result with CVE database to identify vulnerabilities
import dotenv
dotenv.load_dotenv()

import os
import threading

from cve import get_cve_for_service
from nmap_wrapper import scan_server_services
from connectivity import mq_queue, supabase

def assign_cves_to_service(service):
    if ('version' in service and service['version'] is not None and service['version'] != ''):
        service['cves'] = get_cve_for_service(service)

def run_probe():
    # Get host from env variable
    host = os.getenv('TARGET')

    print("Targeting {}...".format(host))

    if host is None:
        raise Exception('Target is not defined !')
    
    supabase.set_probe_as_running()
    print("Probe set as running")

    # Scan open services on host
    print("Scaning services")
    scan_result = scan_server_services(host)
    print('Services scanned')
    scan_result.context.probe_id = os.getenv('PROBE_ID')
    scan_result.context.probe_name = 'probe-nmap'
    scan_result.context.target = host

    # Run CVE scanner in parallel
    if len(scan_result.result) > 0:
        print("Triggering CVE DB")
        threads = []
        for service in scan_result.result:
            threads.append(threading.Thread(target=assign_cves_to_service, args=(service,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    mq_queue.send_message(scan_result.__to_dict__())

if __name__ == "__main__":
    run_probe()
