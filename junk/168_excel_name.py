# author: fanchuangwater@gmail.com
# date: 2020/5/28 上午11:11
# 目的: 

#
# for i in range(1, 27):
#     print(chr(i+64))
#


n = 780
#
# a = s // 26
# b = s % 26
# print(a)
# print(b)

ret = ""
while n > 26:
    # 这里需要检查一下是否能整除的情况。。。
    if n % 26 == 0:
        # 那么就少进位1， 并且在结尾添加上Z
        ret += chr(26+64)
        n = n // 26 - 1

    else:
        ret += chr(n % 26 + 64)
        n = n // 26
else:
    ret += chr(n + 64)

print(ret[::-1])




