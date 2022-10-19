import requests
import urllib3.exceptions
from requests.auth import HTTPBasicAuth
from collections import defaultdict
list = defaultdict(str)


# API_methods
class device_information:
        def __init__(self, build):
                self.build = build

        def current(self, device):
                print(f"current build of {device} :{self.build['software-inventory']['software']['build']}")

        def Rollback(self, device):
                print(f"Previous build of {device} :{self.build['rollback-partition-information']['build']}")


# Importing device IP's from user file
with open('IP_list') as f:
        for ip in f:
                temp = ip.strip("\n ")
                ip = temp
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                auth = HTTPBasicAuth('admindb', 'dana123')
                session = requests.Session()
                session.verify = False
                # Generates key for particualr device
                key = requests.get(f'https://{ip}/api/v1/auth', auth=auth, verify=False).json()
                list[ip] += key['api_key']

                auth_info = session.get(f"https://{ip}/api/v1/system/system-information", auth=(key['api_key'], ""))
                dictionary = auth_info.json()
                info = device_information(dictionary)
                info.current(ip)
                info.Rollback(ip)
                print("*"*40)

# if you need api keys just print "list" variable