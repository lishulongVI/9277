#### 1、python 解释器种类和特点
1. cpython 官方解释器，c语言开发，使用最为广泛
2. ipython 基于cpython之上的交互式解析器
3. pypy 目标是执行速度，对python代码进行动态编译
4. jpython java 平台的Python解释器，将Python代码编译成java class代码
5. ironpython IronPython和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。

#### 2、PEP8 Python 编码规范
##### 代码编排
1. 缩进  space
2. 每行最大长度 < 79
3. 类和函数间空2行，业务逻辑无关 空一行 ；类内的 函数之间 空 一行

##### 文档编排
1. doc 
2. 不要在import 引入多个模块
3. from import 出现多个 feature的时候使用 import
4. 避免不必要的空格

##### 注释
1. 注释要在修改代码的时候也一并修改
2. 尽量避免单行注释
3. 避免无所谓注释

##### 命名规则
1. 模块 使用小写 可使用_
2. 包命名尽量短小，使用全部小写的方式，不可以使用下划线。
3. 类命名 BankService 可以使用_ 内部类使用_BankService
4. 异常命名：BankServiceError
5. 函数名,变量 小写 _
6. 常量名 大写 _

```
module_name, packag_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name.
```
#### 3、进制转换

```
v = '0b1111011'

if __name__ == '__main__':
    print('{}'.format(v))
    print(int(v,2))
    print(int('17',8))
    print(hex(1000))
    print(bin(1000))
    print(oct(1000))

```

#### 4、请编写一个函数实现将IP地址转换成一个整数。


```
def ip_convert_int(ip:str):
    s = ip.split('.')
    tar = ''
    for sd in s:
        l = str("%08s" % str(bin(int(sd)))[2:]).replace(' ','0')
        tar += l
    return int(tar,2)

def int_convert_ip(st:int):
    k = ('%032s'%str(bin(st))[2:]).replace(' ','0')
    j = ''
    tar = ''
    for i,ll in enumerate(k,1):
        j += ll
        if i%8 == 0:
            tar +='{}.'.format(int(j,2))
            j = ''
    return tar[:-1]
```

#### 5、python递归的最大层数？


```
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(999)
print(sys.getrecursionlimit())


➜  src python recursion.py
1000
999
```
#### 6、逻辑运算顺序

```
v1 = 1 or 3
v2 = 1 and 3
v3 = 0 and 2 and 1
v4 = 0 and 2 or 1
v5 = 0 and 2 or 1 or 4
v6 = 0 or False and 1

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)

"""
➜  src python luoji.py
1
3
0
1
1
False
"""

```
#### 7、 ascii、unicode、utf-8、gbk 区别？

```
作者：于洋
链接：https://www.zhihu.com/question/23374078/answer/69732605
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

中国人民通过对 ASCII 编码的中文扩充改造，产生了 GB2312 编码，可以表示6000多个常用汉字。汉字实在是太多了，包括繁体和各种字符，于是产生了 GBK 编码，它包括了 GB2312 中的编码，同时扩充了很多。
中国是个多民族国家，各个民族几乎都有自己独立的语言系统，为了表示那些字符，继续把 GBK 编码扩充为 GB18030 编码。
每个国家都像中国一样，把自己的语言编码，于是出现了各种各样的编码，如果你不安装相应的编码，就无法解释相应编码想表达的内容。终于，有个叫 ISO 的组织看不下去了。他们一起创造了一种编码 UNICODE ，这种编码非常大，大到可以容纳世界上任何一个文字和标志。所以只要电脑上有 UNICODE 这种编码系统，无论是全球哪种文字，只需要保存文件的时候，保存成 UNICODE 编码就可以被其他电脑正常解释。
UNICODE 在网络传输中，出现了两个标准 UTF-8 和 UTF-16，分别每次传输 8个位和 16个位。于是就会有人产生疑问，UTF-8 既然能保存那么多文字、符号，为什么国内还有这么多使用 GBK 等编码的人？因为 UTF-8 等编码体积比较大，占电脑空间比较多，如果面向的使用人群绝大部分都是中国人，用 GBK 等编码也可以。
```
#### 8、字节码 和机器码的区别
字节码是一种中间状态（中间码）的二进制代码（文件）。需要直译器转译后才能成为机器码

#### 9、三目运算

```
if __name__ == '__main__':
    a = 10
    v ='a > 10' if a > 10 else 'a <= 10'
    print(v)
```


#### 10、python 2 、3 区别

```
使用 __future__ 模块
print 函数
Integer division
Unicode
xrange
Raising exceptionsHandling exceptions
next() 函数 和 .next() 方法
For 循环变量和全局命名空间泄漏
比较不可排序类型
通过 input() 解析用户的输入返回可迭代对象，而不是列表

作者：知乎用户
链接：https://www.zhihu.com/question/19698598/answer/58808563
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
#### 11、用一行代码实现数值交换

```python
a = 10
B = 100
a,B = B,a

print(a)
print(B)
```

#### 12、*arg和**kwarg作用

```
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
```
#### 13、Python3和Python2中 int 和 long的区别？

```
从本质上来说，long重命名了int，因为在内置只有一个名为int的整型，但它基本跟之前的long一样
python3 没有 long类型

```


#### 14、xrange和range的区别？

```
Python3中的range()函数跟Python2.X的xrange()函数的作用是一样的，
这样可以使用任意的数字，Python3中去除了xrange()函数。

```


#### 15、文件操作时：xreadlines和readlines的区别？

```

```


#### 16、列举布尔值为False的常见值？

```
[]、{} 、None 、"" 、0、 0.0
```


#### 1、字符串、列表、元组、字典每个常用的5个方法？
##### 字符串

```
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
```

##### 列表

```
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
```

```
➜  questions git:(master) ✗ python list_demo.py
1
10
20
[]
[1, 2, 3, 4, 2, 2, 2, 3, 88, 1, 1, 2, 3, 4, 2, 2, 2, 3, 88, 1]
8
11
1
88
[11, 1, 2, 3, 4, 2, 2, 2, 3, 88, 1, 1, 2, 3, 4, 2, 2, 2, 3]
[3, 2, 2, 2, 4, 3, 2, 1, 1, 88, 3, 2, 2, 2, 4, 3, 2, 1, 11]
0.31292481163391117
0.3958115963630944
[88, 11, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1]
```

##### 元组

```
1	cmp(tuple1, tuple2) 比较两个元组元素。
2	len(tuple)计算元组元素个数。
3	max(tuple)返回元组中元素最大值。
4	min(tuple)返回元组中元素最小值。
5	tuple(seq)将列表转换为元组。
```


##### 字典


#### 2、pass的作用？

```
pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句。
```


#### 3、is和==的区别

```
is 比较的是id


== 比较的是值

```

#### 4、简述Python的深浅拷贝以及应用场景


```
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


```

#### 5、Python垃圾回收机制


```
python采用的是引用计数机制为主，标记-清除和分代收集两种机制为辅的策略

引用计数机制的优点：
简单
实时性：一旦没有引用，内存就直接释放了。不用像其他机制等到特定时机。实时性还带来一个好处：处理回收内存的时间分摊到了平时。

引用计数机制的缺点：
维护引用计数消耗资源
循环引用
```
#### 6、Python的可变类型和不可变类型

```
python中的可变数据类型包括字典和列表，而不可变数据类型包括字符串、数字和元组。

可变数据类型中，即便对数据进行更改，数据的id也不会发生变化，而不可变数据类型中，只要对数据的值进行更改，则数据的id就发生变化。

```
#### 7、 一行代码实现9*9乘法表

```
A = "\n".join("\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1, x+1)]) for x in range(1, 10))

print(A)

```
#### 8、请用代码简答实现stack 。


```
class Stack(object):
    def __init__(self):
        self.item = []
    
    def push(self,value):
        self.item.append(value)
    
    def pop(self):
        return self.item.pop()

    def size(self):
        return len(self.item)
    
    def peek(self):
        if len(self.item) > 0:
            return self.item[len(self.item)-1]
        raise Exception('no peek value')


if __name__ == '__main__':
    que = Stack()
    que.push(1)
    que.push(2)
    print(que.peek())
    print(que.pop())
    print(que.size())
    
    

```


#### 9、简述 生成器、迭代器、可迭代对象 以及应用场景

```
迭代器必须实现迭代器协议__iter__和next/__next方法
__iter__返回迭代器的对象称作可迭代对象
迭代器一定是个可迭代对象，但可迭代对象不一定是迭代器，有可能迭代细节交付给另一个类，这个类才是迭代器
生成器一定是一个迭代器，同时也是个可迭代对象
生成器是一种特殊的迭代器，yield关键字可实现懒惰计算，并使得外部影响生成器的执行成为了可能
```


#### 10、谈谈你对闭包的理解

```
使用闭包主要是为了设计私有的方法和变量。
闭包的优点是可以避免全局变量的污染，缺点是闭包会常驻内存，会增大内存使用量，使用不当很容易造成内存泄露。
在js中，函数即闭包，只有函数才会产生作用域的概念。



特性：

1）函数嵌套函数；

2）函数内部可以使用外部的参数和变量；

3）参数和变量不会被垃圾回收机制回收。

1装饰器！！！装饰器是做什么的？？其中一个应用就是，我们工作中写了一个登录功能，我们想统计这个功能执行花了多长时间，我们可以用装饰器装饰这个登录模块，装饰器帮我们完成登录函数执行之前和之后取时间。

2面向对象！！！经历了上面的分析，我们发现外函数的临时变量送给了内函数。大家回想一下类对象的情况，对象有好多类似的属性和方法，所以我们创建类，用类创建出来的对象都具有相同的属性方法。闭包也是实现面向对象的方法之一。在python当中虽然我们不这样用，在其他编程语言入比如JavaScript中，经常用闭包来实现面向对象编程

3实现单利模式！！ 其实这也是装饰器的应用。单利模式毕竟比较高大，，需要有一定项目经验才能理解单利模式到底是干啥用的，我们就不探讨了。
```
#### 11、简述__new__和__init__的区别

创建一个新实例时调用__new__,初始化一个实例时用__init__,这是它们最本质的区别。

new方法会返回所构造的对象，init则不会.

new函数必须以cls作为第一个参数，而init则以self作为其第一个参数.

#### 12、Python垃圾回收机制(常考)


```
Python GC主要使用引用计数（reference counting）来跟踪和回收垃圾。在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。

1 引用计数

PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少.引用计数为0时，该对象生命就结束了。

优点:

简单 实时性 缺点:

维护引用计数消耗资源 循环引用

2 标记-清除机制

基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。

3 分代技术

分代回收的整体思想是：将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合就成为一个“代”，垃圾收集频率随着“代”的存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量。

Python默认定义了三代对象集合，索引数越大，对象存活时间越长。
```

#### 13、有用过with statement吗？它的好处是什么？具体如何实现？

with语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。


#### 14、Python是如何进行内存管理的？

Python引用了一个内存池(memory pool)机制，即Pymalloc机制(malloc:n.分配内存)，用于管理对小块内存的申请和释放。


#### 15、用Python匹配HTML tag的时候，<.>和<.?>有什么区别？

术语叫贪婪匹配( <.> )和非贪婪匹配(<.?> )


#### 16、列举布尔值为False的常见值？

```
[]、{} 、None 、"" 、0、 0.0
```



