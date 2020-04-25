# author: fanchuangwater@gmail.com
# date: 2020/4/4 上午1:57
# 目的: 尝试使用二分法来做。
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/comments/
# 需要再看看。

s = 5
nums = [2,3,1,2,4,3]
left, right, res = 0, len(nums), 0


# 这个函数才是关键，它是用来判断是否可以缩小当前这个窗口的大小的。
def helper(size):
    sum_size = 0
    for i in range(len(nums)):
        sum_size += nums[i]
        if i > size:
            sum_size -= nums[i-size]
        if sum_size >= s:
            return True
    return False



while left <= right:
    mid = (left + right) // 2
    # 如果这个大小的窗口可以缩小，那么就缩小。
    if helper(mid):
        res = mid
        right = mid - 1
    else:
        left = mid + 1




































# if s > sum(nums):
#     print("return 0")
#
# # 双指针都从第一位出发。
# left = 0
# right = 0
# res = len(nums) + 1         # 这里的写法也很机智啊。
# sum_lr = 0                  # 这个指的应该是2个指针之间的和
#
# while right < len(nums):
#     while right < len(nums) and sum_lr < s:
#         sum_lr += nums[right]
#         right += 1
#     while sum_lr >= s:
#         res = min(res, right - left)
#         sum_lr -= nums[left]
#         left += 1




