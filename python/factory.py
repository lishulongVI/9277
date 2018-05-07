def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)

print(f(2))


start = 100

def tester(start):
    def nested(lable):
        global start
        # nonlocal start
        print(lable,start)
        start+=3
    return nested

f = tester(200)
f(102)
print(start)