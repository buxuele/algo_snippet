# author: fanchuangwater@gmail.com
# date: 2020/5/8 下午6:48
# 目的: 

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
rows = len(matrix)
col = len(matrix[0])

# 这里的dp 是对原始矩阵大小的一个复制。使用列表推导式，一行写出一个矩阵。
dp = [[0] * col for _ in range(rows)]
# 注意是以右下角作为正方形的起始点，应该称为是定点的。

max_side = 0
for i in range(rows):
    for j in range(col):
        if matrix[i][j] == "1":
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                if 0 < i < rows and 0 < j < col:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            max_side = dp[i][j] if dp[i][j] > max_side else max_side
        else:
            dp[i][j] = 0

# 再来证实一下。确实是对的。
# for h in dp:
#     print(h)
print(max_side)










