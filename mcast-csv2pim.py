#!/usr/bin/python
with open('mcast-groups.csv', 'r') as f:
        data=f.readlines()
        for line in data:
                entries = line.split(';')
                entries[2]=entries[2].rstrip('\n')
                print 'ipv4 access-list ' + entries[2]
                print '10 permit ipv4 host ' + entries[1] + ' any'
                print 'router igmp vrf <VRF> interface Loopback1 static-group '+ entries[1]
                print 'ssm map static ' + entries[0] + ' ' + entries[2]

