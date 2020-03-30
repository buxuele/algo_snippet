# author: fanchuangwater@gmail.com
# date: 2020/3/28 下午5:08
# 目的:  有序数组的二分查找。


def binary_search(data_list, target):
    start = 0
    end = len(data_list) - 1
    # 这里的条件也是需要注意的  不是 start < end:
    while start <= end:
        # middle = start + (end - start) // 2    #　我记得ＹｏｕＴｕｂｅ上那位的写法是这样的　　
        middle = (start + end) // 2              #　另一种写法。　　
        if data_list[middle] == target:
            return middle
        elif data_list[middle] < target:
            # 这里的　+1 和下面的　-1 都是我之前做错的的地方。
            start = middle + 1
        else:
            end = middle - 1
    return -1


# test some stuff
l = [1, 5, 7, 8, 13, 19, 23, 29]
ans = binary_search(l, 15)
print(ans)      # -1


