# author: fanchuangwater@gmail.com
# date: 2020/5/28 上午11:44
# 目的: 

a = "23"
b = "6"

# 求 23+ 6

def convert(str_num):
    temp = 0
    res = 0
    for i in str_num[::-1]:
        res += (ord(i) - 48) * (10 ** temp)
        temp += 1

    print(res)
    return res

# convert("234245678")

ret = convert("456") + convert("74154")
print(ret)


