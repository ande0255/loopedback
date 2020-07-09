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
tn.write(b"int lo150\n") 
tn.write(b"ip add 1.1.1.150 255.255.255.255\n")
tn.write(b"int vlan 10\n")
tn.write(b"description Automated VLAN\n") 
tn.write(b"ip add 10.10.10.150 255.255.255.0\n")
tn.write(b"no shut\n") 
tn.write(b"end\n")
tn.write(b"wr\n") 
tn.write(b"exit\n")

print(tn.read_all().decode('ascii')) 