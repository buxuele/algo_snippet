# author: fanchuangwater@gmail.com
# date: 2020/7/26 下午10:32
# 目的: 

# https://leetcode-cn.com/problems/contiguous-sequence-lcci/
# 你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解


nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
temp = -float("inf")
start = 0

while start < n:
    end = start + 1
    if nums[start] < nums[end]:
        start += 1

    while end <= n:
        a = sum(nums[start: end])
        temp = max(temp, a)
        end += 1
    start += 1

print(temp)






