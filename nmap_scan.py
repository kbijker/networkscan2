import nmap, logging,xml
import json


def osdetect(ip):
  print(f'Portscan op host {ip}:')
  hostScan = nmap.PortScanner()
  try:
    result = hostScan.scan(hosts=ip, arguments='-sS -O -vv -n -T4')
    for k, v in result.get('scan').items():
            if v.get('osmatch'):
                for i in v.get('osmatch'):
                    #console('OSdetect', ip, i.get('name') + '\n')
                    return i.get('name')
            else:
                break
  except (xml.etree.ElementTree.ParseError, nmap.nmap.PortScannerError):
        pass
  except Exception as e:
        #console('OSdetect', ip, 'None\n')
        logging.exception(e)

ip = '192.168.178.143'
print(osdetect(ip))


#Bron: https://www.programcreek.com/python/?code=al0ne%2FVxscan%2FVxscan-master%2Fplugins%2FActiveReconnaissance%2Fosdetect.py

'''
#dicScan = hostScan.scan(hosts=target, arguments='-sV -A -O -T4')

outputScan = json.dumps(dicScan)
print(outputScan)
hostScan.command_line()

ports_info = dicScan['scan'][ip]['tcp']
Open_ports = list(ports_info.keys())
for k, v in ports_info.items():
    print(f'OS-info: open port {k} gescand, {v["product"]} {v["version"]}, extra info: {v["extrainfo"]} ')
'''
