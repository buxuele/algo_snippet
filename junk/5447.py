# author: fanchuangwater@gmail.com
# date: 2020/7/11 下午11:39
# 目的: 

import math
from math import sqrt, floor

n = 7

# 那么实际上 一开始是有2种选择的.需要判断哪种结果最终能走向胜利


take = floor(sqrt(n)) ** 2
n = n - take
print(n)



