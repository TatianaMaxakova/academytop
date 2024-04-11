# A = [2,4,1,3,7,9,5,6]
# N = len(A)
# for i in range(N-1):
#     for j in range(N-1-i):
#         if A[j] > A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
    
# print(A)

# A = [2,4,1,3,7,9,5,6]
# N = len(A)
# i = 0
# while i < N-1:
#     j = 0
#     while j < N-1-i:
#         if A[j] > A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
#         j += 1
#     i += 1

# print(A)


A = [2,4,1,3,7,9,5,6]
def bubble_sort(A):
    N = len(A) - 1
    for i in range(N):
        for j in range(N-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

bubble_sort(A)
print(A)