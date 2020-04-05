# author: fanchuangwater@gmail.com
# date: 2020/4/5 上午9:09
# 目的:


class LFUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.data = {}
        # 我想建立的数据结构类似于   dic = {key: [value, frequency]}

    def get(self, key: int) -> int:
        if key in self.data:
            self.data[key][1] += 1
            return self.data[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.data.items()) <= self.size:
            self.data[key] = [value, 0]
        else:
            self.data.items()







