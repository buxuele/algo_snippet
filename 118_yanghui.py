def generate(rows):
    def next_line(forward_line):
        next_list = [1]
        for i in range(len(forward_line) -1):
            next_list.append(forward_line[i] + forward_line[i+1])
        next_list.append(1)
        return next_list

    res = [[1]]
    if rows == 1:
        return res

    k = 1
    while k != rows:
        forward_line = res[-1]
        next_list = next_line(forward_line)
        res.append(next_list)
        k += 1

    print(res)
    return res

    # 根据前一行，获取下一行

rows = 6
generate(rows)

"""
必须满足这样一个递归的公式: 
f(n) = f(n-1).append(f(n-1)[-1].transform())

"""





