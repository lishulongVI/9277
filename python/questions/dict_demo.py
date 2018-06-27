if __name__ == '__main__':
    dic = {
        'name':'lishulong',
        'age':12
    }

    dic1 = {
        'age':23,
        'country':'BJ'
    }
    print(dic.keys())
    print(dic.fromkeys(['name','age']))
    print(dic)

    for letter in 'Python':
        if letter == 'h':
            pass
            print ('这是 pass 块')
            # continue
        print ('当前字母 :', letter)
    print ("Good bye!")
