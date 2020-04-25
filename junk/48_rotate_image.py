# 这道题按照我最原始的想法。只发现一个等式。
# matrix[index1][index2] = matrix[-index2-1][index1-len(matrix)]
# 但是每次换值之后，下次的值就已经变了，不再是最初的值的。
# 借鉴大神的思路。使用zip(*)
# 官方的思路其实很值得借鉴的。。
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]
m2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

print(matrix)

# 如果不使用 numpy, 而且不使用额外的空间。那么可以做吗？需要交换很多次。具体是多少次呢。。。假如便利的次数不限定的话。
tran = 0
# for index1, value1 in enumerate(matrix):
    # print(index1, value1)
    # print(type(value1))
    # for index2, value2 in enumerate(value1):

        # 这里面涉及到一个过度交换。内存中交换了2遍。所以需要限定。
        # if tran <= len(matrix) ** 2 // 2:
            # print(index2, value2)
            # print("坐标：", index1, index2, "值: ", value2)
            # print(index1, index2, matrix[index1][index2])
            # print(index2-len(matrix), index1-len(matrix), matrix[index2-len(matrix)][index1-len(matrix)])
            # print("hello: ", -index2-1, index1-len(matrix), matrix[-index2-1][index1-len(matrix)])
            # print()
            # matrix[index1][index2] = matrix[index2-len(matrix)][index1 -len(matrix)]
            # matrix[index1][index2], matrix[-index2-1][index1-len(matrix)] = matrix[-index2-1][index1-len(matrix)], matrix[index1][index2]

        # tran += 1
# print(matrix)


def solve(m):
    g = zip(*m)     # 这里其实有点创建新的矩阵的意思。有点涉嫌。。。反正是使用了额外的空间。有点违反题目的规定。
    for i, j in enumerate(g):
        matrix[i] = list(j)[::-1]







solve(matrix)
