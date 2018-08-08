#!/usr/bin/env python
import re
import io
import io
import sys
from ftplib import FTP

#vars
#global ftp
host = "ftp.example.co"
port = "21"
username = "login@example.com"
passwd = "password"

# connection function
def ftpconn():
    global ftp
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(username, passwd)

#for ovh servers
def ovhftp():
    ftpconn()
    ovhstats = ftp.getwelcome()
    print(ovhstats)
    ftp.quit()

#for servers supported site quota
def otherftp():
    ftpconn()
    quota = ftp.sendcmd('site quota')
    for row in quota.split('\n'):
        if re.match("(.*)[U|u]ploaded(.*)[0-9]", row):
            match = row
            x = [ float(s) for s in re.findall(r'-?\d+\.?\d*', match)]
            calc = (x[0] / x[1]) * 100
            if calc > 85:
                print("FTP Quota is more than 85% =>", calc)
            else:
                print("FTP usage in bounds", calc)
    ftp.quit()

def main():
    try:
        if re.match("(.*)ovh", host):
           ovhftp()
        else:
            otherftp()
    except Exception as e:
        print(e)
        sys.exit(100)

if __name__ == "__main__":
    main()


#OVH version TODO
#OK. Current directory is /
#92788769 Kbytes used (17%) - authorized: 524185600 Kb
#Logged in to ftpback-rbx7-xxx.ovh.net.
