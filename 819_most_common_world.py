import string


# 这道题除了字典排序有点陌生了，其他都是自己做的。
def solve(paragraph, banned):
    paragraph = paragraph.replace(",", " ").replace("  ", " ")
    paragraph = list(paragraph.lower())
    for i in paragraph:
        if i in string.punctuation:
            paragraph.remove(i)
    parag = "".join(paragraph)
    print(parag)
    maybe = {}

    temp_list = parag.split(' ')
    print(temp_list)
    for i in temp_list:
        if i not in maybe and i not in banned:
            maybe[i] = temp_list.count(i)
    print(maybe)

    res = sorted(maybe.items(), key=lambda dic:dic[1], reverse=True)[0][0]
    # print(res)
    # print(type(res))
    return res





pa2 =  "a, a, a, a, b,b,b,c, c"
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["a"]

# solve(paragraph, banned)
print(solve(pa2, banned))