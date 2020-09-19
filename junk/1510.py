# author: fanchuangwater@gmail.com
# date: 2020/7/13 下午7:20
# 目的: 


# 枚举遍历的方式也是可以的:


from math import sqrt


def solution(n):
    # alice start first
    ret = False
    stone = n
    # 2层遍历, 看看所有的情况
    while n:
        for i in range(1, int(sqrt(n)) + 1):
            n = n - i ** 2
            print("alice take: ", i**2)
            print("left is : ", n)
            print()
            if n < 0:
                break
            elif n == 1:
                ret = False
            elif n == 0:
                ret = True
                break
            else:
                for j in range(1, int(sqrt(n)) + 1):
                    print("bob take: ", j ** 2)
                    print("left is : ", n)
                    print()
                    n = n - j ** 2
                    if n < 0:
                        break
                    elif n == 1:
                        ret = True
                        break
                    elif n == 0:
                        ret = False
                        break
                    else:
                        continue

    print(ret)


n = 7
solution(n)
