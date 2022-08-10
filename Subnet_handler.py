from API_vendors import MacinfoVendor

#Class om subnet op te breken in aantal hosts die gescand moeten worden.
class Subnet:
    def __init__(self, a, b, c, d, sm):
        self.o1= int(a)
        self.o2= int(b)
        self.o3= int(c)
        self.o4= int(d)
        self.sm = sm

    def __repr__(self):
        return f'Subnet gegevens: {self.o1}.{self.o2}.{self.o3}.{self.o4} met subnetmasker /{self.sm}'


    def netid(self):
        bit_string = int(self.sm) * '1'
        nulladd = (32-(int(self.sm))) * '0'
        self.networkmask = bit_string+nulladd
        self.n_hosts_bits = 32-int(self.sm)

        IP_adres_list = [self.o1, self.o2, self.o3,self.o4]
        self.ip32bits = ''
        oct_bin = ''
        for oct in IP_adres_list:
            binary = (format(oct,'b'))
            if len(binary) < 8:
                for i in range(8-(len(binary))):
                    binary = '0'+binary
            self.ip32bits +=binary
        # ANDing IP-adres en subnetmask
        c = 0
        self.netid = ''
        self.octs_dec = []
        octet = ''
        for bit in self.networkmask:
            if bit == '1' and self.ip32bits[c] == '1' :
                self.netid += '1'
                octet += '1'
            else:
                self.netid += '0'
                octet += '0'
            c += 1

            if c % 8 == 0:
                dec = int(octet,2)
                self.octs_dec.append(dec)
                octet = ''

        return self.netid, self.octs_dec, self.n_hosts_bits








def subnet_handler(subnet):
    elements = subnet.split('.')
    element4 = elements[-1].split('/')
    Subnet1 = Subnet(elements[0], elements[1], elements[2], element4[0], element4[1])
    print(repr(Subnet1))
    #print(Subnet1.subnetmask())
    bin_subnet, subnet_list, hostsbits = Subnet1.netid()
    subnet_string = ''
    for i in range(3):
        subnet_string += str(subnet_list[i]) +'.'
    subnet = subnet_string
    hosts = 2**hostsbits-2
    print(hosts, subnet_list, subnet)
    return subnet, hosts, subnet_list







#subnet_handler('11.201.23.0/23')
