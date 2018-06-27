if __name__ == '__main__':
    i = 10
    j = 10
    print(i is j)
    print(i is not j)
    print(i == j)
    print(i != j)

    print(id(i))
    print(id(j))

    k = {'a':1}
    l = {'a':1}

    print('------------------------')
    print(*k)
    print(*l)
    print('------------------------')
    print(id(k))
    print(id(l))

    print(k is l)
    print(l == k)

    print('------------------------')
   