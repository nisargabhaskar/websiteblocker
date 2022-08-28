#change security settings of hosts before execution
#Import libraries
import time
from datetime import datetime as dt
#Windows host file path
hostsPath="C://Windows//System32//drivers//etc//hosts"
redirect="127.0.0.1"
#Add the website you want to block, in this list
websites=[]
n=int(input('enter the no of websites'))
for x in range(n):
websites.append(input('enter the websites '))
websites.append(' ')
s=input('enter the time starts')
s=s.split(sep':')
h=int(s[0])
m=int(s[1])

e=input('enter the end time')
e=e.split(sep=':')
h1=int(e[0])
m1=int(e[1])
while True:
#Duration during which, website blocker will work
    if dt(dt.now().year,dt.now().month,dt.now().day,h,m) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,h1,m1):
        print ("Sorry Not Allowed...")
        with open(hostsPath,'r+') as file:
            content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
        break
    else:
        with open(hostsPath,'r+') as file:
            content = file.readlines()
            file.seek(0)
                for line in content:
                    if not any(site in line for site in websites):
                        file.write(line)
            file.truncate()
        print ("Allowed access!")
    break
