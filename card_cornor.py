# author: fanchuangwater@gmail.com
# date: 2020/3/26 下午9:16
# 目的:

# matrix = \
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# matrix = \
# [
#     [7],
#     [9],
#     [6]
# ]

matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]

m = len(matrix)
n = len(matrix[0])
ret = []
if n == 1:      # 特殊处理？？？
    ret += [t[0] for t in matrix]



# i -= 1 j += 1
flag = True
for i in range(n):
    j = 0
    temp = []
    while i >=0 and j < m:  # 这里的这个3需要修改
        temp.append(matrix[j][i])
        i -= 1
        j += 1
    if flag:
        ret += reversed(temp)
        flag = False
    else:
        ret += temp
        flag = True
# 上面是没有问题的。
# 问题出在了下面这部分。

# 然后是第二部分的切片

for h in range(1, m):
    k = n-1   # k之所以等于n，是因为从最右侧开始切的
    temp2 = []
    while h < m and 0 <= k < n:
        temp2.append(matrix[h][k])
        print(h, k, matrix[h][k])
        h += 1
        k -= 1
    if flag:
        ret += reversed(temp2)
        flag = False
    else:
        ret += temp2
        flag = True
    print(temp2)

print(ret)











