def compress(chars):
    ret = []
    s = set(chars)
    # print(s)

    dic = {}
    for i in s:
        dic[i] = chars.count(i)

    gg = sorted(dic.items())
    # print(gg)
    for g in gg:
        ret.append(g[0])
        if g[1] == 1:
            continue
        else:
            ret.append(str(g[1]))

    chars = ret
    print(ret)
    print(chars)

    return ret


def compress2(chars):
    #  尝试在原地修改。。

    # for i in chars:
        ...



te = ["a","b","b","c","c","c"]
compress(te)
