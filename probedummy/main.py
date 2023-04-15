from uuid import uuid4
from connectivity import supabase
from connectivity import mq_queue
from math import floor
import os
import time
from dotenv import load_dotenv
load_dotenv()


def run_probe():

    target = os.getenv('TARGET')
    if target is None:
        raise Exception('Target is not defined !')

    supabase.set_probe_as_running()

    mq_queue.send_message({
        "context": {
            # 5 minutes probe
            "timestampStart": floor(time.time_ns() / 1_000_000_000 - 60 * 5),
            "timestampStop": floor(time.time_ns() / 1_000_000_000),
            "probeUid": uuid4().__str__(),
            "probeName": "probe-dummy",
            "target": target
        },
        "result": "Dummy Probe Result"
    })


if __name__ == "__main__":
    run_probe()
