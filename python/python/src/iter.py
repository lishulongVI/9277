def generator_function():
    for i in range(10):
        yield i

def add(x):
    return x+x
def mutiply(x):
    return x*x

# for item in generator_function():
#     print(item)
if __name__ == '__main__':
    lis = [add,mutiply]

    for i in range(1,100,1):
        l = map(lambda x:x(i),lis)
        print(list(l))
