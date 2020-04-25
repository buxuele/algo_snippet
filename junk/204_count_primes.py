# 看了一下评论。这道题需要用 厄拉多塞筛法, 见　sovle2()
# see https://www.jianshu.com/p/b1391dc959a9
# 下面的写法是自己写的。对于比较小的数字，还可以，但是对很大的数，速度很慢。
# 怎么证明一个数是质数呢，只要有一个能被小于它的数整除就算质数

import time   # 自己测试看看会使用多少时间


def countPrimes(n):
    coll = {1: 0, 2: 0}       # 来保存一个所有结果的集合
    if n not in coll.keys():
        prime_count = 0
        for i in range(3, n):
            # 下面这3行的写法应该是可行的，只是现在有点问题。。。
            if any([i % j == 0 for j in range(2, i // 2 + 1)]):
                # print(i)
                # 如果满足上面的情况，说明不是一个质数， 那么就可以
                continue
            else:
                # 说明是质数。
                # print(i)
                prime_count += 1
        # print(prime_count + 1)
        return prime_count + 1


    else:
        return coll[n]


# 注意这道题问的是有多少个质数，而不是　是不是质数。
# 初次按照厄拉多塞筛法的思想来实现了代码，但是耗时还是太多了。
# 我觉得主要时间是用在了把数据读进内存中，如何解决这个问题呢？？
# 如何整体删除多个数呢，比如所有被２整除的数，一起删除。

# 这道题先放在这了。下次再看的时候注意看看题解里面的观点。。。

def solve2(n):
    coll = {1: 0, 2: 0}  # 来保存一个所有结果的集合
    if n not in coll.keys():
        nums = [i for i in range(3, n)]
        i = 2
        primes = 1
        while nums:
            for h in nums:
                if h % i == 0:
                    nums.remove(h)
            i = nums[0]
            # print("此时的质数是：　", i)
            primes += 1
            nums.pop(0)
        # print("end: ", primes)
        return primes
    else:
        return coll[n]

t1 = time.time()
n = 499979
# n = 15
# countPrimes(n)
solve2(n)
t2 = time.time()
print("time cost is :  ", t2 - t1)  # 11.448157548904419
