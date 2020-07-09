import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.238.111', 'looped', 'back')
iosvl2.open()

print ('Accessing 192.168.238.111')
iosvl2.load_merge_candidate(filename='aclauto1.cfg')
iosvl2.commit_config()
iosvl2.close()