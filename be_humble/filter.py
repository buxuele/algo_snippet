# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午10:58
# 目的: 


def add_two(x):
    return x % 2 == 0


li = [1, 2, 3]
ret = filter(add_two, li)
print(list(ret))      # 返回的是　1+2+3　＝　6





