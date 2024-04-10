def liner_search(A, N, x):

   for k in range(N):
       if A[k] == x:
           return k
   return -1
