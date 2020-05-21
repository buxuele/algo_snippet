# author: fanchuangwater@gmail.com
# date: 2020/5/21 上午11:06
# 目的: 

import itertools

n = 4
k = 3

li = [i for i in range(1, n+1)]
print(li)

p = itertools.permutations(li, n)
for t in p:
    print(t)



