from typing import List


class CVE:
    def __init__(self, ref, link):
        self.ref = ref
        self.link = link

    def __to_dict__(self):
        return {
            "ref": self.ref,
            "link": self.link
        }


class Service:
    def __init__(self, protocol: str = None, port: int = None, name: str = None, product: str = None, version: str = None, extrainfo: str = None, cves: List[CVE] = []):
        self.protocol = protocol
        self.port = port
        self.name = name
        self.product = product
        self.version = version
        self.extrainfo = extrainfo

        self.cves = cves

    @staticmethod
    def build_from_nmap_result(result) -> 'Service':
        service = Service()
        service.protocol = result['protocol']
        service.port = int(result['portid'])
        service.name = result['service']['name']
        service.product = result['service']['product']
        service.version = result['service']['version']
        return service

    def __to_dict__(self) -> dict:
        return {
            'protocol': self.protocol,
            'port': self.port,
            'name': self.name,
            'product': self.product,
            'version': self.version,
            'extrainfo': self.extrainfo,
            'cves': list(map(lambda cve: cve.__to_dict__(), self.cves))
        }


class Context:
    def __init__(self, timestamp_start: int, timestamp_stop: int) -> None:
        self.timestamp_start = timestamp_start
        self.timestamp_stop = timestamp_stop

    def __to_dict__(self) -> dict:
        return {
            'timestamp_start': self.timestamp_start,
            'timestamp_stop': self.timestamp_stop
        }


class ScanResult:
    def __init__(self, services: List[Service], context: Context):
        self.services = services
        self.context = context

    def __to_dict__(self):
        return {
            "services": list(map(lambda service: service.__to_dict__(), self.services)),
            "context": self.context.__to_dict__()
        }
