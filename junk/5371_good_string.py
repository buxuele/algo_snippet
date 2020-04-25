# author: fanchuangwater@gmail.com
# date: 2020/3/29 下午1:48
# 目的:

# 这个其实是很难的。
n = 2
s1 = "aa"
s2 = "da"
evil = "b"

"""
aa --> az           26 - 1
b...                0 
ca --->ca           26 - 1
da                  1
"""

# 大环境下
# if s1 == s2:
#     return s1 if evil not in s1 else ""
# 这种写法也是不安全的，因为 s1 = "ab", evil ="abc" 那么就不对了


