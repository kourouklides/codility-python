# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    uniqueInt = A.count(1)
    
    uniqueInt = list([x for x in A if A.count(x) == 1])
    
    return uniqueInt[0]
    
