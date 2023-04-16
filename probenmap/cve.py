from sys import stderr
import os

import requests
from nmap_model import Service

api_key = os.getenv('NVD_API_KEY')

def get_cve_for_service(service: Service) -> list:
    """
    Assign CVEs to a given service
    """
    keywords = "{} {}".format(
        service['product'], service['version'] if service['version'] else '')

    # Search for CVEs
    print("[CVE Scanner] Searching for CVEs for service: {}".format(keywords))
    api_call = requests.get(
        url="https://services.nvd.nist.gov/rest/json/cves/2.0",
        params={"keywordSearch": keywords},
        headers={"apiKey": api_key}
    )

    if api_call.status_code != 200:
        print("Error while calling NVD API: {}".format(
            api_call.text))
        return []

    try:
        body = api_call.json()
        vulnerabilites = body['vulnerabilities']

        print("[CVE Scanner] Found {} CVEs for service: {}".format(len(vulnerabilites), keywords))

        # Returns all the 'CVE' entries of vulnerabilities array
        return list(
            map(
                lambda vuln: vuln['cve'],
                filter(
                    lambda vuln: 'cve' in vuln, vulnerabilites
                )
            )
        )
    except requests.JSONDecodeError as e:
        print("Error while decoding JSON response from NVD API: {}".format(
            e))
        return []
