def solve(nums):
    temp = nums[0]
    max_ = temp

    for i in range(1, len(nums)):
        if nums[i] + temp > nums[i]:
            max_ = max(nums[i]+temp, max_)
            temp = nums[i] + temp
        else:
            max_ = max(max_, temp, nums[i], nums[i] + temp)
            temp = nums[i]

    print(max_)
    return max_


nums = [-2,1,-3,4,-1,2,1,-5,4]

solve(nums)
