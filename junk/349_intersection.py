# 求2个数组的交集



# 这道题最简单啊。需要看看 set 的相关知识点了。有点遗忘了。
#　see https://www.runoob.com/python3/python3-set.html
def solve(s1, s2):
    s1 = set(s1)
    s2 = set(s2)

    temp = s1 & s2
    print(list(temp))

    print(s1)
    print(s2)




nums1 = [1,2,2,1]
nums2 = [2,2]
solve(nums1, nums2)
