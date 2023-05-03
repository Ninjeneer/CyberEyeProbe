import subprocess
import xmltodict
import json

from connectivity import model
from nmap_model import Service


def scan_server_services(host: str) -> model.ScanResult:
    """Scan open services on a given server"""
    print("[Nmap Scanner] Scanning open services on host: {}".format(host))
    try:
        nmap_output = subprocess.check_output(
            ['nmap', '-Pn', '-sV', host, '-oX', '-'])
    except:
        print("error")
    print("[Nmap Scanner] Result provided, parsing...")
    parsed_output = json.loads(json.dumps(
        xmltodict.parse(nmap_output, attr_prefix="")))
    print("[Nmap Scanner] Result parsed")


    if 'host' not in parsed_output["nmaprun"]:
        print("[Nmap Scanner] No result")
        return model.ScanResult(
            [],
            model.Context(
                parsed_output['nmaprun']['start'],
                parsed_output['nmaprun']['runstats']['finished']['time']
            )
        )

    ports = parsed_output["nmaprun"]['host']['ports']['port']
    nb_open_services = len(ports) if ports else 0
    print("[Nmap Scanner] Scan ended - Found {} open services".format(nb_open_services))

    # When there is a single port open, Nmap returns a single object instead of a list
    # so we need to check the type of the ports
    portsResult: list = []
    if isinstance(ports, list):
        portsResult = list(map(lambda port: Service.build_from_nmap_result(port).__to_dict__(), ports))
    else:
        portsResult = [Service.build_from_nmap_result(ports).__to_dict__()]

    return model.ScanResult(
        portsResult,
        model.Context(
            parsed_output['nmaprun']['start'],
            parsed_output['nmaprun']['runstats']['finished']['time']
        )
    )
