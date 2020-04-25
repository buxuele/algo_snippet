# author: fanchuangwater@gmail.com
# date: 2020/3/30 下午11:09
# 目的:

# 字符串的长度区间是　[4, 12]
s = "25525511135"
# for i in range(len(s)-1):
#     print(s[i])

# if len(s) == 4 or len(s) == 12:
#     print(s.split('.'))     # 此时就可以直接返回结果了。


"""
这种无休止的遍历，显然不是一个很好的解决办法。
# 仔细观察结果发现一个现象，那就算ip里面是有3个点号作为分隔符的。也就是说，我们需要3个指针。
# 进而，如果这3个指针能把数据分割为符合要求的4部分，那就算是符合要求的。
i = 0
j = 1
k = 2
h = 3
ret = []
while i < j < k < len(s):
    # 后面必须留出3个空间。j, k分别占一个，末尾还有ip的第四部分也要占据一位。下面的j, k同理。
    # 开头必须取一位。
    for i in range(1, len(s)-3):
        if int(s[:i]) > 255:
            break
        for j in range(i+1, len(s)-2):
            if int(s[i:j]) > 255:
                break
            for k in range(j+1, len(s)-1):
                if int(s[j:k]) > 255:
                    break
                for h in range(k + 1, len(s)):
                    if len(s[h:]) > 3 or int(s[h:]) > 255:
                        break
                    # if len(s[k:]) > 3 or int(s[k:]) > 255:
                    #     break
                    t = [s[:i], s[i:j], s[j:k], s[k:]]
                    # print(t)

                    # if len(s[k:]) <= 3 and int(s[k:]) <= 255:
                    if t not in ret:
                        print("ok, here we go: ", t)
                        ret.append(t)
                    # else:
                    #     break
                    #     continue    # break



                # 不必全写在这里。每一层开始的时候就可以限定条件了。那样的话可以省去很多不必要的循环。


"""


