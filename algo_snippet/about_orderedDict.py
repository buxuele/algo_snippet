import collections

# 参考 https://www.cnblogs.com/zhenwei66/p/6596248.html
# OrderedDict 有序字典
"""
1. clear(), 清空有序字典
2. copy(), 拷贝
3. fromkeys([], value), 指定一个列表，把列表中的值作为字典的key,生成一个字典
4. items(), 返回键值对组成的列表
5. keys(), 所有的 key
6. values(), 
7. move_to_end(key), 把指定的键值对移动到最后
8. pop(key), 获取指定key的value，并在字典中删除
9. 按照后进先出原则，删除最后加入的元素，返回key-value
10. setdefault(key, val), 设置默认值， val可以不指定
11. 
"""


dic = collections.OrderedDict()
dic["a"] = 1
dic["b"] = 2
dic[3] = 3
print(dic)
print()
dic.popitem()
print(dic)
print()
print()



new_dic = dic.copy()
print(new_dic)


names = ["dog", "hippo", "rhino"]
print(dic.fromkeys(names))
print(dic.fromkeys(names, 20))


print(dic.keys())
print(dic.values())


print(dic)

dic.move_to_end("a")
print(dic)

dic.pop("a")
print(dic)

dic["new_stuff"] = 100
print(dic)

print(dic.popitem(), dic)

val = dic.setdefault("f1", 2)
print(val, dic)






