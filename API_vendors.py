#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
from OuiLookup import OuiLookup


import urllib.request as urllib2
import json
import codecs

def MacinfoVendor(mac_address):
    if mac_address == 'unknown': return 'Device/host was up and now down? check!'
    #API base url,you can also use https if you need
    url = "http://macvendors.co/api/"

    request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
    response = urllib2.urlopen( request )
    #Fix: json object must be str, not 'bytes'
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))
    info = (obj['result']['company']+"<br/>")
    try:
        results = OuiLookup().query(mac_address)
        key = list(results[0])[0]
        info2 = results[0][key]
    except KeyError as e:
        print(f"Error: {e}")
        vendor = "UNKNOWN"
    return info2+str(info)




#mac = input('Geef Mac adres: ')
#macinfo = MacinfoVendor(mac)
#print(macinfo)

