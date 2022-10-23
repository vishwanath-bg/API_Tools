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

    def get(self, username, password):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        auth = HTTPBasicAuth(username, password)
        session = requests.Session()
        session.verify = False

        try:
            # Generates key for particualr device
            key = requests.get(f'https://{self.IP}/api/v1/auth', auth=auth, verify=False).json()
            list[ip] += key['api_key']

            auth_info = session.get(f"https://{self.IP}/api/v1/system/system-information", auth=(key['api_key'], ""))
            dictionary = auth_info.json()
            return dictionary

        except requests.exceptions.ConnectTimeout:
            print(f"{self.IP} Device is not pingable")

        except TypeError:
            print("not able to get information from device")

    def current(self, device):
        try:
            print(f"Current build of {device} :{self.build['software-inventory']['software']['build']}")

        except TypeError:
            print("not able to get information from device")

    def rollback(self, device):
        try:
            print(f"Previous build of {device} :{self.build['rollback-partition-information']['build']}")

        except TypeError:
            print("not able to get information from device")

        except KeyError:
            print("Roll back version not available")

    def machine_ID(self):
        try:
            print(f"Machine ID: {self.build['system-information']['machine-id']}")

        except TypeError:
            print("not able to get information from device")


# Importing device IP's from user file
with open('files/IP_list') as file:
    for line in file:
        temp = (line.strip("\n ")).split(',')
        ip = temp[0]
        username = temp[1]
        password = temp[2]
        print(f'Device IP: {ip}\nUSERNAME: {username}\nPASSWORD: {password}')
        x = api_info(ip, '')
        info = api_info(ip, x.get(username, password))
        info.current(ip)
        info.rollback(ip)
        info.machine_ID()
        print("*" * 40)

# if you need api keys just print "list" variable