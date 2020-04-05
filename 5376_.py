# author: fanchuangwater@gmail.com
# date: 2020/4/5 上午11:30
# 目的:


# 双指针。2个都从左边出发。
# nums = [4,3,10,9,8]
nums =[8]
nums.sort(reverse=True)

s = sum(nums)
ret = []
for i in range(len(nums)+1):
    if sum(nums[:i]) > s - sum(nums[:i]):
        print("ans is:  ", nums[:i])
        break




