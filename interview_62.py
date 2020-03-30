# author: fanchuangwater@gmail.com
# date: 2020/3/30 上午1:49
# 目的:

slices = [1,2,3,4,5,6]
ret = []
for i in range(len(slices)):
    me = 0
    s = slices.copy()
    s = s[i:] + s[:i]
    while s:
        print(s)

        if len(s) == 3:
            me += max(s)
            break
        me += s.pop(i)
        s.pop(i - 1)
        print("sorry")
        s.pop(i)
    ret.append(me)

print(ret)













# s = [1,2,3,4,5,6]

# i = 2
# a = s[i:]
# b = s[:i]
# print(a)
# print(b)
# print(a+b)



# ret = []
# for i in range(len(slices)):
#     me = 0
#     s = slices.copy()
#     print(i, s)
#
#     while s:
#         me += s.pop(i)
#         s.pop(i - 1)
#         s.pop(i)
#     ret.append(me)
#     print(me)
#
# print(ret)


# me = 0
# a = 0
# b = 0
# i = 3
# while slices:
#     me += slices.pop(i)
#     print(me, slices)
#     a += slices.pop(i-1)
#     print(a, slices)
#     b += slices.pop(i)
#     print(b, slices)
#
# print(me, a, b)

