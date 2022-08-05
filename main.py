from Diepte_scan import scan
from API_vendors import MacinfoVendor
from Subnet_handler import subnet_handler
from Ping_Sweep import ping_sweep, scan

ans1 = input('Deze scanner gebruiken voor een enkel IP adres (E) of een range (R) ').upper()
if ans1 == 'E':
    host = {}
    print('Dit is een eenmalige scan en wordt niet vastgelegd.')
    target =input('Geef IP-adres op: ')
    scanned_output, live, macHost = scan(target)
    infoMac = MacinfoVendor(macHost)
    print(f'Host {target} heeft een Mac-adres van {macHost}, producent {infoMac}')
    host[target] = scanned_output


if ans1 == 'R':
    print('Ping Sweep')
    ip_address_mask = input('Geef het IP-adres/subnetmask(shorthand-notation), voorbeeld 1.1.1.1/16. ')
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
        # hosts[IP] = (mac, vendor)
        print(f'{ip} is gedetecteerd in dit netwerk met als mac: {macadd}, fabricant interface: {vendor}')





if __name__ == '__main__':
    print("Scanprogramma is uitgevoerd.")


