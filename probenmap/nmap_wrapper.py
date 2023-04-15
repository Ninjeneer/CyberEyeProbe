import subprocess
import xmltodict
import json

from connectivity import model
from nmap_model import Service


def scan_server_services(host: str) -> model.ScanResult:
    """Scan open services on a given server"""
    print("[Nmap Scanner] Scanning open services on host: {}".format(host))
    nmap_output = subprocess.check_output(['nmap', '-sV', host, '-oX', '-'])
    parsed_output = json.loads(json.dumps(xmltodict.parse(nmap_output, attr_prefix="")))

    ports = parsed_output["nmaprun"]['host']['ports']['port']
    nb_open_services = len(ports) if ports else 0
    print("[Nmap Scanner] Scan ended - Found {} open services".format(nb_open_services))

    return model.ScanResult(
        list(map(lambda port: Service.build_from_nmap_result(
            port).__to_dict__(), ports)),
        model.Context(
            parsed_output['nmaprun']['start'],
            parsed_output['nmaprun']['runstats']['finished']['time']
        )
    )