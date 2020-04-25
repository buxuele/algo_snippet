# author: fanchuangwater@gmail.com
# date: 2020/3/25 下午11:17
# 目的:


# 先暴力一点试试看

ret = 0
for i in range(10 ** 7):
    if len(str(i)) == len(set(str(i))):
        # print(i)
        ret += 1


print()
print("finally")
print(ret)
