A = ["bella","label","roller"] 
# A = ["bella","abel","roer"] 
# A = ["cool","lock","cook"] 
# n = len(A)

# temp = A[0]
# ret = {}
 

ret = []
t = set(A[0])
print(t)
for w in t:
    count = [x.count(w) for x in A]
    print(count)
    a = w * min(count)
    print("a: ", a)

    ret += a 

print(ret)

        






# """
# 1. 从已经有的入手 貌似不太好用 不能计算总数 只能再对比后计数。
# 2. 计数然后再统计
# """
# # ret = A[0]  # 把它变成字典的形式。然后再计数统计。
# ret = {x: A[0].count(x) for x in A[0]}
# original_times = ret.copy()
# print(ret)


# for a in A[1:]:
#     for i in a:
#         if i in ret:
#             ret[i] += 1
#         else:
#             pass 

# print(ret)

# out = []

# # 先是能整除，然后再是总数相等。
# # 总数 = len(A) * original_times

# for j in ret:
#     if ret[j] % n == 0 and ret[j] ==  n * original_times[j]:
#         # 下面这里处理的不对。必须是初始值的整数倍。
#         times = ret[j] // n
#         out += j * times

# print(out)



