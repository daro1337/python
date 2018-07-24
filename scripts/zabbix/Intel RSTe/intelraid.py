#!/usr/bin/env python

import re
import sys
import subprocess

#run IRST CLI and grab output and save to file
log = open("C:\zabbix\check\intelraid.txt", "w")
rstcli = subprocess.Popen([sys.argv[1], '-I', '--comma'], stdout=log , stderr=subprocess.STDOUT)
rstcli.wait()
#log.flush()
log.close()
#set counters
#All volumes counter
count=0
#volumes in good state counter
count2=0
#reading from file - second argument
out = open(sys.argv[2], "r")
#--GET VOLUME INFORMATION--
for line in out:
	if re.match("(.*)Raid Level(.*)", line):
		if re.match("(.*)State: Normal", line):
			#print("OK")
			count2 +=1
		#else:
			#print("PROBLEM")
		count +=1
out.close()
#print(count)
#print(count2)

if count == count2:
# 0 =OK,  1 = PROBLEM
	print("OK Raid Volume detected:", count )
else:
	print("RAID PROBLEM")
