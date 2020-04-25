# author: fanchuangwater@gmail.com
# date: 2020/4/8 下午6:46
# 目的:

# nums = [-1, 2, 1, 4]
nums = [0,2,1,-3]


target = 1
nums.sort()
temp = []
print(nums)
g = float("inf")
ret = float("inf")
for i in range(1, len(nums) -1):
    if nums[i-1] <= target <= nums[i+1]:
        # temp.append(abs(sum(nums[i-1: i+2]) - target))
        if abs(sum(nums[i - 1: i + 2]) - target) < g:
            g = abs(sum(nums[i - 1: i + 2]) - target)
            ret = sum(nums[i - 1: i + 2])

print(ret)

