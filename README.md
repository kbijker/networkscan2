# networkscan2
# This networkscan has two Purposes: 
# 1: Scan for hidden and known devices in a LAN.
# 2. In Depht scan for al kind of host (server, webapplication)  in and out of the LAN (also internet).
# from the main you can start this program and chose for option 1 (Kind of Ping Sweep in a LAN) or option 2 (nmap scan for one host).
# For the ping sweep you can give a known IP-address of a host with subnet (shorthand notation), for example 192.168.2.1/24 (local router). This program will
# automaticly calculate all the possible host in the subnet and try to ARP every host to see its alive or not. if a host is alive than the program will search by three sources 
# so much as possible information about the mac-address. The information will be reported in a textdocument in the map c:/networkscan/*.txt.
