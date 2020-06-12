#!/usr/bin/env python3.8
import wmi, sys, os, requests

def functionA(var):
    if var<=50:
        print ( "OK - - C:\\ Drive Used Space",var,"%")
        sys.exit(0)
    elif 60<=var & var<=79:
        print ( "Warning - C:\\ Drive Used Space",var,"%"  )
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Rundeck-Auth-Token': 'GLZA6ZIBJENbPPvePyrRqpOhW8g7gAE9',
        }
        data = '{"argString":"-servername servername -filesystem redhat "}'
        response = requests.post('http://192.168.1.10:4440/api/16/job/f26a56bf-1974-4f7a-b8f4-37162e52188d/executions', headers=headers, data=data)
        sys.exit(1)
    elif 80<=var & var<=99:
        print ( "CRITICAL  - C:\\ Drive Used Space",var,"%")
        sys.exit(2)
    else:
        print ( "UKNOWN  - C:\\ Drive Used Space",var,"%")
        sys.exit(3)

    print ("Good bye!")

if __name__ == '__main__':
    c = wmi.WMI ()
    var=(int(format(c.Win32_LogicalDisk()[0].Freespace))/int(format(c.Win32_LogicalDisk()[0].Size)))*100
    var=int(var)
    functionA(var)
