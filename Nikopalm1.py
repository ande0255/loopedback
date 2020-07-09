from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.238.11',
    'username': 'looped',
    'password': 'back'
}

with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)