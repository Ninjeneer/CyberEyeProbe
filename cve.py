from sys import stderr
import nvdlib
import os

from requests import JSONDecodeError
from model import Service

def _filter_cve_results(cve_results: list) -> list:
    return filter(lambda entry: entry['cve']['data_type'] == 'CVE', cve_results)

def get_cve_for_service(service: Service) -> None:
    """
    Assign CVEs to a given service
    """
    keywords = "{} {}".format(service.product, service.version if service.version else '')

    # Search for CVEs
    cves = []
    try:
        cves = nvdlib.searchCVE(keyword=keywords)
    except JSONDecodeError as jsonError:
        if os.environ.get('DEV'):
            print(jsonError, file=stderr)

        print("[Error]: failed to search for CVE with keyword {}".format(keywords))
    
    service.cves = _filter_cve_results(cves)
