from scapy.all import *

#host = '192.168.178.11'
#resp = sr1(IP(dst=str(host))/ICMP(),inter=.1,timeout=1,retry=0,verbose=0)
#print(resp)

def scan(ip):
   arp = ARP(pdst=ip)
   # zet eenEther broadcast packet in elkaar
   # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
   ether = Ether(dst="ff:ff:ff:ff:ff:ff")
   # stack them
   packet = ether / arp

   result = srp(packet, timeout=3, verbose=0)[0]

   for sent, received in result:

      mac = received.hwsrc
   return mac
def test(h):

   ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=h),timeout=2)
   antw = str(ans.__repr__())
   print(antw)
   if 'Other:1' in antw:
       print(f'{h} is alive')
   else: print(f'{h} is not use?')

host = '192.168.178.1'
live = test(host)
host1 = '192.168.178.73/24'
mac= scan(host1)
print(mac)


#ans.summary( lambda(s,r) : r.sprintf("%IP.src% is alive") )