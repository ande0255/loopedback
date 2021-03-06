import getpass
import telnetlib

HOST = "192.168.238.150" 
user = input("Enter your remote account: ") 
password = getpass.getpass() 

tn = telnetlib.Telnet(HOST) 

tn.read_until(b"Username: ") 
tn.write(user.encode('ascii') + b"\n") 
if password: 
    tn.read_until(b"Password: ") 
    tn.write(password.encode('ascii') + b"\n") 

tn.write(b"enable\n")  
tn.write(b"loopedback\n") 
tn.write(b"conf t\n")  

for n in range (2,10):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Auto_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"wr\n") 
tn.write(b"exit\n")

print(tn.read_all().decode('ascii')) 