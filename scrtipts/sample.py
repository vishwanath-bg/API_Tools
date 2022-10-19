import requests
import urllib3.exceptions
from requests.auth import HTTPBasicAuth
import sys
import copy

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
auth = HTTPBasicAuth('admindb', 'dana123')
session = requests.Session()
session.verify = False

key = requests.get('https://10.96.206.17/api/v1/auth', auth=auth, verify=False).json()
print(key)

auth_info = session.get(
        "https://10.96.206.17/api/v1/system/system-information",
        auth=(key['api_key'], ""))
print(auth_info.json())
dictionary = auth_info.json()

class device_information:
        def __init__(self, build):
                self.build = build

        def current(self):
                print(f"current build :{self.build['software-inventory']['software']['build']}")

        # def (self):
        #         print(f"current build :{self.build['software-inventory']}")

info = device_information(dictionary)
info.current()