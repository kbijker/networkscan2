from Diepte_scan import scan
from API_vendors import MacinfoVendor
from Subnet_handler import subnet_handler
from Ping_Sweep import ping_sweep, scan
from gathering_info import rapport
from GunMacLookup import Udger
from nmap_scan import Port, osdetect

ans1 = input('Deze scanner gebruiken voor een enkel IP adres (E) of een range (R) ').upper()
if ans1 == 'E':
    host_info = {}
    print('Dit is een eenmalige scan en wordt niet vastgelegd.')
    ip =input('Geef IP-adres op: ')
    os_inf = ''

    print(f'nmap searches for OS target {ip}:')
    os_inf= osdetect(ip)
    print(f'OS van {ip} is {os_inf}')
    print('...Voert een portscan....')
    port_inf1 = Port(ip).port_scan()
    print(port_inf1)
    #for port in port_inf:
     #       print(port)



if ans1 == 'R':
    info_hosts = {}
    print('Ping Sweep')
    ip_address_mask = input('Geef een geldig IP-adres/subnetmask(shorthand-notation) uit de LAN , voorbeeld 1.1.1.1/16. ')
    subnet, hosts, subnetlist = subnet_handler(ip_address_mask)
    live_hosts = ping_sweep(subnet, hosts)
    #live_hosts = ping_sweep('192.168.178.', 24)
    print(live_hosts)
    for ip in live_hosts:
        macadd = scan(ip)
        print(f'host {ip} heeft als mac-adres {macadd}.')
        vendor = 'onbekend'
        try:
            vendor = MacinfoVendor(macadd)
        except:
            pass
        if macadd == 'unknown': extra_info = 'mac address niet gevonden!'
        else: extra_info = str(Udger(macadd))
        info_hosts[ip] = (macadd, vendor, extra_info)

        print(f'{ip} is gedetecteerd in dit netwerk met als mac: {macadd}, extra info: {extra_info}')
    rapport(subnet, info_hosts)




if __name__ == '__main__':
    print("Scanprogramma is uitgevoerd.")


