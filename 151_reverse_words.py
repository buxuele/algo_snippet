# author: fanchuangwater@gmail.com
# date: 2020/4/4 上午2:43
# 目的:

nums = [0,0,1,1,1,1, 1,1,2,2,3,3,4]


l = len(nums)
i = 0
while i < l - 1:
    if nums[i] == nums[i+1]:
        print(i, nums[i], nums[i+1])
        nums.pop(i+1)
        l -= 1

    i += 1
print(nums)




















