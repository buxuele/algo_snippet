# ，找到其中最长的回文子序列，并返回该序列的长度。 



st = "bbbab"

 

def find_child_string(st):
    # 如何找到所有的子序列呢
    


s = set()

ret = 0

for i in st:
    if i in s:
        ret += 2 
        s.remove(i)
    else:
        s.add(i)
    
    print(s)


if s:
    ret += 1

print(ret)


    



