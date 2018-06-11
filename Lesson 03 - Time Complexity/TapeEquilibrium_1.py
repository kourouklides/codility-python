# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    
    index1 = 0
    index2 = N-1
        
    sum1 = A[index1];
    sum2 = A[index2];
        
    sum1_next = sum1+A[index1+1]
    sum2_next = sum2+A[index2-1]
        
    diff = abs(sum1-sum2)
        
    while (index1 < index2):
        diff = abs(sum1-sum2)
        
        sum1_next = sum1+A[index1+1]
        sum2_next = sum2+A[index2-1]
            
        if ( abs(sum1 - sum2_next) > abs(sum1_next - sum2) ):
            index1+=1
            sum1 += A[index1]
        else:
            index2-=1
            sum2 += A[index2]
        
    return diff
    
# Task Score
# 100%
# Correctness
# 100%
# Performance
# 100%
