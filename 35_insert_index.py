def solve(nums, target):
    res = 0
    if target in nums:
        print(nums.index(target))
        res = nums.index(target)
        return res
    else:
        # 说明不包含
        if target < nums[0]:
            res = 0
            return res
        if target > nums[-1]:
            res = len(nums)
            return res

        # 说明是在某个区间里面
        for i in range(len(nums)):
            if nums[i] < target < nums[i + 1]:
                res = i + 1
                return res


nums = [1, 3, 5, 10]
# nums = [2,3,4,7,8,9]
target = 7
print(solve(nums, target))

