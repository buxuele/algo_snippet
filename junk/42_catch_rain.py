# author: fanchuangwater@gmail.com
# date: 2020/4/4 下午2:55
# 目的: 大名鼎鼎的接雨水问题。

height = [0,1,0,2,1,0,1,3,2,1,2,1]

# 根据提示的思路。先找到最高点，然后往2侧搜索。
left = 0
right = len(height) - 1

mx = height.index(max(height))
print(mx)








