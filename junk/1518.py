numBottles = 9 
numExchange = 3


ret = numBottles 
# if numExchange == 0:
#     ret = numBottles
    # break and return 

while numBottles >= numExchange:
    quotient, remainder = numBottles // numExchange, numBottles % numExchange
    ret += quotient 
    numBottles = quotient + remainder 
    print(ret)


print(ret) 




