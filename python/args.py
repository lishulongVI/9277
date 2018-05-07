
def retur_args(a, *b, **c):
    print(a)
    print(b) 
    print(c)

retur_args('a',*(1,2,3),**{'name':'lishulong'})


retur_args(1,2,3,**{})

retur_args.count = 1

print(retur_args.count)