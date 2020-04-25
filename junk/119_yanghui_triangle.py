# author: fanchuangwater@gmail.com
# date: 2020/3/18 下午6:57
# 目的:

temp1 = [1, 2, 3, 4, 5]

# 尝试直接循环生成

cur = [1]
pre = []
rowIndex = 5
for i in range(1, rowIndex + 1):
    # 每行首个元素为１　
    temp = [1]
    for j in range(1, i):
        temp += [pre[j-1] + pre[j]]

    cur = temp + [1]
    pre = cur









