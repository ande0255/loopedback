from device_info import ios_xe1
from ncclient import manager

if __name__ == '__man__':
    with manager.connect(host=ios_xe1["address], port=ios_xe1"],
                        username=ios_xe1["username"],
                        password=ios_xe1["password"],
                        hostkey_verify=False) as m:

print("Here are the NETCONF Capabilities")
for capibility in m.server_capabilities:
    print(capability)