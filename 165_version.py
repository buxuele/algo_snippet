# author: fanchuangwater@gmail.com
# date: 2020/3/28 上午1:05
# 目的:

version1 = "0.1"
version2 = "1.1"


def compareVersion(self, version1: str, version2: str) -> int:
    # 问题的焦点来到了 version1 = "1.01", version2 = "1.001"
    # 如何去掉前导０　>>> "00000001".lstrip("0")	# python3中的正确方法。
    # 　https://cloud.tencent.com/developer/ask/63904　　下方的评论。

    """
    "1.1"                   # 因为它是第1个小版本号
    "1.10"                  # 而它是第10个小版本号
    预期   -1 ？？？？
    """
    ret = 0
    a = version1.split(".")
    b = version2.split(".")

    # 去除前导零
    for m in range(len(a)):
        if len(a[m]) > 1:
            a[m] = a[m].lstrip("0")
    for n in range(len(b)):
        if len(b[n]) > 1:
            b[n] = b[n].lstrip("0")
    print(a)
    print(b)

    # 补零，使长度相等。
    if len(a) > len(b):
        b += ["0"] * abs(len(a) - len(b))
    else:
        a += ["0"] * abs(len(a) - len(b))

    # 然后就可以真正的比较了！
    i = 0
    while i < len(a):
        i += 1
        if a[i] > b[i]:
            ret = 1
            break
        elif a[i] < b[i]:
            ret = -1
            break
        else:
            continue


    return ret

# a = version1.split(".")
# b = version2.split(".")
#
# # 去除前导零
# for m in range(len(a)):
#     if len(a[m]) > 1:
#         a[m] = a[m].lstrip("0")
# for n in range(len(b)):
#     if len(b[n]) > 1:
#         b[n] = b[n].lstrip("0")
#
# # 补零，使长度相等。
# if len(a) > len(b):
#     b += ["0"] * abs(len(a) - len(b))
# else:
#     a += ["0"] * abs(len(a) - len(b))
#
# # 然后就可以真正的比较了！
# i = 0
# while i < len(a):
#     if a[i].lstrip("0") > b[i].strip("0"):
#         return 1
#     elif a[i].lstrip("0") == b[i].strip("0"):
#         continue
#     else:
#         return -1
#     i += 1
#
# return 0






