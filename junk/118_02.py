def generate(numRows):
    # 这道题成功。自己独立完成的！！！

    # def transform(forward_line):
    #     next_list = [1]
    #     for i in range(len(forward_line) -1):
    #         next_list.append(forward_line[i] + forward_line[i+1])
    #     next_list.append(1)
    #     return next_list

    res = [[1], [1, 1]]
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return res

    # 类型错误，不是逻辑错误！
    # 下面这行不通的原因在于，一个二维列表是不能直接在追加一个一维列表的。只能追加元素。。。
    # res = generate(numRows - 1).append(transform(generate(numRows - 1)[-1]))

    if numRows > 2:
        m1 = generate(numRows - 1)
        print("m1: ", m1)

        res = generate(numRows - 1)


        new_list = [1]
        last_line = generate(numRows-1)[-1]
        for i in range(len(last_line)-1):
            new_list.append(last_line[i] + last_line[i+1])
        new_list.append(1)
        res.append(new_list)

        # print("pretty hhaha", generate(numRows - 1).append(new_list))



        # m2 = transform(generate(numRows - 1)[-1])
        # print("m2: ", m2)
        #
        # res = m1.append(m2)
        # print("why is fucked up !!!", res)
        #
        print("final res is : ", res)


    return res



# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
rows = 5
generate(rows)

aaa = generate(6)
print(aaa)