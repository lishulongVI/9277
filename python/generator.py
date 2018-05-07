G = (x ** 2 for x in range(3))


a = iter(G)

print(a)

print(list(a))

print(list(G))

"""
<generator object <genexpr> at 0x105c0d308>
[0, 1, 4]
[]
"""