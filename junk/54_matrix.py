matrix = \
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12],
#   [13,14,15,16],
#   [17,18,19,20]
# ]


m = len(matrix)
n = len(matrix[0])
# i = 0
# j = 0

i = 0
j = 0
ret = []
left = 0
up = 0
while left < n or up < m:
    while i == up and j < n-1:                      # 水平方向
        ret.append(matrix[i][j])
        j += 1
    while j == n-1 and i < m-1:                    # 竖直方向
        ret.append(matrix[i][j])
        i += 1
    while j > left and i == m-1:
        ret.append(matrix[i][j])                   # 水平方向
        j -= 1
    # 这里原本是要停在0　　但是修改为１的时候，就行了。为什么呢。这里需要一个边界。
    # while j == 0 and i > 0:                        # 竖直方向
    # up += 1
    # left += 1
    # n -= 1
    # m -= 1
    while j == left and i > up:                        # 竖直方向
        ret.append(matrix[i][j])
        i -= 1
        print(ret)
    print("forth end: ", ret)
    print(i, j, up, left)

    n -= 1
    m -= 1
    left += 1
    up += 1



    # 上面的结束之后，指针停留的地点是　[0, 0]
    # while i == 1 and j < n-1:
    #     print("run me")
    #     ret.append(matrix[i][j])
    #     j += 1
    #     print(ret)

    # break








