import nmap, logging,xml
import json


def port_scan(ip):

       nm = nmap.PortScanner()

       try:
          nm.scan(hosts=ip, arguments='-T4 -p 20-500 -sV -sT -Pn --host-timeout 3600')  # arguments='-T5 -p 1-65535 -sV -sT -Pn --host-timeout 3600'
          ports = nm[ip]['tcp'].keys()
          report_list = []

          for port in ports:
            report = {}
            state = nm[ip]['tcp'][port]['state']
            service = nm[ip]['tcp'][port]['name']
            product = nm[ip]['tcp'][port]['product']
            report[port] = (state, service, product)

            report_list.append(report)

          return report_list
       except Exception as e:
         print(e)


def osdetect(ip):

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



#ip = '192.168.178.73'
#print(port_scan(ip))

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
