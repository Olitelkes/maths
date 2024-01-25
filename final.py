from typing import List

def solution(A: List, Y: int) -> List:
    """Create a new list containing the results"""
    return [
        min(A[max(0, index-Y): index])
        for index, _ in enumerate(A, start=1)
    ]

for _ in range(0, 1000):
    solution([3, 4, 1], 2)
    solution([7,3,5,6,9,1,2], 3)