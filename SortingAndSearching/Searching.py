def Search(A, v):
    for k in range(len(A)):
        if v == A[k]:
            print("The value you are looking for is on index {} of list A".format(k+1))
        else:
            pass
        
A = [31, 41, 59, 26, 41, 58, 27,41, 29, 94, 14]
Search(A, 59)

            