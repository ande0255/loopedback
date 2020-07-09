import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.238.11', 'looped', 'back')
iosvl2.open()

print ('Accessing 192.168.238.11')
iosvl2.load_merge_candidate(filename='aclauto1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No changes required.')
    iosvl2.discard_config()

iosvl2.close()