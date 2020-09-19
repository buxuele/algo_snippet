# author: fanchuangwater@gmail.com
# date: 2020/7/25 下午10:05
# 目的: 

# 1025 divisorGame

N = 17

ret = [False] * [N + 1]

if N == 1:
    print("have to lose")

for i in range(1, N+1):
    if N % i == 0:
        ret[i] = True

    else:
        # 说明此时这个数没法被完全整除，那么对于　bob　他的胜负情况是怎么样的呢
        # 如果这个数无法被整除的话，那么ａlice 就取　1
        for j in range(1, N):
            if ret[j] == False:
                ret[i] = True
                break



