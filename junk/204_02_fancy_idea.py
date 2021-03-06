# 学习评论区的做法。see https://leetcode-cn.com/u/bruce-33/
# 要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。
# 反正我觉得这个解法很经典。　


def solve(n):
    if n < 2:
        return 0

    # 这里使用 1， 0 分别代表合数，质数，利用下标来表示 数字，这一点上很机智。
    nums = [1] * n      # 代表了 [1, n]之间的所有的数字
    nums[0] = nums[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        # 这里的nums[i] 如果为1的话是执行的，如果是0，则跳过了。
        # 比如ｉ= 2 的时候就已经把4排除掉了，所以i=4是不会执行的
        if nums[i]:
            # 下面这种就是切片的做法，比如 i=2， 那么把，所有2的倍数都排除了，即都变成了0。
            # 前半部分是赋值的范围，后半部分是求出当前有多少个合数。
            # 这里从 i*i 开始确实是很高级的做法。

            # 其实我觉得最难理解的地方在于后半部分　求个数的写法
            # 比如 20 以内能被2，或3整除的数有多少个呢
            # 如果是从20以内， i=2, nums[4:20]，实际上取到的数是第五个。
            # 第一个4 被剔除了，所以最后又加上一个 1
            nums[i * i: n: i] = [0] * ((n-1 - i*i) // i + 1)

    return sum(nums)        # 所有的1的个数。就算质数的总个数。因为上面已经把合数变成0了

