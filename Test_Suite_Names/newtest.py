# import requests
# import urllib3.exceptions
# from requests.auth import HTTPBasicAuth
# from collections import defaultdict
# list = defaultdict(str)
#
#
# # API_methods
# class api_info:
#     def __init__(self, IP):
#         self.IP = IP
#
#     def get(self):
#         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#         auth = HTTPBasicAuth('admindb', 'dana123')
#         session = requests.Session()
#         session.verify = False
#
#         # Generates key for particualr device
#         key = requests.get(f'https://{self.IP}/api/v1/auth', auth=auth, verify=False).json()
#         list[ip] += key['api_key']
#
#         auth_info = session.get(f"https://{self.IP}/api/v1/system/system-information", auth=(key['api_key'], ""))
#         dictionary = auth_info.json()
#         return dictionary
#
#
# class device_information:
#         def __init__(self, build):
#                 self.build = build
#
#         def current(self, device):
#                 print(f"current build of {device} :{self.build['software-inventory']['software']['build']}")
#
#         def Rollback(self, device):
#                 print(f"Previous build of {device} :{self.build['rollback-partition-information']['build']}")
#
#
# # Importing device IP's from user file
# with open('IP_list') as f:
#         for ip in f:
#                 temp = ip.strip("\n ")
#                 ip = temp
#                 x = api_info(ip)
#
#                 info = device_information(x.get())
#                 info.current(ip)
#                 info.Rollback(ip)
#                 print("*"*40)
#
# # if you need api keys just print "list" variable

#
import requests
import urllib3.exceptions
from requests.auth import HTTPBasicAuth
from collections import defaultdict

list = defaultdict(str)


# API_methods
class api_info:
    def __init__(self, IP, build):
        self.IP = IP
        self.build = build

    def get(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        auth = HTTPBasicAuth('admindb', 'dana123')
        session = requests.Session()
        session.verify = False

        # Generates key for particualr device
        key = requests.get(f'https://{self.IP}/api/v1/auth', auth=auth, verify=False).json()
        list[ip] += key['api_key']

        auth_info = session.get(f"https://{self.IP}/api/v1/system/system-information", auth=(key['api_key'], ""))
        dictionary = auth_info.json()
        return dictionary

    def current(self, device):
        print(f"current build of {device} :{self.build['software-inventory']['software']['build']}")

    def Rollback(self, device):
        print(f"Previous build of {device} :{self.build['rollback-partition-information']['build']}")


# Importing device IP's from user file
with open('IP_list') as f:
    for ip in f:
        temp = ip.strip("\n ")
        ip = temp
        x = api_info(ip, 0)
        info = api_info(ip, x.get())
        info.current(ip)
        info.Rollback(ip)
        print("*" * 40)

# if you need api keys just print "list" variable