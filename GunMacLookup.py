import requests
from bs4 import BeautifulSoup


mac = '90:5c:44:f1:f7:36'

#URL = "https://udger.com/resources/mac-address-vendor-lookup?macaddress=00%3A01%3A02%3A01%3A02%3A03"

def Udger(mac):
    URL = f"https://udger.com/resources/mac-address-vendor-lookup?macaddress={mac}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(lambda tag: tag.name=='table')
    info_termen = []
    vendorinfo = []
    try:
       for res in results:
          tekst = str(res).split()
          print(tekst)
          for element in tekst:
             if 'vendor' in element and 'name' in element or 'Country' in element:
                vendorinfo.append(element)
                print(element)
             elif 'code' in element:
                vendorinfo.append(element)
                print(element)

       #print('vendorinfo:',vendorinfo)
       html_shit = ['</b>','</td>','<td>','</tr>','<tr>','</a>', '<b>', '<a>', 'Country']

       for term in vendorinfo:
          t2 = term
          for code in html_shit:
             t1 = t2.replace(code,'')
             t2 = t1
          info_termen.append(t2)
    except:
        pass
    return info_termen