import requests
import urllib3.exceptions
from requests.auth import HTTPBasicAuth
import sys
import copy

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
auth = HTTPBasicAuth('admin', 'dana123')
session = requests.Session()
session.verify = False

key = requests.get('https://10.96.224.60/api/v1/auth', auth=auth, verify=False).json()
print(key)

auth_info = session.get(
        "https://10.96.224.60/api/v1/system/system-information",
        auth=(key['api_key'], ""))
# print(auth_info.json())
dictionary = auth_info.json()
print(dictionary["system-information"]['machine-id'])

