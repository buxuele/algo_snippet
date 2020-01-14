import itertools

# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
a = list(str(111221))
print(a)
for k, g in itertools.groupby(a):
    print(k, list(g))