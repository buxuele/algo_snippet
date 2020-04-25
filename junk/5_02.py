def solve(s):
    # 使用 itertools 是个错误。。。或者说是使用的不对。
    # 回文子串，满足的条件是 第一个数与最后一个数是相等的。
    # 1. 找到所有的字串
    # 2. 查看字串的奇偶性，然后比较最长的字串
    # 3. 需要考虑 s == [], or [1]

    s = list(s)
    want = []


    for start in range(len(s)):
        for end in range(start, len(s)):
            if start <= end:
                end += 1
                # print(start, end)
                # print("value is :  ", s[start: end])

                # 下面就是判断回文了。
                temp = s[start: end]


                k = 1
                for m in range(len(temp) // 2 + 1):
                    if temp[m] == temp[-m - 1]:
                        k *= 1      # 此时第一次首位相等
                    else:
                        k *= 0      # 否则的话，就直接 排除掉了。
                print(k)
                if k != 0:
                    print(temp)
                    if len(want) < len(temp):
                        want = temp



                # for j in range(len(temp) // 2 + 1):
                #     if temp[j] == temp[-j - 1]:         #
                #         maybe = temp
                #         j += 1                          # 那么就看下一次的首尾是否相等


                        # print(j, temp[j], -j-1, temp[-j-1])



                        # if len(temp) > len(want):
                        #     want = temp
                        # j += 1
                # print(maybe)         # 这个时候才是验证过的。




                    # print(j, want)


                # j = 0
                # while j < len(temp) / 2 and temp[j] == temp[-j - 1]:
                #     if temp[j] == temp[-j - 1]:
                #
                #         print(j, temp[j], -j - 1, temp[-j - 1])
                #         print("yes ! *****************", temp)
                #         print()
                #
                #         if len(temp) > len(want):
                #             want = temp
                #         j += 1
                #
                #     else:
                #         break
                #     # print(j, want)

        start += 1

    print("this is the final res: ", want)

# s = 'a'
s = 'abcdabcd'  # 为什么无法通过这个测试用例呢 ？？？
# s = 'aaaabbb'  # 为什么无法通过这个测试用例呢 ？？？

solve(s)