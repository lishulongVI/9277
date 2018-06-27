


# 字符串、列表、元组、字典每个常用的5个方法？


if __name__ == '__main__':
    s = "lishulong"
    # 字符中没有空格
    print(s.isalnum())
    # isalpha() 方法检测字符串是否只由字母组成。
    print(s.isalpha())
    print(s.isdecimal())
    print(s.isdigit())
    print(s.islower())
    print(s.lower())
    print(s.upper())

    """
        True
        True
        False
        False
        True
        lishulong
        LISHULONG
    """

    str = "This Is String Example...Wow!!!"
    print (str.istitle())

    str = "This is string example....wow!!!"
    print (str.istitle())
