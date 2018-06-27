v = '0b1111011'


def ipconvertint(ip:str):
    s = ip.split('.')
    tar = ''
    for sd in s:
        l = str("%08s" % str(bin(int(sd)))[2:]).replace(' ','0')
        tar += l
    return int(tar,2)

def intconvertip(st:int):
    k = ('%032s'%str(bin(st))[2:]).replace(' ','0')
    j = ''
    tar = ''
    for i,ll in enumerate(k,1):
        j += ll
        if i%8 == 0:
            tar +='{}.'.format(int(j,2))
            j = ''
    return tar[:-1]

if __name__ == '__main__':
    print('{}'.format(v))
    print(int(v,2))
    print(int('17',8))
    print(hex(1000))
    print(bin(1000))
    print(oct(1000))

    # 请编写一个函数实现将IP地址转换成一个整数
    # 10.1.2.100

    ip = '10.1.2.100'
    print(int(b'00001010000000010000001001100100',2))
    print(bin(167838308))
    print(intconvertip(2345671111))
    

    

