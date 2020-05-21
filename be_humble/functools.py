# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午10:04
# 目的: 

#  @cached_property         只计算一次，然后就把返回值缓存下来了。。


# 可能是需要python3 3.8　
# import functools
# from functools import *

# class DataSet:
#     def __init__(self, nums):
#         self._data = nums
#
#     @cached_property
#     def stdev(self):
#         return statistics.stdev(self._data)
#
#     @cached_property
#     def variance(self):
#         return statistics.variance(self._data)
#

# a = [1, 2, "a"]
# print(a)
#
# print("some %s and %d" % ("ok", 1))
#
# b = [1, 2]
# c = [1, 2]
#
# print(b == c)
# print(b is c)


# class Shirt:
#     def __init__(self, color):
#         self.color = color
#
#
# print(Shirt("blue").color)
#
#
#

