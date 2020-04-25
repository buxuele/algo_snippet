# author: fanchuangwater@gmail.com
# date: 2020/3/25 下午1:56
# 目的:


grid = [[1, 2], [3, 4]]

ret = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        # print(grid[i][j])
        temp = 0
        temp += grid[i][j] * 6
        # 减去自身
        if grid[i][j] > 1:
            temp -= (grid[i][j] - 1) * 2
        # 减去左侧的　
        if j > 0:
            temp -= min(grid[i][j], grid[i][j-1])*2
        # 减去正前方的
        if i > 0:
            temp -= min(grid[i][j], grid[i-1][j])*2
        # print(temp)
        ret += temp

print("ok", ret)













