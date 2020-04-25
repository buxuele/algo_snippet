# author: fanchuangwater@gmail.com
# date: 2020/4/15 下午10:21
# 目的: 

# nums = [824,938,1399,5607,6973,5703,9609,4398,8247]
# nums = [128, 12]
nums = [824, 8247]

nums.sort()
n = [str(i) for i in nums]
n.sort(key=lambda x: x[0])
print(n)

print("33" > "30")

#　需要自定义一种排序规则。比如　3 ,30 如果 因为30小于33,所以 30 需要排在3的后面 即为 3 > 30
for i in range(len(n) -1):
    if n[i][0] == n[i+1][0]:
        if len(n[i]) < len(n[i+1]):
            temp = n[i] + ( len(n[i+1]) - len(n[i]) ) * n[i][-1]
            if temp > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]

    print(n)

print("in the end: ", n)
print(''.join(list(reversed(n))))

