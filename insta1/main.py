from utils import IgUtils
from os import system
from colorama import init
from requests import Session
from time import sleep

request = Session()
init(autoreset=True)
system('cls')
xmid = IgUtils.__xmid__()
csrftoken = IgUtils.__csrf__()
uuid4 = IgUtils.doUUID4()
deviceid = IgUtils.__deviceid__()


username = input("\n Username >>> ")
password = input("\n Password >>> ")

print("logging in ...")
sleep(2)
system('cls')

url = "https://i.instagram.com/api/v1/accounts/login/"

payload = f"uuid={str(uuid4)}&password={password}&username={username}&device_id={str(deviceid)}&from_req=false&_csrftoken=missing&login_attempt_countn=0"

headers = {
    "cookie": f"mid={str(xmid)}; csrftoken={str(csrftoken)};",
    "User-Agent": "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "i.instagram.com",
    "Connection": "keep-alive"
}

response = request.post(url, data=payload, headers=headers)

if response.json()['status'] != "ok" or not response.json()['logged_in_user']['pk']:
    print(response.json()['message'])
    raise SystemExit

print(f"Sessionid >>> {str(response.cookies['sessionid'])}")