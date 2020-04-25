# author: fanchuangwater@gmail.com
# date: 2020/4/4 下午11:12
# 目的:

s = "annabelle"
k = 2


def real(w):
    t = len(w) // 2
    if t == 1:
        return True
    else:
        return w[:t] == w[-t:][::-1]


# 分成３部分或者是４部分怎么做呢
for i in range(1, len(s)):
    if real(s[:i]):
        k -= 1

