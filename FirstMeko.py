from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.238.11',
    'username': 'looped',
    'password': 'back',
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('sh vlan brief')
print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (21,31):
    print ("Creating VLAN " +str(n))
    config_commands = ['vlan ' + str(n), 'name Miko_Vlan ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)

output = net_connect.send_command('sh vlan brief')
output = net_connect.send_command('sh ip int brief')
output = net_connect.send_command('end')
output = net_connect.send_command('wr')
print (output)
