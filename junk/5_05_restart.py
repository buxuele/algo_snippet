import time

# 参考：
# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/shuang-zhi-zhen-fa-bei-xiang-tan-ce-by-miao-su-wu-/
def solve(s):
    s = list(s)

    want = []

    # 根本问题上还是出现在，到底如何判断一个 子串 是一个回文子串。。。
    # 总体上分为2中情况，即起始处的 奇偶：
    for i in range(len(s)):

        s1 = s[i: i+1]
        if len(s1) % 2 == 1:
            print(s1)

        s2 = s[i: i + 2]
        if len(s2) % 2 == 0:
            print(s2)


s = "caabbbd"
# s = "caabttbd"


solve(s)