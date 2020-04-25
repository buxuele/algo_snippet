# author: fanchuangwater@gmail.com
# date: 2020/4/15 下午7:16
# 目的:


# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。

from collections import deque   # 双向队列　

matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

m = len(matrix)
n = len(matrix[0])
Q = deque([])
visited = set()

#　初始化队列，将所有的起始点加入队列　

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            Q.append((i, j))        #　把所有起点的索引加入到索引中　
            visited.add((i, j))     #  把已经检查的也记录下来　

"""
这种写法的本质上是，
1. 第一步先围绕所有的0开始查找，把0周围的１都变成　1，因为此时的距离是１
2. 然后开始围绕所有是１的元素开始查找，把１变成２，以此类推。
3.　第二轮的时候，如果当前这个元素的２，那么围绕的元素就要变成３
"""
#
# 将所有相邻的节点加入到队列　
while Q:
    i, j = Q.popleft()
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
            matrix[x][y] = matrix[i][j] + 1
            visited.add((x, y))
            Q.append((x, y))










