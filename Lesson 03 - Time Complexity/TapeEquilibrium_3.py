# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    sum1 = A[0]
    sum2 = sum(A) - A[0]
    min_diff = abs(sum1-sum2)
    
    for i in range(1, N-1):
        sum1 += A[i]
        sum2 -= A[i]
        min_diff = min(min_diff, abs(sum1 - sum2))
    
    return min_diff
    
    
