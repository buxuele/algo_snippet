# author: fanchuangwater@gmail.com
# date: 2020/8/5 下午10:12
# 目的:

# 已经通过


n = 900750
# n = 7
ret = [1, 2, 4]
if n <= 3:
    # return ret[n - 1]
    pass



i = 3
t1 = 1
t2 = 2
t3 = 4
ret = 0

while i < n:
    ret = t1 + t2 + t3
    # ret = (t1 + t2 + t3 ) % 1000000007
    t1 = t2
    t2 = t3
    t3 = ret
    i += 1
    print(i, ret)

print(ret % 900750)

# after 391457