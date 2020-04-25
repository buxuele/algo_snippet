# author: fanchuangwater@gmail.com
# date: 2020/4/25 下午8:23
# 目的:

nums1 = []
nums2 = [1,2,3,4]

ret = []
for i in range(len(nums1)):
    flag = False
    idx = nums2.index(nums1[i])
    for j in range(idx, len(nums2)):        # nums2
        if nums2[j] > nums1[i]:
            ret.append(nums2[j])
            flag = True
            break

    if not flag:
        ret.append(-1)
print(ret)





