# python3 如何实现栈呢？
# 栈的特点，先进后出。
# 2中写法都是可行的。但是第二种写法的性能更能好一些。

# 我自己写的。未参考别人的写法之前写的。
# 这种写法，相当于是把列表顺时针旋转90度。那如果是逆时针旋转90度呢，性能上会更好吗？
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def __repr__(self):
        print(self.data)

    # 添加元素
    def push(self, x: int) -> None:
        self.data.insert(0, x)
        # print(self.data)

    def pop(self) -> None:
        self.data.pop(0)
        # print(self.data)

    # 这里是有问题的。这里我只想获取栈顶的值，并且不能删除这个值。
    def top(self) -> int:
        # return self.data.pop(0)
        return self.data[0]

    def getMin(self) -> int:
        return min(self.data)


# 测试一下逆时针旋转90度的性能
class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    # 添加元素
    def push(self, x: int) -> None:
        self.data.append(x)
        # print(self.data)

    def pop(self) -> None:
        self.data.pop()
        # print(self.data)

    # 这里是有问题的。这里我只想获取栈顶的值，并且不能删除这个值。
    def top(self) -> int:
        # return self.data.pop(0)
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)


# ********* test start here ************
# s = MinStack()
# s.push(-2)
# s.push(0)
# s.push(-3)
# print(s.data)
#
# res1 = s.getMin()
# print(res1)
#
# s.pop()
# t = s.top()
# print(t)
# res2 = s.getMin()
# print(res2)
# print(s.data)

s = MinStack2()
s.push(-2)
s.push(0)
s.push(-3)
print(s.data)

res1 = s.getMin()
print(res1)

s.pop()
print(s.data)

t = s.top()
print(t)
res2 = s.getMin()
print(res2)
print(s.data)