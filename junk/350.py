# author: fanchuangwater@gmail.com
# date: 2020/7/13 下午10:19
# 目的: 



# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         from collections import Counter
#         return list((Counter(nums1) & Counter(nums2)).elements())


from collections import Counter


nums1 = [1,2,2,1]
nums2 = [2,2]

x = Counter(nums1)
y = Counter(nums2)


print(x)
print(y)


ret = x & y
print(ret)











