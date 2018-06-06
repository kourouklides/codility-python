# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    
    n = len(A)
    B = A[:]
    
    for i in range(0, n):
        B[(i + K) % n] = A[i]
    
    return B
