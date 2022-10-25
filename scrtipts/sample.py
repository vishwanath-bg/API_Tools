# import requests
# import urllib3.exceptions
# from requests.auth import HTTPBasicAuth
# import sys
# import copy
#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# auth = HTTPBasicAuth('admin', 'dana123')
# session = requests.Session()
# session.verify = False
#
# key = requests.get('https://10.96.224.60/api/v1/auth', auth=auth, verify=False).json()
# print(key)
#
# auth_info = session.get(
#         "https://10.96.224.60/api/v1/system/system-information",
#         auth=(key['api_key'], ""))
# # print(auth_info.json())
# dictionary = auth_info.json()
# print(dictionary["system-information"]['machine-id'])

import requests
import urllib3.exceptions
from requests.auth import HTTPBasicAuth
import sys
import copy
class device_information:
        def __init__(self, ips):
                self.ips = ips

#               print(f'temp value : {temp}')
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                auth = HTTPBasicAuth('admindb', 'dana123')
                session = requests.Session()
                session.verify = False
                self.key = requests.get("https://"+self.ips+"/api/v1/auth", auth=auth, verify=False).json()
                print(self.key)
                auth_info = session.get("https://"+self.ips+"/api/v1/system/system-information",auth=(self.key['api_key'], ""))
                self.details = auth_info.json()
                print(f"details:{self.details}\n")

        # def current(self):
        #         print(f"current build :{self.details['software-inventory']['software']['build']}")


# listOfIps = ['10.96.231.123','10.96.231.133','10.96.206.17','10.96.74,149']
# #listOfIps = ['10.96.231.123']
# def Details_of_all_ips(listOfIps):
#         for ip in listOfIps:
#                 info = device_information(ip)
#                 info.current()
#
# Details_of_all_ips(listOfIps)
info = device_information("10.64.57.34")
