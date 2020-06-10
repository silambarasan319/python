
root@ubuntu:/usr/lib/nagios/plugins# cat usedspace.py
#!/usr/bin/python
import os, sys
import requests
used_space=os.popen("df -h / | grep -v Filesystem | awk '{print $5}'| sed 's/%//g'").readline().strip()
used_space=int(used_space)

if used_space<=59:
   print ("OK - %s of disk space used." % used_space)
   print (used_space)
   sys.exit(0)
elif 60<=used_space & used_space<=79:
   print (used_space)
   print ("WARNING - %s of disk space used." % used_space)
   sys.exit(1)
elif 80<=used_space & used_space<=95:
   headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-Rundeck-Auth-Token': '8h7eFvQ1Nb5JrhulUdYrHvAKzwWw18gp',
   }
   data = '{"argString":"-servername servername -filesystem redhat "}'
   response = requests.post('http://192.168.1.10:4440/api/16/job/2ed8d8c9-3f46-46d3-ba5f-e71d3211a40c/executions', headers=headers, data=data)

   print ("CRITICAL - %s of disk space used." % used_space)
#   print (used_space)
   sys.exit(2)
else:
   print ("UKNOWN - %s of disk space used." % used_space)
   print (used_space)
   sys.exit(3)


print ("Good bye!")
