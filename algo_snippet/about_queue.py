import queue

# queue 单向队列，先进先出
"""
1. 注意是包的导入,  import queue 
2. q = queue.Queue(2), 初始化可以指定队列的大小
3. empty(), 判空
4. full(), 是否满了
5. put(), 添加一个元素
6. get(), 获取一个元素
7. qsize(),获取元素的个数

"""

q = queue.Queue(2)

print(q.empty())

q.put("a")
q.put("b")
print(q)
print(q.full())

print(q.get())
print(q.qsize())



