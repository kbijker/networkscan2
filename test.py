import nmap, json


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
          scan = nm.scan(hosts=ip, arguments='-T4 -p 20-400 -sV -sT -Pn --host-timeout 3600')  # arguments='-T5 -p 1-65535 -sV -sT -Pn --host-timeout 3600'
          print(scan)
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

ip = '192.168.178.73'
nm = nmap.PortScanner()
scan = nm.scan(hosts=ip, arguments='-T4 -sV')  # arguments='-T5 -p 1-65535 -sV -sT -Pn --host-timeout 3600'
print(scan)
#scan = Port(ip).port_scan()