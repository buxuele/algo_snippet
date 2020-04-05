# author: fanchuangwater@gmail.com
# date: 2020/4/3 上午2:50
# 目的:

s = 5
nums = [2,3,1,2,4,3]


ret = float("inf")
for i in range(len(nums)):
    j = i+1
    while j <= len(nums):
        print(i, j, nums[i:j], sum(nums[i:j]))
        if sum(nums[i:j]) < s:
            j += 1
        else:
            if j-i < ret:
                ret = j-i
            break

print("this is the end", ret)
