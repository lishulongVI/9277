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


    c = copy.copy(a)
    d = copy.deepcopy(a)

    print(id(a))
    print(id(b))
    print(id(c))
    print(id(d))
    '''
        4492540088
        4493437760
        4494322280
        4494323288
    '''
    b['aa']='aa'
    c['xx'] = 'xx'
    d['yy'] = 'yy'
    print(a)
    print(b)
    print(c)
    print(d)


    aa = 'name'
    bb = copy.copy(aa)
    cc = copy.deepcopy(aa)

    print(id(aa))
    print(id(bb))
    print(id(cc))

    print('===================')
    # 字符串的 数字的拷贝 深浅 ==
    aa = 'name'
    """
    字符串，数字的深浅拷贝是一样的。
    对于这种gc 有个常量赤，紧是地址改变
    无论修改任意其中一个变量，只是将其指向了另一个内存地址，其他两个变量不会变，字符串同理。
    因此，对于 数字 和 字符串 而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一个内存地址。
    """
    # aa =  1212121212

    aa =  {'name':'beijing','age':20}
    # aa =  [1,2,3,4]
    bb = copy.copy(aa)
    cc = copy.deepcopy(aa)

    print(id(aa))
    print(id(bb))
    print(id(cc))
    print(aa)
    print(bb)
    print(cc)
    # aa = '1'
    # bb = 23
    # cc = 'ddd'
    # dd = 'name'

    # bb.append(1)
    # cc.append(2)

    aa['name'] = '124'

    print('===================')
    print(id(aa))
    print(id(bb))
    print(id(cc))
    # print(id(dd))


    print(aa)
    print(bb)
    print(cc)

