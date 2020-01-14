import time

def solve(s):
    s = list(s)                      # 动态规划。。。
    want = []
    if not s:
        want = 0
    if len(s) == 1:
        want = s[0]

    for start in range(len(s)):     # 确保测试用例的长度是大于等于2
        # 0. 总体上划分为： 分别以 1 和 2 为中心往2侧拓展，做不同的处理。
        # 1. 以 1 为中心往2侧拓展, 开始的时候是没有意义的。
        stair = 0
        print()
        # 必须要取到整个初始的奇数
        while stair < len(s) // 2 + 1:
            if start - stair < 0:
                odd = s[0: start + stair+1]
            else:
                odd = s[start-stair: start+stair+1]

            # print(odd)

            if len(odd) % 2 == 1:
                print(odd)
                h = len(odd) // 2
                if odd[:h] == list(reversed(odd[h+1:])) and len(want) <= len(odd):
                    print("find one! **********: ", odd)
                    want = odd
                    stair += 1
                else:
                    break
            else:
                break



        #
        # 2. 以 2 为中心往2侧拓展, 开始的长度是. 假设已经是偶数了。那么怎么移动呢？
        # 此时的 even 也只是一个字串而已
        # 偶数这部分是可行的了
        # 这部分整体就是按照一个假设开始的，那就是 偶数个字串。。。
        # step = 0
        # while step < len(s) // 2+1:
        #     if start - step < 0:
        #         even = s[0: start + 2 + step]
        #     else:
        #         even = s[start - step: start + step + 2]
        #
        #     if len(even) < len(want):
        #         break
        #     else:
        #         print(step, even)
        #         if len(even) % 2 == 0:  # 确保都是偶数。。。
        #             # 用另一种写法来判断是否为回文
        #             t = len(even) // 2
        #             if even[:t] == list(reversed(even[t:])) and len(want) <= len(even):
        #                 want = even
        #                 print("find one! **********: ",even)
        #                 print(start, step, start-step+2)    # tt 4--6
        #                 step += 1
        #             else:
        #                 break
        #         else:
        #             break


    print("this is what you want: ",''.join(want))


# s = 'abcddcba'  # 8
s = "caabbbd"
# s = "caabttbd"
# s = "cab"
# s = 'babad'

solve(s)



# t1 = time.time()
# t2 = time.time()
# print(t2 - t1)

