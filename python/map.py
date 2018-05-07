a = map(lambda x: x+1, [1, 2, 3])

print(a)
print(list(a))


b = filter(lambda x: x > 0, range(-4, 5))

print(b)
print(list(b))