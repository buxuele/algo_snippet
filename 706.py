# author: fanchuangwater@gmail.com
# date: 2020/4/1 上午5:21
# 目的:

bits = [1, 1, 1, 1]
print(id(bits))

for i in bits:
    if i == 1:
        # bits = bits[2:]
        bits = []
        print(bits)
        print(id(bits))

"""
实际输出如下，怎么解释呢？：
140034905285248
[]
140034905287808
[]
140034903450240
[]
140034905287808
[]
140034903450240
"""



