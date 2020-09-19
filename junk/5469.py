# author: fanchuangwater@gmail.com
# date: 2020/8/8 下午10:56
# 目的: 


def toggle(s, t, start_point):

    # 如下是需要进行操作的实际总数，但是我们的起点还是是需要变化的。
    cnt = 0
    # ａ ---> b
    if ord(s) < ord(t):
        cnt += ord(t) - ord(s)

    # b ------> a
    else:
        cnt += (26 - (ord(t) - ord(s)))

    return cnt - start_point


# s = "input"
# t = "ouput"

s = "abc"
t = "bcd"
k = 10

temp = 0
start_point = 0
for a, b in zip(s, t):
    if a != b:
        cnt = ord(b) - ord(a) if a < else 26 - (a-b)
        check = False
        


# return True

print(temp)








