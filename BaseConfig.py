from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.238.11',
    'username': 'looped',
    'password': 'back'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.238.22',
    'username': 'looped',
    'password': 'back'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.238.33',
    'username': 'looped',
    'password': 'back'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.238.44',
    'username': 'looped',
    'password': 'back'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.238.55',
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

with open('iosv_l2_lan') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)