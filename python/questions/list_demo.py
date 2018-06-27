if __name__ == '__main__':
    lis = [1,2,3,4,2,2,2,3,88,'2',{1:2}]
    lis = [1,2,3,4,2,2,2,3,88]
    lis.append(1)
    print(lis.count(88))
    print(len(lis))
    lis.extend(lis)
    print(len(lis))
    l = lis.copy()
    lis.clear()
    print(lis)
    print(l)
    print(l.index(88))
    l.insert(0,11)
    print(l[0])
    print(l.pop())
    print(l.pop())
    print(l)
    l.reverse()
    print(l)

    print(5939/18979)
    print(5311/13418)

    # 排序 倒排 无法实现不同类型的
    l.sort(reverse=True)
    """
        Traceback (most recent call last):
        File "list_demo.py", line 21, in <module>
            l.sort(reverse=True)
        TypeError: '<' not supported between instances of 'dict' and 'int'
    """
    print(l)