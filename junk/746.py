# author: fanchuangwater@gmail.com
# date: 2020/8/8 下午8:25
# 目的: 


# cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
n = len(cost)

ret = 0
sum0 = cost[0]
sum1 = cost[1]


for i in range(2, n):
    if i % 2 == 0:
        sum0 += cost[i]
        sum0 = min(sum0, sum1)
    else:
        sum1 += cost[i]
        sum1 = min(sum0, sum1)

    print(i, sum0, sum1)

ret = min(sum0, sum1)
print("ok  ret: ", ret)






