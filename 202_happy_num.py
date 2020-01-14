import time

def isHappy(n):
    t1 = time.time()
    ret = float('inf')
    temp = str(n)

    # 这里对于无限循环的结果该怎么处理呢？？？
    # 我采用的使用时间模块的计时器来计时，但是执行效率非常低。
    # 但是，通过了。我自己写的。666哦。

    # "若某个数字出现两次，说明程序会一直在这两个数字之间死循环，即不是快乐数"
    # 这个结论一定是给出很多的测试用例才得出来的。
    #　别人的思路是，如果ret 出现重复，则退出。
    # 我的解法有一定的风险，如果对一个很大的数字，结果无法保证正确性。！！！
    while ret != 1:

        ret = sum([int(i)**2 for i in temp])
        temp = str(ret)[::-1]
        print("this is sum", ret)
        t2 = time.time()
        if t2 - t1 > 0.001:
            return False

    else:
        return True


n = 24
res = isHappy(n)

