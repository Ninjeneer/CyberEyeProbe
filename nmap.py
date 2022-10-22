import nmap3

from model import Context, ScanResult, Service
nmap = nmap3.Nmap()

def scan_server_services(host: str) -> ScanResult:
    """Scan open services on a given server"""
    print("[Nmap Scanner] Scanning open services on host: {}".format(host))
    nmap_output = nmap.nmap_version_detection(host)

    ip = list(nmap_output.keys())[0]
    ports = nmap_output[ip]['ports']
    nb_open_services = len(ports) if ports else 0
    print("[Nmap Scanner] Scan ended - Found {} open services".format(nb_open_services))

    return ScanResult(
        map(lambda port: Service.build_from_nmap_result(port), nmap_output[ip]['ports']),
        Context(
            nmap_output['stats']['start'],
            nmap_output['runtime']['time']
        )
    )