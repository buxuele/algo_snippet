# 如果是动态规划的话，那么动态转移方程呢？？

import itertools
# 难度确实是难，先放着了。

req_skills = ["a","b","c"]
people = [
    ["a"],
    ["b"],
    ["b","c"]]

# 输出：[0,2]
# 由于数据集比较小。可以使用暴力的全排列。顺便改进以下。
# 然后根据暴力的写法，看看能否再抽出来一种更好的方法、

n = len(people)
s = set(req_skills)
possible = []

# 尝试双指针




# 如下 也许可以得到结果，但是无法获取原始的index值
# for i in range(1, n+1):
#     it = itertools.combinations(people, i)
#     for j in it:
#         # print(j)
#         temp = []
#         for k in j:
#             temp += k
#         # print(temp)
#         if set(temp) == s:
#             possible.append()


 

# people = sorted(people, key=lambda x: -len(x))
# print(people)  貌似暂时没什么必要
 


 