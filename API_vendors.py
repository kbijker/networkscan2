#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address


import urllib.request as urllib2
import json
import codecs

def MacinfoVendor(mac_address):
    #API base url,you can also use https if you need
    url = "http://macvendors.co/api/"

    request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
    response = urllib2.urlopen( request )
    #Fix: json object must be str, not 'bytes'
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))
    info = (obj['result']['company']+"<br/>")
    #Print company name
    return str(info)


#mac = input('Geef Mac adres: ')
#macinfo = MacinfoVendor(mac)
#print(macinfo)

