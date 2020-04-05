# author: fanchuangwater@gmail.com
# date: 2020/4/5 上午9:11
# 目的: defaultdict　本质上是为dic提供一个初始化的值，键的值，可以指定这个值的类型

from collections import defaultdict

"""
1. default_factory 接收一个工厂函数作为参数, 例如int str list set等
2. defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值默认值的类型由工厂函数决定
"""

# 1. 下面是来统计单词出现的次数
strings = ('puppy', 'kitten', 'puppy', 'puppy','weasel', 'puppy', 'kitten', 'puppy')
d = defaultdict(int)    # pos　Ｘ
for k in strings:
    d[k] += 1
print(d)            # stdout defaultdict(<class 'int'>, {'puppy': 5, 'kitten': 2, 'weasel': 1})
print(d.items())    # dict_items([('puppy', 5), ('kitten', 2), ('weasel', 1)])


# 2. 解释为什么上面的 X 处的int 是怎么回事
d2 = defaultdict(int)
print(d2["something"])      # 输出 0
print(d2["another_thing"])  # 还是输出 0









