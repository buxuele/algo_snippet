# author: fanchuangwater@gmail.com
# date: 2020/4/25 下午8:01
# 目的:

import itertools

""" itertools 中有用的函数
1. zip_longest()            默认以None 来填充分组的结果
2. permutations(iter, len)  排序组合, 重点在排序, 包含逆序
3. combinations(iter, n)    可迭代对象中的元素不与自身重复
4. combinations_with_replacement(iter, n),     有重复
5. count(start=1, step=2)
6. repeat(4, 3)           # 4, 4, 4
7. cycle(iter)            # 无线循环下去，类似 while True
8. accumulate(iter)          # 累加
9. product(iter, iter)
"""

a = [1, 2, 3]

ret = itertools.permutations(a, len(a))
print(ret)
for i in ret:
    print(i)





