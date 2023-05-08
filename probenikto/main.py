import os
import niktowrapper

def run_probe():

    target = os.getenv('TARGET')

    if target is None:
        raise Exception("Target not defined")

    print('[Nikto] Targeting {}...'.format(target))
    nikto_result = niktowrapper.run_nikto_on_target(target)