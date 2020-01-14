# 练习如何使用递归

# 成功！逐渐累计出来的想法。
# 1. 注意这里递归的写法。。先测试吧 ，我一直以为是这种模式的。。。
# 参考：https://leetcode-cn.com/problems/count-and-say/solution/xin-shou-di-yi-ci-xie-ti-jie-by-quan-wang-zui-xiu/
# 2. 使用内建库类的 groupbBy



# 解法 1，递归。
def solve(n):
    # 外层函数用于处理 递归的前后关系。
    if n == 1:
        return "1"

    new_string = solve(n - 1)               # 这里使用了递归
    res = ''
    many = 1
    i = 0
    while i < len(new_string)-1:
        if new_string[i] == new_string[i+1]:
            many += 1

            print(i, new_string[i])
            print("a")

        else:
            res += str(many)
            res += new_string[i]

            many = 1
            print(i, new_string[i])
            print("b")



        i += 1

    # 如果最后2个数字不相等的话，那么while 循环没法取到最后一位。
    # 所以这里需要处理一下最后一位数字的问题。比如 ”11“
    if new_string[-1] != new_string[i]:
        res += "1"
        res += new_string[-1]
        print("c")
    else:
        res += str(many)
        res += new_string[i]

    print()
    return res


import itertools

def it_solve(n):
    if n == 1:
        return "1"
    res = ""
    for k, g in itertools.groupby(solve(n-1)):
        temp = ''.join(list(g))
        res += str(len(temp))
        res += str(k)
    return res


n = 6
# ok = solve(n)
ok2 = it_solve(n)
print(ok2)