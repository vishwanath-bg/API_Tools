import requests
import urllib3.exceptions
from requests.auth import HTTPBasicAuth
from collections import defaultdict

list = defaultdict(str)


# API_methods
class api_info:
    def __init__(self, IP, username, password):
        self.IP = IP
        self.username = username
        self.password = password

    def get(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        auth = HTTPBasicAuth(self.username, self.password)
        session = requests.Session()
        session.verify = False

        try:
            # Generates key for particualr device
            self.key = requests.get(f'https://{self.IP}/api/v1/auth', auth=auth, verify=False).json()
            list[ip] += self.key['api_key']

            auth_info = session.get(f"https://{self.IP}/api/v1/system/system-information", auth=(self.key['api_key'], ""))
            dictionary = auth_info.json()
            return dictionary

        except requests.exceptions.ConnectTimeout:
            print(f"{self.IP} Device is not pingable")

        except TypeError:
            print("not able to get information from device")

    def current(self, device):
        try:
            print(f"Current build of {device} :{self.key['software-inventory']['software']['build']}")

        except TypeError:
            print("not able to get information from device")

    def rollback(self, device):
        try:
            print(f"Previous build of {device} :{self.key['rollback-partition-information']['build']}")

        except TypeError:
            print("not able to get information from device")

        except KeyError:
            print("Roll back version not available")

    def machine_ID(self):
        try:
            print(f"Machine ID: {self.key['system-information']['machine-id']}")

        except TypeError:
            print("not able to get information from device")


# Importing device IP's from user file
with open('files/IP_list') as file:
    for line in file:
        temp = (line.strip("\n ")).split(',')
        ip = temp[0]
        username = temp[1]
        password = temp[2]

        # Device Information methods calling from class
        print(f'Device IP: {ip}\nUSERNAME: {username}\nPASSWORD: {password}')
        info = api_info(ip, username, password)
        info.current(ip)
        info.rollback(ip)
        info.machine_ID()
        print("*" * 40)

# if you need api keys just print "list" variable