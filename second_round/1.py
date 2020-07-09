# author: fanchuangwater@gmail.com
# date: 2020/7/9 下午6:35
# 目的: 



nums = [2, 7, 11, 15]
# nums = [3, 2, 4]
# nums = [-1,-2,-3,-4,-5]
target = 9


have = {}
#
for index, val in enumerate(nums):
    want = target - val
    if want in have:
        print(have[want], index)    # return
    else:
        have[val] = index

