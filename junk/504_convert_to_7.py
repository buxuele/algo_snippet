# 输入: 100
# 输出: "202"


def work(num):

    def helper(num):
        temp = []
        b = num % 7

        while num // 7 >= 7:
            num = num // 7  # 如果 a 是大于7 的话， 那么就继续除下去，但是需要把余数保存下来
            temp.insert(0, num % 7)
            print("At now, num is :  ", num, temp)
        else:
            # 此时的 a 是小于7    比如 8 = 7*1 +1
            # temp = temp + str(a) + str(b)
            temp.insert(0, num // 7)

        temp.append(b)
        print(temp)
        print(''.join([str(i) for i in temp]))
        return ''.join([str(i) for i in temp])

    if num >= 7:
        helper(num)

    # 对于负数的话，直接取绝对值，然后按照上面的来就行了。
    elif num <= -7:
        return "-" + helper(abs(num))


    else:
        # num > -7 and num < 7:
        # return num
        print(str(num))
        return str(num)


num = 49   # 1000   2626
work(num)

