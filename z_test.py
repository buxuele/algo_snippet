# d = {1:2, 3:4}
# print()


# m = d.values()
# print(m)
# print(type(m))


import itertools 

n = 2
l = [i for i in range(n**2)]

print(l)

t = itertools.combinations(l, 4)
for x in t:
    print(x)

