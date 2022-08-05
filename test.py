from scapy.all import *

#host = '192.168.178.11'
#resp = sr1(IP(dst=str(host))/ICMP(),inter=.1,timeout=1,retry=0,verbose=0)
#print(resp)

def test(h):

   ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=h),timeout=2)
   antw = str(ans.__repr__())
   print(antw)
   if 'Other:1' in antw:
       print(f'{h} is alive')
   else: print(f'{h} is not use?')

host = '192.168.178.11'
live = test(host)
#ans.summary( lambda(s,r) : r.sprintf("%IP.src% is alive") )