class Singleton1(object):
    _instance = None

    def __new__(self,*args,**kaw):
        if not self._instance:
            self._instance = super(Singleton1,self).__new__(self,*args,**kaw)
        return self._instance

class MyClass(Singleton1):
    pass