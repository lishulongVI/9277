class User(object):

    def __init__(self):
        self.__x = None

    def getx(self):
        return self.__x

    def setX(self, value):
        self.__x = value

    def delX(self):
        del self.__x
    x = property(getx, setX, delX, '')


u = User()
u.setX(12)
print(u.getx())

print(u.x)

u.x = 100

print(u.x)

# del u.x
# print(u.x)


class Pepole(object):

    def __init__(self):
        self.__name = None

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

p = Pepole()

p.name = 'lishulong'

print(p.name)