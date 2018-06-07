# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(X, Y, D):
    # write your code in Python 3.6
    
    num = Y - X
    den = D
    jumps = math.ceil(num/den)
    
    return jumps
    
