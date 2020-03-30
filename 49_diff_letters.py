# author: fanchuangwater@gmail.com
# date: 2020/3/27 下午3:09
# 目的:

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
strs = ["tea","","eat","","tea","", "some"]


ret = [[] for _ in range(len(strs))]
count = 0
special = []
while strs:
    i = strs.pop(0)
    s = set(i)
    if i:
        for j in range(len(ret)):

                if ret[j]:
                    # if s == set(ret[j][0]):
                    if all(i.count(t) == ret[j][0].count(t) for t in s):
                    # if all(i.count(t) == ret[j][0].count(t) for t in i):
                        ret[j].append(i)
                        break   # 这个　break 很关键。因为已经添加上一个元素之后，那么这一轮的任务就完成了。必须退出循环。
                else:
                    ret[j].append(i)
                    count += 1
                    break
    else:
        special.append("")


print(ret)
print(count)








    # for j in range(len(ret)):
    #     print("yes")    # ret = [[]]　执行了。。。、
    #
    #     if ret[j]:      # 无法执行。
    #         print("memmeme")
    #         if s == set(ret[j][0]):
    #             ret[j].append(i)
    #     else:
    #         print("add me ")
    #         ret.append([])
    #         ret[j].append(i)



