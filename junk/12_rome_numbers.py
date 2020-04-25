# author: fanchuangwater@gmail.com
# date: 2020/4/15 下午8:07
# 目的: 整数转罗马数字

dic = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
# dic2 = {0: "", 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
num = 58
stack = []
j = 0
for i in str(num)[::-1]:
    stack.append(int(i) * (10 ** j))
    j += 1
print(stack)

ret = ""
s = list(reversed(stack))
while s:
    h = s.pop(0)
    if h in dic:
        ret += dic[h]
    else:
        if h >= 1000:
            ret += h // 1000 * "M"
        elif h > 500:
            ret += "D"
            s.insert(0, h-500)  # 减去500剩下的部分　
        elif h == 500:
            ret += "D"

        elif h > 100:
            ret += h // 100 * "C"

        elif h == 100:
            ret += "C"
        elif h > 50:
            ret += "L"
            s.insert(0, h - 50)
        elif h == 50:
            ret += "L"
        elif h > 10:
            ret += h // 10 * "X"
        elif h == 10:
            ret += "X"
        elif h > 5:
            ret += "V"
            s.append(h-5)
        else:
            ret += h * "I"

print(ret)





