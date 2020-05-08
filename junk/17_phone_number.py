# author: fanchuangwater@gmail.com
# date: 2020/5/3 下午2:04
# 目的: 

import itertools
d = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

digits = "223"
temp = []

for i in digits:
    temp.append(list(d[i]))

print(temp)
ret = []
g = itertools.product(*temp)
for x in g:
    print(x)
    ret.append("".join(x))
print(ret)


