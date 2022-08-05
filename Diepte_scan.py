import scapy.all as scapy
import argparse
from API_vendors import MacinfoVendor



def scan(ip):
    arp_req_frame = scapy.ARP(pdst = ip)

    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    client_dict ={}
    host_live = False
    mac_host = ''
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        #result.append(client_dict)
        mac_host = answered_list[i][1].hwsrc
        if answered_list[i][1].hwsrc == None:  host_live = False
        else: host_live = True

    return client_dict, host_live, mac_host

'''
mac = str(macHost)
vendor = 'onbekend'
    try:
        vendor = MacinfoVendor(mac)
    except:
        pass
    #hosts[target] = (mac, vendor)
    print(f'{target} is gedetecteerd in dit netwerk met als mac: {macHost}, fabricant interface: {vendor}')
    print(scan(target))

'''
