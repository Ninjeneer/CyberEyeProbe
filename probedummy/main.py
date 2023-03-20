from dotenv import load_dotenv
load_dotenv()

import time
import os
from math import floor
from connectivity import mongo_saver
from connectivity import mq_queue

from uuid import uuid4

if __name__ == '__main__':

    target = os.getenv('TARGET')

    print('dummy')
    mongo_saver.save_object({
        "context": {
            "timestampStart": floor(time.time_ns() / 1_000_000_000 - 60 * 5), # 5 minutes probe
            "timestampStop": floor(time.time_ns() / 1_000_000_000),
            "probeUid": uuid4().__str__(),
            "probeName": "probe-dummy",
            "target": target
        },
        "result": "Dummy Probe Result"
    })