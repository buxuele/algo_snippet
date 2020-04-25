# author: fanchuangwater@gmail.com
# date: 2020/3/22 上午11:48
# 目的:

g = [[2,4,3],[6,5,2]]
h = [[1, 2, 3, 4, 5, 6]]


b = list(zip(*h))
print(b)

for i in b:
    print(i)
    print(type(i))
    if (3, 2) in i:
        print("nono")
