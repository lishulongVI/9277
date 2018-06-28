from functools import wraps

def singleton(cls):
    instance = {}
    @wraps(cls)
    def get_instance(*args,**kaw):
        if cls not in instance:
            instance[cls] = cls(*args,**kaw)
        return instance[cls]
    return get_instance

@singleton
class MyClass(object):
    a = 1