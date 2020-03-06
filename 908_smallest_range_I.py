A = [1, 3, 6]
k = 3

x = [-3, 3]

for i in A:
    temp = i
    for x in range(-k, k+1):
        temp += x

