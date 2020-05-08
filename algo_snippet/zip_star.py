###  python3 zip(）的用法

# 1. 基本操作。按照顺序对多个可迭代对象打包。
a = [1, 2, 3]
b = [4, 5, 6]
T = list(zip(a, b))
print(T)
# [(1, 4), (2, 5), (3, 6)]

# 2.  zip(*)，是解压。
g = zip(*T)
print(list(g))
# [(1, 2, 3), (4, 5, 6)]


# 3. 下面是一个很好的写法
def better_group(nums, n):
    iters = [iter(nums)] * n    # 这里的 n 个迭代器，实际上指向的是同一个地址!
    ret = zip(*iters)
    for i in ret:
        print(i)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
better_group(nums, n)

