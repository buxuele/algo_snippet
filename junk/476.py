# author: fanchuangwater@gmail.com
# date: 2020/5/28 下午12:10
# 目的: 


# num = 476
num = 5
b = format(num, "b")
print(b)

temp = ""
for i in b:
    if i == "0":
        temp += "1"
    else:
        temp += "0"

print(int(temp, base=2))










