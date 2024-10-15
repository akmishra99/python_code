#!/usr/bin/python3
import os
#following program pings to ip address and displays results , if ping was successful then prints "SUCCESS"
#else dusplays Failure on terminal  below is output of running this program
"""akmishra@windows11:~$ ./test_os.py
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
64 bytes from 192.168.1.1: icmp_seq=1 ttl=63 time=1.16 ms
64 bytes from 192.168.1.1: icmp_seq=2 ttl=63 time=1.56 ms
64 bytes from 192.168.1.1: icmp_seq=3 ttl=63 time=0.898 ms
64 bytes from 192.168.1.1: icmp_seq=4 ttl=63 time=1.55 ms
64 bytes from 192.168.1.1: icmp_seq=5 ttl=63 time=1.63 ms

--- 192.168.1.1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 0.898/1.358/1.631/0.284 ms
192.168.1.1 SUCCESS
PING 192.168.1.2 (192.168.1.2) 56(84) bytes of data.
From 192.168.1.40 icmp_seq=3 Destination Host Unreachable

--- 192.168.1.2 ping statistics ---
5 packets transmitted, 0 received, +1 errors, 100% packet loss, time 4130ms

192.168.1.2 Failure
akmishra@windows11:~$
"""
def execute_ping(ip_address):

    iret_val = os.system("/usr/bin/ping -c  5 " + ip_address)
    return iret_val 

if __name__=='__main__':
    ip_address_list = [ "192.168.1.1", "192.168.1.2" ]
    for i in ip_address_list:
        ret_val = execute_ping(i)
        if ( ret_val == 0 ):
            print (i,"SUCCESS")
        else:
            print (i,"Failure")

