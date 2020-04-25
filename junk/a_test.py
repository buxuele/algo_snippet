# author: fanchuangwater@gmail.com
# date: 2020/4/5 上午10:28
# 目的:

a = 4
b = 4
c = 0

ret = ""
a = ["a"] * a
b = ["b"] * b
c = ["c"] * c

a, b, c = sorted([a, b, c], key=lambda x: -len(x))
print(a)
print(b)
print(c)

while a or b or c:
    while a or b:           # a >= b         此时 b 一定是先消耗尽的
        if a:
            if len(a) >= 2:
                ret += "".join(a[:2])           # ret += "a"*2 ; a -= 2  ????
                a = a[2:]
            else:
                ret += a.pop()
        else:
            break
        if b:
            if len(b) >= 2:
                ret += "".join(b[:2])
                b = b[:2]
            else:
                ret += b.pop()
        else:
            break

    print("first round", ret)
    print(a, b , c)


    # while a or c:  # a >= b         此时 b 一定是先消耗尽的
    #     print("what is this", f"{a[0]}")
    #     if ret.endswith(f"{a[0]}"):
    #         if c:
    #             if len(c) >= 2:
    #                 ret += "".join(c[:2])
    #                 c = c[:2]
    #             else:
    #                 ret += c.pop()
    #         else:
    #             print("why", ret)
    #             break
    #         if len(a) >= 2:
    #             ret += "".join(a[:2])  # ret += "a"*2 ; a -= 2  ????
    #             a = a[2:]
    #         else:
    #             ret += a.pop()
    #     else:
    #         if len(a) >= 2:
    #             ret += "".join(a[:2])  # ret += "a"*2 ; a -= 2  ????
    #             a = a[2:]
    #         else:
    #             ret += a.pop()
    #         if c:
    #             if len(c) >= 2:
    #                 ret += "".join(c[:2])
    #                 c = c[:2]
    #             else:
    #                 ret += c.pop()
    #         else:
    #             break


print(ret)
print(a, b, c)







