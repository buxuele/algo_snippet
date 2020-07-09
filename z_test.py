
# print(chr(26+64))
# print(4 % 2)
# print(26*30)    # 780


# for i in range(-10, 0):
#     print(i)

#
# a = {1: "a", 3: "b"}
#
# if "b" in a:
#     print("ok")

nums = [2, 7, 11, 15]
target = 9

have = {}
for index, val in enumerate(nums):
    want = target - val
    if want in have:                            #  直接查看键是否在字典中, 精简.
        print([have[want], index])
    have[val] = index


