# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    sum_left = [None]*(N-1)
    sum_right = [None]*(N-1)
    result = [None]*(N-1)
        
    sum_left[0] = A[0]
    for i in range(1, N-1):
        sum_left[i] = A[i] + sum_left[i-1]
        
    sum_right[0] = A[N-1];
    for i in range(1, N-1):
        sum_right[i] = A[N-1-i] + sum_right[i-1]
        
    for i in range(0, N-1):
        result[i] = abs(sum_left[i] - sum_right[N-2-i])
    
    min_diff = min(result)
        
    return min_diff
    
