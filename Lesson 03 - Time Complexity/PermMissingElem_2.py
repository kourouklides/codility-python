# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)+1
    missing = N
    for i in range(1, N):
        missing ^= A[i-1]
        missing ^= i
    
    return missing
    
