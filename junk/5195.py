# author: fanchuangwater@gmail.com
# date: 2020/4/5 上午11:50
# 目的:

a = 1
b = 1
c = 7

ret = "a" * a + "b" * b + "c" * c
temp = list(ret)
print(temp)

i = 0
while temp:
    if temp[i] == temp[i+2]:
        temp.append(temp.pop(i-1))

    i

