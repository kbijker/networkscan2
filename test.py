import nmap
import xml, logging

def osdetect(ip):
    # sys.stdout.write(Bcolors.RED + "\nOS：\n" + Bcolors.ENDC)
    nm = nmap.PortScanner()
    try:
        result = nm.scan(hosts=ip, arguments='-sS -O -vv -n -T4 -p 80,22,443')
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


ip = '192.168.178.1'
print(osdetect(ip))