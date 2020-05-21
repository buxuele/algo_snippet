# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午10:54
# 目的: 

from functools import reduce
# reduce(func, iter) 最终返回的是一个单一的值


def add_two(x, y):
    return x + y


li = [1, 2, 3]
ret = reduce(add_two, li)
print(ret)      # 返回的是　1+2+3　＝　6


