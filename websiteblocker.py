#change security settings of hosts before execution
#Import libraries
import time
from datetime import datetime as dt
#Windows host file path
hostsPath=&quot;C://Windows//System32//drivers//etc//hosts&quot;
redirect=&quot;127.0.0.1&quot;
#Add the website you want to block, in this list
#websites=[&quot;www.youtube.com&quot;,&quot;www.facebook.com&quot;]
websites=[]
n=int(input(&#39;enter the no of websites&#39;))
for x in range(n):
websites.append(input(&#39;enter the websites &#39;))
websites.append(&#39; &#39;)
s=input(&#39;enter the time starts&#39;)
s=s.split(sep=&#39;:&#39;)
h=int(s[0])
m=int(s[1])

e=input(&#39;enter the end time&#39;)
e=e.split(sep=&#39;:&#39;)
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
