A = [2,4,1,3,7,9,5,6]
N = len(A)
for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
    
print(A)