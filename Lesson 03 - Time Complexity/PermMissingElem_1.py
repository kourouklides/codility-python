# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A) + 1
    
    sum2 = (N * (N + 1)) // 2
    sum1 = sum(A)
    
    missing = sum2 -sum1
    
    return missing
    
