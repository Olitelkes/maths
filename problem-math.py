def solution(A, Y):
    print( [min(A[max(0, i-Y+1):i+1]) for i in range(len(A))] )
    return


for _ in range(0, 100):
    solution([3, 4, 1], 2)
    solution([7,3,5,6,9,1,2], 3)