# author: fanchuangwater@gmail.com
# date: 2020/7/25 下午10:04
# 目的: 


# 1510 stone game

from math import sqrt


"""
1. 这道题里面暗藏了一个数学上的原理:
对于任意的一个正整数x,   
a = int(sqrt(x))
b = x - a * a 
那么，一定有　a > b ! 

证明代码也可以写一下的:

def prove(x):
    a = int(sqrt(x))
    b = int(sqrt(x - a * a))

    if a >= b:
        print(x, a, b, "yes")
    else:
        print(x, a, b, "oops!!!! this is impossible!")


for i in range(100):
    prove(i)
    
"""
n = 7

ret = [False] * (n + 1)

# 计算 n - i * i 的情况          着重找到能赢的情况

for i in range(1, n+1):
    sq = int(sqrt(i))

    # 如果当前的n是一个平方数,稳赢
    if sq ** 2 == n:
        ret[i] = True

    else:
        # 2. 这里bob 的取值范围只能是在[1, alice取走的数　+ 1]
        for j in range(1, sq+1):

            # 下面这一行再理解一下．．．
            #  3. 注意一点, 这里的 i 代表的是石头的总数量!!!!
            if ret[i - j * j] == False:
                ret[i] = True
                break









