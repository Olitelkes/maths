def solution (A, Y):
    i = 1
    B = []
    while i <= len(A):
        k = max(0,i-Y)
        B.append(min(A[k:i]))
        i = i + 1
    return B     

for _ in range(0, 1000):
    solution([3, 4, 1], 2)
    solution([7,3,5,6,9,1,2], 3)


            




    
