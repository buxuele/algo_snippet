import collections

# deque  是一个双向队列
"""
1. deque 内置的方法
2. append(ele), 在右边添加一个元素
3. appendleft(ele), 在左边添加元素
4. clear() 清空队列
5. copy() 浅拷贝, 这个是自带的方法
6. count(value), 返回指定元素出现的次数
7. extend([]), 从队列向右边扩展一个列表的元素
8. extendleft([]), 注意是向左边，不是整体放在左边
9. index(value), 查找索引位置
10. insert(pos, value), 在指定位置插入值
11. pop(), 获取最右边的元素，并删除该元素
12. popleft(), 获取最左边的元素，并删除该元素
13. remove(value), 删除指定元素
14. reverse(), 队列反转
15. rotate(2), 把最右边的元素放在最左边，指定次数
"""
d = collections.deque()

d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

# d.clear()
# print(d)

# new_deque = d.copy()
# print(new_deque)
print(d.count(2))

d.extend([5, 6, 7])
print(d)

d.extendleft([8, 9, 10])
print(d)

print(d.index(2))

# insert()
d.insert(3, 35)
print(d)

d.remove(10)
print(d)

d.reverse()
print(d)


d.rotate(2)
print(d)










