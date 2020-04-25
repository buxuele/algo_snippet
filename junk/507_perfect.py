from  math import sqrt


# 输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14


def test(num):
    a = int(sqrt(num))
    temp = [1]
    for i in range(1, a):
        # print(i+1)
        if num % (i+1) == 0:
            print(i+1)
            temp.append(i+1)
            temp.append(num // (i+1))


    print(temp)

    return num == sum(temp)



a = 2

test(a)
