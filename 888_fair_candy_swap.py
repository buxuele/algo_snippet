A = [1,2,5]
B = [2,4]

ret = []
# f, g = sorted([A, B], key=lambda t: sum(t))
for i in range(len(A)):
    for j in range(len(B)):
        A[i], B[j] = B[j], A[i]
        if sum(A) == sum(B):
            print(A[i], B[j])
            break
        else:
            A[i], B[j] = B[j], A[i]
            print(A, B)

