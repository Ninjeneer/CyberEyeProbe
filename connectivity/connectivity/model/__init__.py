class Context:
    def __init__(self,
                 timestamp_start: int = 0,
                 timestamp_stop: int = 0,
                 probe_id: str = None,
                 probe_name: str = "unknown_probe",
                 target: str = "unknown_target") -> None:
        self.timestamp_start = timestamp_start
        self.timestamp_stop = timestamp_stop
        self.probe_id = probe_id
        self.probe_name = probe_name
        self.target = target

    def __to_dict__(self) -> dict:
        return {
            'timestampStart': self.timestamp_start,
            'timestampStop': self.timestamp_stop,
            'probeUid': self.probe_id,
            "probeName": self.probe_name,
            "target": self.target
        }
    
class ScanResult:
    def __init__(self, result, context: Context):
        self.result = result
        self.context = context

    def __to_dict__(self):
        return {
            "result": self.result,
            "context": self.context.__to_dict__()
        }