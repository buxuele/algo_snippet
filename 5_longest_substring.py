import itertools

def solve(s):
    # 使用 itertools 是个错误。。。
    # 回文子串，满足的条件是 第一个数与最后一个数是相等的。
    # 1. 找到所有的字串
    # 2. 查看字串的奇偶性，然后比较最长的字串
    # 3. 需要考虑 s == [], or [1]

    want = []   # 目标

    if not s:
        return 0

    else:
        for i in range(1, len(s)+1):
            print()
            print(i)

            temp = list(itertools.combinations(s, i))
            print(temp)   # 是所有的字串列表

            for h in temp:
                # print(h)
                # 奇偶性都是一样的
                for j in range(len(h)):

                    # if j < len(h) / 2 -1 and h[j] == h[-j - 1]:
                    if j < len(h) / 2 and h[j] == h[-j - 1]:
                        print(h, j, len(h) - 1)
                        print(h)
                        if len(h) > len(want):
                            want = list(h)
                            print(want)
                    else:
                        break
                    # print(j, want)

        return want


# s = 'a'
s = 'a3cdabcd'
solve(s)
# print(solve(s), "this is the end")