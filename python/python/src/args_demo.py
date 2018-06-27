def test(name,age):
    print(name)
    print(age)

def good(a,b,c):
    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    aaa = {'name':12,'age':13}
    test(**aaa)
    good(*(1,2,3))

    for k in aaa.keys():
        print(k)

    for i in aaa:
        print(i)


    a = 10
    B = 100
    a,B = B,a

    print(a)
    print(B)
