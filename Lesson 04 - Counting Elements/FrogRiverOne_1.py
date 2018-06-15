# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    
    N = len(A)
    
    isNotThere = [True] * (X+1)
    
    counter = 0;
    
    for i in range(0, N):
        if A[i] <= X and  isNotThere[A[i]]:
            isNotThere[A[i]] = False
            counter += 1
            if counter == X:
                return i
    return -1
