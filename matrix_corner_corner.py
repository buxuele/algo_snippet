# author: fanchuangwater@gmail.com
# date: 2020/3/30 下午3:47
# 目的: 对角线遍历二维矩阵

import os

"""
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

[
 [ 1, 4, 7 ],
 [ 2, 5, 8 ],
 [ 3, 6, 9 ]
]

[
 [ 1, 2, 4 ],
 [ 7, 5, 3 ],       # 目标数组
 [ 6, 8, 9 ]
]

[
 [ 1, 2, 43 ],
 [ 74, 5, 36 ],
 [ 67, 8, 9 ]
]

[
 [1, 2, 63, 74],
 [35, 56, 87, 138],
 [49, 910,1211,1412],
 [1013,1114,15,16],
 
]

"""

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

m = len(matrix)
n = len(matrix[0])


for j in range(n):
    i = j


#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(i, j, "----> ",matrix[i][j])


