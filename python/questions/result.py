if __name__ == '__main__':

    v = dict.fromkeys(['k1', 'k2'], [])
    print(v)
    v['k1'].append(666)
    print(v)
    v['k1'] = 777
    print(v)

    i = 20
    print(id(i>1))
    print(id(True))


