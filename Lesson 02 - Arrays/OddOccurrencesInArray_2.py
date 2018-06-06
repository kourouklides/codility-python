# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    unpaired = 0
    
    for i in range(0, N):
        unpaired ^= A[i]
    
    return unpaired
    
