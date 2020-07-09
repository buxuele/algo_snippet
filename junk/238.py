# author: fanchuangwater@gmail.com
# date: 2020/6/7 下午8:50
# 目的: 

nums = [1, 2, 3, 4]

right_list = []
temp2 = 1
for j in nums[::-1]:
    right_list.append(temp2)
    temp2 *= j

left_list = []
temp = 1

ret = []
for i in range(len(nums)):
    ret.append(temp * right_list[-1-i])
    temp *= nums[i]

print(ret)





