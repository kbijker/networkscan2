import urllib.request as urllib2
import json
import codecs

OUI_URL = "http://standards-oui.ieee.org/oui.txt"


mac_address = '90:5c:44:f1:f7:36'
url = f"https://www.macvendorlookup.com/api/v2/{mac_address}/"

request = urllib2.Request(url)
response = urllib2.urlopen( request )
print(response)
#reader = codecs.getreader("utf-8")
obj = json.load(response)
print(obj)
#info = (obj['result']['company']+"<br/>")