import time


def solve(s):
    s = list(s)  # 动态规划。。。
    want = []
    if not s:
        want = 0
    if len(s) == 1:
        want = s[0]
    for start in range(len(s)):          # 奇偶同时取 ???
        box = []
        step = 0

        while step < len(s) // 2 + 1:
            if start - step < 0:
                odd = s[0: start + step + 1]
                even = s[0: start + 2 + step]

            else:
                odd = s[start - step: start + step + 1]
                even = s[start - step: start + step + 2]

            print()
            print("odd:  ", odd)
            print("even :", even)
            step += 1

            # if len(odd) % 2 == 1:
            #             #     print(odd)
            #             #     h = len(odd) // 2
            #             #     if odd[:h] == list(reversed(odd[h + 1:])) and len(want) <= len(odd):
            #             #         print("find one odd! **********: ", odd)
            #             #         want = odd
            #             #         step += 1
            #             #     else:
            #             #         break
            #             # else:
            #             #     break
            #

    print("this is what you want: ", ''.join(want))


# s = 'abcddcba'  # 8
s = "caabbbd"
# s = "caabttbd"


solve(s)

