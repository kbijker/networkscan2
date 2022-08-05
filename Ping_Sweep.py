#!/usr/bin/python
from scapy.all import *
import netaddr

#
#Read in file, ping sweep the entitre network, write result to file
#
def scan(ip):
    mac_host ='unknown'
    arp = ARP(pdst=ip)
    # zet eenEther broadcast packet in elkaar
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    for sent, received in result:
        mac_host = received.hwsrc

    return mac_host

def ping_sweep(network, hosts):
    addresses = []

    for i in range(hosts):
        host = network + str(i+1)
        addresses.append(host)
    print(addresses)
    #addresses = ['192.168.178.1', '192.168.178.2', '192.168.178.73', '192.168.178.138', '192.168.178.146', '192.168.178.254']
    Livehosts = []

    for host in addresses:
        print(f'ip = {host}')

        try:

           response, geen = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=host), timeout=2)
           #print(response)
           antw = str(response.__repr__())


           if 'Other:1' in antw:
               print(f'{host} is alive')
               Livehosts.append(host)
           else:
               print(f'{host} is not use?')

        except:
            print(f'{host} is fout ingevoerd?.')
            pass


    return Livehosts



#ping_sweep('192.168.178.', 254)
