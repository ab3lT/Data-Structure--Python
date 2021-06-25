def InsertionIncreasingSort(A):
    for j in range(len(A)):
        key = A[j]
        i= j-1
        while i>=0 and A[i] >= key:
            A[i+1] = A[i]
            i-=1
        A[i+1] = key
    return A

def InsertionDecreasingSort(A):
    for j in range(len(A)):
        key = A[j]
        i= j-1
        while i>=0 and A[i] <= key:
            A[i+1] = A[i]
            i-=1
        A[i+1] = key
    return A

A = [31, 41, 59, 26, 41, 58, 27,41, 29, 94, 14]
print(InsertionIncreasingSort(A))
print(InsertionDecreasingSort(A))


