# matrix = [
#     [53,64,90,98,34],
#     [91,53,64,90,98],
#     [17,91,53,64,0]
#     ]

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
# matrix = [
#   [1,2],
#   [2,2]
# ]


m = len(matrix)
n = len(matrix[0])
i = m-1
j = n-1

flag = True
while i > -1:
    while j > -1:
        print(matrix[i][j], matrix[i-1][j-1])
        if matrix[i][j] != matrix[i-1][j-1]:
            flag = False
            break 
        j -= 1
    if not flag:
        break 
    i -= 1

print(flag)

            


# 2. 从1 ---9


