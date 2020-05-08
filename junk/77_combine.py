# author: fanchuangwater@gmail.com
# date: 2020/4/30 下午7:57
# 目的:

import itertools


n = 4
k = 2

t = [i for i in range(1, n+1)]
print(t)

a = itertools.combinations(t, k)
for j in a:
    print(j)




