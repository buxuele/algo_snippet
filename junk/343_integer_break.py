# author: fanchuangwater@gmail.com
# date: 2020/8/8 下午2:54
# 目的: 

from math import sqrt

"""
数学上的问题，最终的结果与 3 有关 


2   1 * 1 = 1
3   1 * 2 = 2
4   2 * 2 = 4
5   2 × *2 *2 = 8
6   3 * 3 = 9  
7   3 * 4 = 12 
8   4 * 4 = 16   
9   4 * 5 = 20   3 * 3 * 3 = 27  2 * 4 * 3
10 　３　×３　×　４　＝　３６　
11   4 * 4 * 3 = 48   3* 3* *3 * 2    =54 
12     3* 3* *3 * 3 = 81  4 * 4 * 4  5*5*2
13   3* 3* *3 *4          108  144

"""

# 1549681956
# 1647086
# 11529602

n = 1
ret = 1

sq = int(sqrt(n))
m = n % sq

if sq ** 2 == n:
    ret = sq ** sq

elif m == 0:
    ret = sq ** (n // sq)

else:
    while n > 0:
        if n == 1:
            ret = ret // sq
            ret *= (sq + 1)
        elif n >= sq:
            ret *= sq
        else:
            ret *= n

        n -= sq


print(sq)
print(ret)



