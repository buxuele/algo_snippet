# author: fanchuangwater@gmail.com
# date: 2020/7/11 下午10:29
# 目的: 

# date = "6th Jun 1933"
# d, m, y = date.split(" ")
# print(d, m, y)
#
# if "32".isnumeric():
#     print("ok")
# a = [2, 3, 1]
# a.sort()
# print(a)


# nums = [1,5,0,10,14]
# nums = [6,6,0,1,1,4,6]
# nums = [1,5,6,14,15]
nums = [9,48,92,48,81,31]


# 31, 48, 48,

"""
[9, 31, 48, 48, 81, 92]
[31, 48, 48, 81, 92]
[48, 48, 81, 92]
[48, 48, 81]
33
"""
# nums.sort()
# print(nums)

# [0, 1, 5, 10, 14]       # 去掉右边3个数字
# [0, 1, 1, 4, 6, 6, 6]   # 去掉左边3个数字

# [1, 5, 6, 14, 15]     # 去掉右边2个和左边一个


def t(nums):

    if len(nums) <= 4:
        return 0

    nums.sort()
    print(nums)
    if nums[0] == nums[-1]:
        return 0

    # 如果去掉左边的话
    def helper(x):
        if x[-1] - x[1] > x[-2] - x[0]:
            x = x[:-1]
        else:
            x = x[1:]
        print(x)
        return x

    a = helper(nums)

    b = helper(a)
    c = helper(b)
    return c[-1] - c[0]

ret = t(nums)
print(ret)

