# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午10:49
# 目的: 

# map() 会根据提供的函数对指定序列做映射。
# map(func, *iter) 后半部分可以传入多个可迭代对象


def add_two(x):
    return x + 3


li = [1, 2, 3]
ret = list(map(add_two, li))
print(ret)
