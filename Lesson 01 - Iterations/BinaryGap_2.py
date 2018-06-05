# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    i = N
    max_gap = 0;
    current_gap = -1;
    
    while (i > 0):
        if  (i % 2 != 0):
            if (current_gap > max_gap):
                max_gap = current_gap
            current_gap = 0
        elif (current_gap >= 0):
            current_gap += 1
        i >>= 1
        
    return max_gap
    
    
