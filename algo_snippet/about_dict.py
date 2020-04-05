# 关于普通的 字典

# 1.对一个字典排序。注意这里是  maybe.items(),而 maybe自身是不行的。
maybe = {}
res = sorted(maybe.items(), key=lambda dic:dic[1], reverse=True)


# 2. 可以用数字作为键的。不知道什么时候改的，或是我原本就记错了。
d1 = {1: "a"}
print(d1)       # {1: 'a'}

d3 = {1: 2}
print("this is d3", d3)  # 也是可行的。

# 3. OrderedDict可以扔了， python3.6开始默认的Dict已经是Ordered了
d2 = {"some": 3, "one": 2, "tell": 1, "me": 0}
print(d2)
x = sorted(d2.items())
print(x)    # [('me', 0), ('one', 2), ('some', 3), ('tell', 1)]




