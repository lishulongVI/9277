print(abs(-1))


class Func(object):

    def __init__(self):
        self.id = 1

    def calc(self, ab, cd):
        return sum([ab, cd])

    def sub(a, b):
        return a-b
    sub = staticmethod(sub)


f = Func()

d = f.calc(1, 2)
print(d)

g = Func.calc(f, 1, 2)
print(g)

print(f.__dir__)


print(hasattr(f, 'id'))

print(f.id)
