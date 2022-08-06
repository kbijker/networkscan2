import scapy.all as scapy
import argparse
from API_vendors import MacinfoVendor
from Subnet_handler import subnet_handler

from pathlib import Path
import datetime, shutil

import collections
import glob
import os, ast




def spacies(string):
    l = len(string)
    maxl = 15
    output = ''
    if l == maxl:
        return string
    for i in range(maxl-l):
        output = string + ' '
    return output

def rapport(subnet, info_hosts):
    datetime_object = datetime.datetime.now()
    datum = str(datetime_object)
    network = subnet
    hosts_info = info_hosts
    name = f'{network}_{datum[0:10]}'
    path = os.path.join('c:/', 'networkscan')
    if os.path.isdir(path): print('map bestaat al.')
    else: os.mkdir(path)

    Rapport = path + '/' + name + '.txt'
    with open(Rapport, "w") as f:

       f.write(f'Live hosts in netwerk: {network}, op {datum} gemeten:\n')
       f.write('----------------- -----------------------------------------\n')
       for host_ip, info in hosts_info.items():
          hostadapt = spacies(host_ip)
          print(f'{hostadapt} | mac {info[0]} | fabricant: {info[1]}')
          f.write(f'{hostadapt} | mac {info[0]} | fabricant: {info[1]}\n')




