import functools

a = functools.reduce(lambda x, y: x+y, [1, 2, 3])

print(a)


def gensquare(N):
    for i in range(N):
        yield i**2


for i in gensquare(5):
    print(i, end=" ")

x = gensquare(2)
a = next(x)
b = next(x)

print(a)
print(b)
"""
Traceback (most recent call last):
  File "function_tool.py", line 22, in <module>
    print(next(x))
StopIteration
"""
print(next(x))
