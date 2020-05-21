# author: fanchuangwater@gmail.com
# date: 2020/5/21 上午10:46
# 目的:

s = "babad"


start = 0
end = start + 1

ret = ""
while start < end:
    if s[start: end] == reversed(s[start:end]):
        # 此时是我们想要的
        if end - start > len(ret):
            ret = s[start: end]
        end += 1
    if end > len(s) - 1:
        start += 1
        end = start + 1

    print(ret)









