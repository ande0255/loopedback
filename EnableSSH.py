import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ") 
password = getpass.getpass() 

f = open ('myswitches')

for IP in f:
    IP=IP.strip()
    print ("Configuring Switch with SSH on " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ") 
    tn.write(user.encode('ascii') + b"\n") 
    if password: 
        tn.read_until(b"Password: ") 
        tn.write(password.encode('ascii') + b"\n") 
    tn.write(b"conf t\n")
    tn.write(b"ip domain-name loopedback.com\n")
    tn.write(b"crypto key generate rsa\n")
    tn.write(b"2048\n")
    tn.write(b"\n")
    tn.write(b"ip ssh ver 2\n")
    tn.write(b"line vty 0 15\n")
    tn.write(b"transport input ssh\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    