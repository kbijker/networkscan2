from Diepte_scan import scan
from API_vendors import MacinfoVendor
from Subnet_handler import subnet_handler
from Ping_Sweep import ping_sweep

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
    print(live_hosts)





if __name__ == '__main__':
    print("Scanprogramma is uitgevoerd.")


