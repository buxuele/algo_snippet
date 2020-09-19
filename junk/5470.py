# author: fanchuangwater@gmail.com
# date: 2020/8/8 下午11:36
# 目的: 

#
# s = "(()))"
#
# # 　栈的思想　　
#
#
# left = 0
# right = 0
#
# for i in s:
#     if i == "(":
#
#     else:
#         # i == ")"
#

import re

s = "))())("


while "())" in s:
    s = s.replace("())", "", 1)

print(s)        # ))(

left = 0
right = 0

for i in s:
    if i == "(":
        left += 1
    if i == ")":
        right += 1

ret = 0

ret += right if right % 2 == 0 else











