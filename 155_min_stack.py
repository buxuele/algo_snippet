# python3 如何实现栈呢？
# 栈的特点，先进后出。
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


# ********* test start here ************
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.data)

res1 = s.getMin()
print(res1)

s.pop()

t = s.top()
print(t)
res2 = s.getMin()
print(res2)
print(s.data)






