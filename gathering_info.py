import scapy.all as scapy
import argparse
from API_vendors import MacinfoVendor
from Subnet_handler import subnet_handler
from xlutils.copy import copy
from xlrd import open_workbook
from pathlib import Path
import datetime, shutil
import xlsxwriter
import csv
import collections
import pandas as pd
from openpyxl import load_workbook
#keep_default_na=False, na_filter= False,
import glob
import os, ast
import xlwt
from xlwt import Workbook



def spacies(string):
    l = len(string)
    maxl = 15
    output = ''
    if l == maxl:
        return string
    for i in range(maxl-l):
        output = string + ' '
    return output

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    options = parser.parse_args()

    #Check for errors i.e if the user does not specify the target IP Address
    #Quit the program if the argument is missing
    #While quitting also display an error message
    if not options.target:
        #Code to handle if interface is not specified
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options

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

ans1 = input('Deze scanner gebruiken voor een enkel IP adres (E) of een range (R) ').upper()
hosts = {}




#options = get_args()
#scanned_output = scan(options.target)

if ans1 == "R":
    ip_address_mask = input('Geef het IP-adres/subnetmask(shorthand-notation), voorbeeld 1.1.1.1/16. ')
    subnet, hosts, subnetlist = subnet_handler(ip_address_mask)
    result_IP_Mac =[]

    for i in range(1,hosts):

           host_id = i
           IP = subnet + str(host_id)
           print(f'Bezig met scannen van {IP}:')
           scanned_output, live, macHost = scan(IP)
           if live:
              result_IP_Mac.append(scanned_output)
              mac = str(macHost)
              vendor ='onbekend'
              try:
                 vendor = MacinfoVendor(mac)
              except:
                 pass
              #hosts[IP] = (mac, vendor)
              print(f'{IP} is gedetecteerd in dit netwerk met als mac: {macHost}, fabricant interface: {vendor}')
           else: print(f'{IP} is niet aanwezig in dit netwerk.')
    datetime_object = datetime.datetime.now()
    datum = str(datetime_object)
    network =network_id.replace('.','o')
    name = f'{network}_{datum[0:10]}'
    path = os.path.join('c:/', 'networkscan')
    if os.path.isdir(path): print('map bestaat al.')
    else: os.mkdir(path)

    Rapport = path + '/' + name + '.txt'
    with open(Rapport, "w") as f:
       print(f'Live hosts in netwerk: {network_id}, op {datum} gemeten:')
       print('----------------- -----------------------------------------')
       f.write(f'Live hosts in netwerk: {network_id}, op {datum} gemeten:\n')
       f.write('----------------- -----------------------------------------\n')
       for host_ip, info in hosts.items():
          hostadapt = spacies(host_ip)
          print(f'{hostadapt} | {info[0]} | fabricant: {info[1]}')
          f.write(f'{hostadapt} | {info[0]} | fabricant: {info[1]}\n')




