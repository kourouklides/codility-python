# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    
    N = len(A)
    
    if ((N==0) or (K==0) or (K==N)):
        return A
    
    if (K > N):
        i = K % N
    else:
        i = K
    
    A1 = A[N-i:N]
    A2 = A[0:N-i]
    
    B = A1 + A2
    
    return B
