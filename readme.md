1. while nums[i] <= 0 and j < len(nums) - 1 and nums[k] >= 0 and k > j:
这种写法是可行的，但是不一定高效。无法跳出上级循环。
2. 