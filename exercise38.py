class IP:
    decimal_ip = ''
    def __init__(self, ip):
        binary_list = [bin(int(x))[2:].zfill(8) for x in ip.split('.')]
        self.decimal_ip = int(''.join(binary_list), 2)

    def absolute_difference(self, comparation):
        return abs(self.decimal_ip - comparation.decimal_ip)
    


ip = IP('20.0.0.0.10')
ip2 = IP('20.0.0.1.0')


print(ip.absolute_difference(ip2))
