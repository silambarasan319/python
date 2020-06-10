#!/usr/bin/env python3.8
import wmi
import sys
import requests

c = wmi.WMI ()
var=(int(format(c.Win32_LogicalDisk()[0].Freespace))/int(format(c.Win32_LogicalDisk()[0].Size)))*100
var=int(var)

if var<=50:
   print ("1 - Got a true expression value")
   print (var)
   exit(0)
elif 60<=var & var<=79:
   print ("2 - Got a true expression value")
   headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Rundeck-Auth-Token': '8h7eFvQ1Nb5JrhulUdYrHvAKzwWw18gp',
   }
   data = '{"argString":"-servername servername -filesystem redhat "}'
   response = requests.post('http://192.168.1.10:4440/api/16/job/2ed8d8c9-3f46-46d3-ba5f-e71d3211a40c/executions', headers=headers, data=data)
   print (var)
   exit(1)
elif 80<=var & var<=95:
   print ("3 - Got a true expression value")
   print (var)
   exit(2)
else:
   print ("4 - Got a false expression value")
   print (var)
   exit(3)

print ("Good bye!")


