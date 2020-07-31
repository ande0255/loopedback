from device_info import ios_xe1
from ncclient import manager
import xmltodict

netconf_filter = open("filter-ietf-interface.xml").read()

if __name__ == '__man__':
    with manager.connect(host=ios_xe1["address], port=ios_xe1"],
                        username=ios_xe1["username"],
                        password=ios_xe1["password"],
                        hostkey_verify=False) as m:

print("Here are the NETCONF Capabilities")

for capibility in m.server_capabilities:
    print(capability)


netconf_reply = m.get(netconf_filter)

intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["Data"]
intf_config = intf_details["interfaces"]["interface"]
intf_info = intf_details["interfaces-state"]["interface"]

print("")
print("Interface Details:")
print(" Name: {}".format(intf_config["name"]))
print(" Decription: {}".format(intf_config["description"]))
print(" Type: {}".format(intf_config["type"]["text"]))
print(" Mac Address {}".format(intf_info["phy-address"]))
print(" Mac Input: {}".format(intf_info["statistics"]["in-unicast-packets"]))
print(" Mac Output: {}".format(intf_info["statistics"]["out-unicast-packets"]))
