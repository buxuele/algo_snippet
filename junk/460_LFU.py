# author: fanchuangwater@gmail.com
# date: 2020/4/5 上午9:09
# 目的:

# from collections import OrderedDict
#
# # move_to_end(key)
#
#
# class LFUCache:
#     def __init__(self, capacity: int):
#         self.size = capacity
#         self.data = OrderedDict()
#         # 我想建立的数据结构类似于   dic = {key: [value, frequency]}
#
#     def get(self, key: int) -> int:
#         ret = -1
#         if key in self.data:
#             self.data[key][1] += 1
#             return self.data[key][0]
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         if len(self.data.items()) <= self.size:
#             self.data[key] = [value, 0]
#         else:
#             self.data.items()


class LFUCache:
    # 我觉得是还是要看你怎么来理解这个 "最近最少使用"。 关键在于最近。
    def __init__(self, capacity: int):
        self.size = capacity
        self.keys = []
        self.values = []

    def print_stuff(self):
        print(self.keys)
        print(self.values)

    def get(self, key: int) -> int:
        if self.size == 0:
            return -1
        else:
            # 找到真正的索引位置。
            if key in self.keys:
                index = self.keys.index(key)
                ret = self.values[index]
                # 这里还是需要再排序一下
                self.keys.append(self.keys.pop(index))
                self.values.append(self.values.pop(index))

                return ret
            else:
                return -1

    def put(self, key: int, value: int) -> None:
        if self.size != 0:
            # 首先检查 键是否已经存在了
            if key in self.keys:
                # 那么只是需要修改已有的值就行了
                index = self.keys.index(key)
                self.values[index] = value

                # 然后还是需要修改排序一下的。2.1 暂时先不排序看看是什么结果 确实是需要再排序一下啊。因为我已经到达了测试４　
                self.keys.append(self.keys.pop(index))
                self.values.append(self.values.pop(index))
            else:
                # 紧接着才是检查长度
                if len(self.keys) >= self.size:
                    # 先删除旧的元素然后才能添加新的元素
                    self.keys.pop(0)
                    self.values.pop(0)
                    self.keys.insert(0, key)
                    self.values.insert(0, value)
                else:
                    self.keys.insert(0, key)
                    self.values.insert(0, value)
                    # self.keys.append(key)
                    # self.values.append(value)
            # self.print_stuff()


c = LFUCache(3)
c.put(1, 1)
c.put(2, 2)
c.put(3, 3)
c.print_stuff()
c.put(4, 4)
c.print_stuff()
print(print())



# print(c.get(2))
# print(c.get(1))
# print(c.get(2))
#
# c.put(3, 3)
# c.put(4, 4)
# print()
# print()
#
# print(c.get(3))
# print(c.get(2))
# print(c.get(1))
# print(c.get(4))



# print(c.get(1))
# print(c.get(3))
# print(c.get(4))








