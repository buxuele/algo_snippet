# author: fanchuangwater@gmail.com
# date: 2020/5/3 下午2:13
# 目的: 一个列表的所有子集

import itertools

nums = [1, 2, 3]

ret = []
for i in range(len(nums)+1):
    temp = itertools.combinations(nums, i)
    for t in temp:
        ret.append(list(t))

print(ret)






