# author: fanchuangwater@gmail.com
# date: 2020/3/27 下午8:38
# 目的:


matrix = \
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

m = len(matrix)
n = len(matrix[0])

for i in range(m):
    for j in range(n):
        print([i, j], matrix[i][j])

"""
这个也是一种很好的思路　
class Solution(object):
    def spiralOrder(self, matrix):
       　
        a = []
        while matrix:
            a += matrix[0]
            matrix = matrix[1:]
            matrix = map(list,zip(*matrix))[::-1]
        return a
        
        
[0, 0] 1
[0, 1] 2
[0, 2] 3
[0, 3] 4
[1, 0] 5
[1, 1] 6
[1, 2] 7
[1, 3] 8
[2, 0] 9
[2, 1] 10
[2, 2] 11
[2, 3] 12

matrix = \
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
]

[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16],
  [17,18,19,20]
]
before:
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7]
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6]

  [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14]
"""
