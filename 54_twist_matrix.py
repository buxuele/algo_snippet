# author: fanchuangwater@gmail.com
# date: 2020/4/3 上午1:39
# 目的:

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

# matrix = [
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# print(zip(*matrix))
# print(list(zip(*matrix)))

a = []
while matrix:
    print(matrix[0])
    a += matrix[0]
    matrix = matrix[1:]
    matrix = list(map(list, zip(*matrix)))[::-1]

print(a)


