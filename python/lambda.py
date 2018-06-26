# 匿名函数
f = lambda x, y, z : x + y + z

print(f(1, 2, 3))

# 带默认参数的函数
f = lambda x = 1,y = 1: x + y


print(f())

# 嵌套lambda 函数
def action(x):
    return (lambda y : x + y)

f = action(1)
print(f(3))