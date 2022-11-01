from typing import List

from object_utils import safe_dict_value

class Service:
    def __init__(self, protocol: str = None, port: int = None, name: str = None, product: str = None, version: str = None, extrainfo: str = None, cves: list = []):
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

        if result['service']:
            if 'name' in result['service']:
                service.name = result['service']['name']
            if 'product' in result['service']:
                service.product = result['service']['product']
            if 'version' in result['service']:
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
            'cves': list(map(lambda cve: {
                'id': safe_dict_value('id', cve),
                'sourceIdentifier': safe_dict_value('sourceIdentifier', cve),
                'published': safe_dict_value('published', cve),
                'vulnStatus': safe_dict_value('vulnStatus', cve),
                'descriptions': self._get_relevant_decription(safe_dict_value('descriptions', cve)),
                'metrics': safe_dict_value('metrics', cve),
            }, self.cves))
        }

    def _get_relevant_decription(self, descriptions: list) -> str:
        if not descriptions:
            return ''

        for description in descriptions:
            if description['lang'] == 'en':
                return description['value']

        return ''


class Context:
    def __init__(self, timestamp_start: int = 0, timestamp_stop: int = 0, probe_uid: str = None) -> None:
        self.timestamp_start = timestamp_start
        self.timestamp_stop = timestamp_stop
        self.probe_uid = probe_uid

    def __to_dict__(self) -> dict:
        return {
            'timestampStart': self.timestamp_start,
            'timestampStop': self.timestamp_stop,
            'probeUid': self.probe_uid
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
