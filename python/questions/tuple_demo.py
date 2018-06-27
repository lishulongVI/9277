

if __name__ == '__main__':
    tup = (1,3)
    print(tup[0])
    print(tup[1])
    print(tup.count(1))
    print(type(tup))

    tup = 1,2,3,4
    print(type(tup))
    print(tup)

    for i in tup:
        print(i)
    
    lis = [('name','lilili'),('age',100)]

    for i in lis:
        print(i[0])