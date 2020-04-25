# author: fanchuangwater@gmail.com
# date: 2020/4/12 下午9:59
# 目的:

# beginWord = "hit"
# wordList = ["hot","dot","dog","lot","log","cog"]
#


nums = [1,1,1,1, 1, 2, 2, 2, 2,2,3]

i = 0
while i < len(nums) - 1:
    if nums[i] == nums[i+1]:
        nums.pop(i)
        print(nums)
    i += 1


print("in the end :", nums)


