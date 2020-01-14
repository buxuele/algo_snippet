# 找到一个字符串的所有子串
def solve(s):
    s = list(s)
    for start in range(len(s)):
        for end in range(start, len(s)):
            if start <= end:
                end += 1
                print(start, end)
                print("value is :  ", s[start: end])

        start += 1
        print()
        print()

s = 'abcd'
solve(s)