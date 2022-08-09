import nmap, logging,xml
import json

class Port(object):
    """docstring for Port"""
    def __init__(self, ip):
        self.state = 'unscan'
        self.ip = ip
        self.report = ''
    def port_scan(self, ):
       host = self.ip
       nm = nmap.PortScanner()
       self.state = 'scanning'
       try:
          nm.scan(hosts=ip, arguments='-T4 -p 20-400 -sV -sT -Pn --host-timeout 3600')  # arguments='-T5 -p 1-65535 -sV -sT -Pn --host-timeout 3600'
          ports = nm[host]['tcp'].keys()
          report_list = []
          for port in ports:
            report = {}
            state = nm[host]['tcp'][port]['state']
            service = nm[host]['tcp'][port]['name']
            product = nm[host]['tcp'][port]['product']
            report['port'] = port
            report['state'] = state
            report['service'] = service
            report['product'] = product
            if state == 'open':
                report_list.append(report)
          print(report_list)
          self.state = 'scanned'
          self.report = json.dumps(report_list)
          return json.dumps(report_list)
       except Exception as e:
         print(e)


def osdetect(ip):
  print(f'Portscan op host {ip}:')
  hostScan = nmap.PortScanner()
  try:
    result = hostScan.scan(hosts=ip, arguments='-sS -O -vv -n -T3')

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



#ip = '192.168.178.1'
#print(osdetect(ip))

#Bron: https://www.programcreek.com/python/?code=vulscanteam%2Fvulscan%2Fvulscan-master%2Fportscan%2Fportscan.py
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
