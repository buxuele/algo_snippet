# author: fanchuangwater@gmail.com
# date: 2020/5/19 下午9:10
# 目的: 

# s = "abca"
s = "ebcbbececabbacecbbcbe"

cnt = 0
start = 0
end = len(s) - 1
print(s)


while start < end:
    if s[start] == s[end]:
        start += 1
        end -= 1
    else:
        # 问题出现在了这里，如果下面这２种都满足的话，那么怎么办呢。
        # 此时需要分成2条路分别走下去。

        # if s[start] == s[end - 1]:      # 1
        #     start += 1
        #     end -= 2
        # elif s[start + 1] == s[end]:    # 2
        #     start += 2
        #     end -= 1
        # else:
        #     pass
        if s[start] == s[end - 1]:      # 1
            start += 1
            end -= 2
        elif s[start + 1] == s[end]:    # 2
            start += 2
            end -= 1
        else:
            pass

        cnt += 1
    print(s[start: end + 1])
    if cnt > 1:
        break










