# author: fanchuangwater@gmail.com
# date: 2020/4/25 下午8:01
# 目的:

import itertools

a = [1, 2, 3]

ret = itertools.permutations(a, len(a))
print(ret)
for i in ret:
    print(i)





