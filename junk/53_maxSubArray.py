# 给定一个整数数组 nums ，
# 找到一个具有最大和的连续子数组
# （子数组最少包含一个元素），返回其最大和。


def maxSubArray(nums):
    temp = nums[0]
    max_ = temp
    n = len(nums)

    for i in range(1, n):
        if temp + nums[i] > nums[i]:
            max_ = max(max_, temp + nums[i])
            temp = temp + nums[i]
        else:
            max_ = max(max_, temp, temp+nums[i], nums[i])
            temp = nums[i]

    print(max_)
    return max_


nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)
