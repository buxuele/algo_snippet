A = [4,2,5,7] 

n = len(A)
for i in range(n):
    if i % 2 == 0 and A[i] % 2 != 0:
        A.append(A.pop(i))
    if i % 2 != 0 and A[i] % 2 == 0:
        A.append(A.pop(i))

print(A)
