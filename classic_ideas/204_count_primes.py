def solve(n):
    nums = [1] * n
    nums[0] = nums[1] = 0
    for i in range(int(n ** 0.5) + 1):

        # 这里的nums[i] 如果为1的话是执行的，如果是0，则跳过了。
        # 比如ｉ= 2 的时候就已经把4排除掉了，所以i=4是不会执行的
        if nums[i]:

            # 其实我觉得最难理解的地方在于后半部分　求个数的写法
            # 比如 20 以内能被2，或3整除的数有多少个呢
            nums[i*i: n: i] = [0] * (n - i*i -1) // n + 1

    return sum(nums)

