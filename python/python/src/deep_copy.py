import copy

if __name__ == '__main__':
    a = {
        'name':'lishulong',
        'age':12,
        'addr':{
            'coutry':'BJ'
        }
    }

    b = a.copy()

    print(id(a))
    print(id(b))

    print(a)
    print(b)


    print(a is b)
    print(a == b)
