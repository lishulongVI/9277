import sys

a = "{motto} and {0}".format('ham', motto='spam')

b = "{1[spam]} run {0.platform}".format(sys, {'spam': 'laptop'})

print(b)

c = [[1, 2], 'string', {}, {}]

d = list(map(ord, 'spam'))

print(d)

print(c.count({}))

d.insert(1, c)

print(d)


a, *b, c = 'spam'

print(a)
print(b)
print(c)


