# author: fanchuangwater@gmail.com
# date: 2020/4/1 下午7:31
# 目的:

a = [9,8,4,5,32,64,2,1,0,10,19,27]

# 快速排序
def quick_sort(arr):
    less = []
    greater = []
    if len(arr) <= 1:
        return arr
    p = arr.pop()
    for x in arr:
        if x <= p:
            less.append(x)
        else:
            greater.append(x)

    return quick_sort(less) + p + quick_sort(greater)


ret = quick_sort(a)
print(ret)


