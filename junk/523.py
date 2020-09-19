# author: fanchuangwater@gmail.com
# date: 2020/8/13 下午7:19
# 目的: 


import time

"""
一开始是一点头绪都没有

"""

nums = [23, 2, 4, 6, 7]

# 先尝试最基础的 如何遍历所有 连续的子数组呢
n = len(nums)

k = 6

for i in range(n):
    for j in range(i+2, n+1):
        temp = sum(nums[i: j])
        print(temp, temp % k, nums[i: j])


# k = 6
#
# stack = []

#
# if n < 2:
#     print("False")
#
# pointer = 0
# for i in range(2, n):
#     temp = sum(nums[:i])
#     temp2 = sum(nums[pointer:i])
#     print(nums[:i])
#     print(nums[pointer:i])
#     print()
#     if temp % k == 0 or temp2 % k == 0:
#         print(" True Break")
#     else:
#         stack.append(temp)
#         stack.append(temp2)
#
#     pointer += 1

