# author: fanchuangwater@gmail.com
# date: 2020/7/25 下午10:04
# 目的


class NumArray:
    def __init__(self, nums: List[int]):
        # 就是大量地使用空间.
        self.nums = nums
        self.n = len(self.nums)
        self.food = [0] * self.n
        self.ret = 0

        # 不必再写一个方法了,直接在初始化的时候就得出全部的结果
        temp = 0
        for i in range(self.n):
            temp += self.nums[i]
            self.food.append(temp)

        # 到了这里，那么我们的　self.food 就已经是有结果了．

    def sumRange(self, i: int, j: int) -> int:
        """
        闭区间[i, j+1] 之间的和就等于是 [0, j+1]  - [0, i]
        """
        self.ret = self.food[j+1] - self.food[i]




























