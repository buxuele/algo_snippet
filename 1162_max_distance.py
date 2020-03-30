# author: fanchuangwater@gmail.com
# date: 2020/3/29 上午8:38
# 目的:

# grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1],[0,1,0,0,0,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,0],[1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1],[0,0,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0],[1,0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1],[0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1],[1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0],[0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0],[1,1,1,1,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0],[0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0],[0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,1,0,1],[0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0],[0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0],[0,1,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1],[0,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1],[0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1],[0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1],[0,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1],[0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0],[1,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1],[0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,0],[1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0],[0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1],[1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1],[1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1],[0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0],[0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0],[1,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1],[0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1],[1,1,0,1,1,1,1,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0],[1,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,1,1],[1,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1],[0,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1],[1,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1],[0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,0,1,0,0,0],[0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0],[1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0],[1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0],[1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1],[0,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0],[0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1],[0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0],[0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0],[0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1],[1,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0],[0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0],[1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0],[0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,0],[0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1],[1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1],[0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1],[0,1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1],[0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0],[0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0],[1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0],[0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0],[0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1],[0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1],[0,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1],[1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1],[0,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0],[0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,1,0,1],[1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0],[1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],[0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,0],[0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,0,0],[0,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,0],[0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1],[1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,1],[0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,0],[1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1],[0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1],[0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1],[0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0],[0,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,1,1],[1,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1],[1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,0,1],[0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1],[0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,1],[0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0],[0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,0],[1,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0],[1,0,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0],[0,1,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0],[0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0],[0,1,0,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,0],[0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0],[1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,0],[1,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0],[1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0],[0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1],[0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],[0,0,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1],[0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,1]]
m = len(grid)
n = len(grid[0])

for x in grid:
    print(x)


# land = []
# ocean = []
#
# for i in range(m):
#     for j in range(n):
#
#
#         if grid[i][j] == 1:
#             land.append([i, j])
#         else:
#             ocean.append([i, j])
#
# # if len(land) == 0 or len(ocean) == 0:
# #     return -1
#
#
# print(land)
# print(ocean)

# 下面是遍历海洋到陆地的距离。

# ret = -1    # init return value
# for a in ocean:
#     real_dis = float("inf")   # 正无穷大。
#     for b in land:
#         # 当前我们判断的是每一块海洋度，相对于每一块陆地的距离，而实际上海洋与陆地的距离应该是取最小值。
#         # 因此我们需要保存每一块海洋与陆地的距离。
#         dis = abs(a[0] - b[0]) + abs(a[1] - b[1])
#         if dis < real_dis:
#             real_dis = dis
#
#     # 当前这一块海洋的循环结束之后，与ret 比较，更新ret
#     if real_dis > ret:
#         ret = real_dis
#
# print("this is the end: ", ret)

